/*

Cleaning Data in SQL Queries

*/

select * from NashvilleHousing


--------------------------------------------------------------------------------------------------------------------------

-- Standardize Date Format

select SaleDate from NashvilleHousing

alter table NashvilleHousing
alter column SaleDate date


 --------------------------------------------------------------------------------------------------------------------------

-- Populate Property Address data
select a.ParcelID,a.PropertyAddress,b.ParcelID,b.PropertyAddress, isnull(a.PropertyAddress,b.PropertyAddress)
from NashvilleHousing a, NashvilleHousing b
where a.ParcelID=b.ParcelID
and a.[UniqueID ]<>b.[UniqueID ]
and a.PropertyAddress is null

update a
set PropertyAddress = isnull(a.PropertyAddress,b.PropertyAddress)
from NashvilleHousing a, NashvilleHousing b
where a.ParcelID=b.ParcelID
and a.[UniqueID ]<>b.[UniqueID ]


--------------------------------------------------------------------------------------------------------------------------

-- Breaking out Address into Individual Columns (Address, City, State)
select PropertyAddress from NashvilleHousing

select substring(PropertyAddress,1,charindex(',',PropertyAddress,1)-1) as address,
substring(PropertyAddress, charindex(',',PropertyAddress,1)+1, len(propertyaddress)) as city
from NashvilleHousing

alter table nashvillehousing
add PropertySplitAddress nvarchar(255)
alter table nashvillehousing
add PropertySplitCity nvarchar(255)
go
update NashvilleHousing
set PropertySplitAddress=substring(PropertyAddress,1,charindex(',',PropertyAddress,1)-1)
update NashvilleHousing
set PropertySplitCity=substring(PropertyAddress, charindex(',',PropertyAddress,1)+1, len(propertyaddress))

select * from NashvilleHousing


select 
parsename(replace(owneraddress,',','.'),3),
parsename(replace(owneraddress,',','.'),2),
parsename(replace(owneraddress,',','.'),1)
from NashvilleHousing

alter table nashvillehousing
add OwnerSplitAddress nvarchar(255)
alter table nashvillehousing
add OwnerSplitCity nvarchar(255)
alter table nashvillehousing
add OwnerSplitState nvarchar(255)

update NashvilleHousing
set OwnerSplitAddress=parsename(replace(owneraddress,',','.'),3)
update NashvilleHousing
set OwnerSplitCity=parsename(replace(owneraddress,',','.'),2)
update NashvilleHousing
set OwnerSplitState=parsename(replace(owneraddress,',','.'),1)

select * from NashvilleHousing
--------------------------------------------------------------------------------------------------------------------------


-- Change Y and N to Yes and No in "Sold as Vacant" field

select SoldAsVacant, count(SoldAsVacant)
from NashvilleHousing
group by SoldAsVacant
order by 2

select SoldAsVacant,
case when SoldAsVacant = 'N' then 'No'
	 when SoldAsVacant = 'Y' then 'Yes'
	 else SoldAsVacant
end
from NashvilleHousing

update NashvilleHousing
set SoldAsVacant = case when SoldAsVacant = 'N' then 'No'
	 when SoldAsVacant = 'Y' then 'Yes'
	 else SoldAsVacant
	 end

-----------------------------------------------------------------------------------------------------------------------------------------------------------

-- Remove Duplicates
with rownumCTE as(
select *,
row_number() over (partition by
parcelID, landuse, propertyaddress, saledate, saleprice, legalreference
order by UniqueID) row_num
from nashvillehousing
)
delete
from rownumCTE
where row_num>1
select * from nashvillehousing
---------------------------------------------------------------------------------------------------------

-- Delete Unused Columns

alter table nashvillehousing
drop column owneraddress, taxdistrict, propertyaddress, saledate
















-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------

--- Importing Data using OPENROWSET and BULK INSERT	

--  More advanced and looks cooler, but have to configure server appropriately to do correctly
--  Wanted to provide this in case you wanted to try it


--sp_configure 'show advanced options', 1;
--RECONFIGURE;
--GO
--sp_configure 'Ad Hoc Distributed Queries', 1;
--RECONFIGURE;
--GO


--USE PortfolioProject 

--GO 

--EXEC master.dbo.sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'AllowInProcess', 1 

--GO 

--EXEC master.dbo.sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'DynamicParameters', 1 

--GO 


---- Using BULK INSERT

--USE PortfolioProject;
--GO
--BULK INSERT nashvilleHousing FROM 'C:\Temp\SQL Server Management Studio\Nashville Housing Data for Data Cleaning Project.csv'
--   WITH (
--      FIELDTERMINATOR = ',',
--      ROWTERMINATOR = '\n'
--);
--GO


---- Using OPENROWSET
--USE PortfolioProject;
--GO
--SELECT * INTO nashvilleHousing
--FROM OPENROWSET('Microsoft.ACE.OLEDB.12.0',
--    'Excel 12.0; Database=C:\Users\alexf\OneDrive\Documents\SQL Server Management Studio\Nashville Housing Data for Data Cleaning Project.csv', [Sheet1$]);
--GO


















