--Looking at total cases and total deaths
--Shows likelihood of dying (percentage) if you contract covid in your country
select location, date, total_cases,total_deaths, (total_deaths/total_cases)*100 as deathPercentage
from CovidDeaths
where location like 'Viet%'
order by 1,2

--Looking at total cases and population
--Shows what percentage of population got Covid
select location, date, total_cases,population, (total_cases/population)*100 as casePercentage
from CovidDeaths
where location like 'Viet%'
order by 1,2

--Looking at countries with highest infection rate compared to Population
select location,population,max(total_cases) as highestInfectionCount, (Max(total_cases)/population)*100 as casePercentage
from CovidDeaths
group by location,population
order by 4 desc

--Showing countries with highest death count
select location, Max(total_deaths) as TotalDeathCount
from CovidDeaths
where continent is not null
group by location
order by 2 desc


--Let's breaking down by continent 

--Showing continents with the highest death count
select continent, Max(total_deaths) as TotalDeathCount
from CovidDeaths
where continent is not null
group by continent
order by 2 desc


--Global numbers
select date, Sum(new_cases) as Cases, Sum(new_deaths) as Deaths, Sum(new_deaths)/Sum(new_cases)*100 as DeathPercentage
from CovidDeaths
where continent is not null
group by date
order by 1,2 desc




--Looking at total vaccinations and population
select dea.continent, dea.location, dea.date, dea.population,vac.new_vaccinations,
Sum(vac.new_vaccinations) over (partition by dea.location order by dea.location,dea.date)
as RollingPeopleVaccinated
from CovidDeaths dea,CovidVaccinations vac
where dea.location = vac.location and dea.date = vac.date and dea.continent is not null
order by 2,3

--create CTE
with PopVsVac(continent, location, date, population, vaccinations, rollingPeopleVaccinated)
as
(
select dea.continent, dea.location, dea.date, dea.population,vac.new_vaccinations,
Sum(vac.new_vaccinations) over (partition by dea.location order by dea.date)
as RollingPeopleVaccinated
from CovidDeaths dea,CovidVaccinations vac
where dea.location = vac.location and dea.date = vac.date and dea.continent is not null
)
select *, (rollingPeopleVaccinated/population) *100 as percentagePeopleVaccinated from PopVsVac


--create temp table:
drop table if exists #PopvsVac
create table #PopvsVac
(
continent nvarchar(100),
location nvarchar(100),
date datetime,
population numeric,
new_vaccinations numeric,
rollingPeopleVaccinated numeric
)
Insert into #PopvsVac
select dea.continent, dea.location, dea.date, dea.population,vac.new_vaccinations,
Sum(vac.new_vaccinations) over (partition by dea.location order by dea.location,dea.date)
as RollingPeopleVaccinated
from CovidDeaths dea,CovidVaccinations vac
where dea.location = vac.location and dea.date = vac.date and dea.continent is not null


select *, (rollingPeopleVaccinated/population)*100 as percentagePeopleVaccinated from #PopvsVac