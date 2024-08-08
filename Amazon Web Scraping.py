#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import time
import datetime 
import requests


# In[3]:


URL = 'https://www.amazon.com/Data-Analyst-Programmer-Accountant-T-Shirt/dp/B0C1TCPZG5/ref=sr_1_4?crid=CU1Y4O95IOPK&dib=eyJ2IjoiMSJ9.ZppBLSWPvPm5RFqNGsT3Vcf-TCA0UHx3_i_GqzvkgsU9Xg-IzMGnys93_FcapDMZxpymRVz9JNrsX0VVAEbuQVgQ7rgiPQPK_yn_QzqkZAr8GYFNOfOxsE80G7msFckKkIjHJ956Nz8rkNsyLukS8ytpqsA_Wo7pKSyZPDofi2aoQwGd_rfGax-O34Tmvvf4hRJfO0uBPidj3lUzK76wgHSza5musVLvbr0TMDoZYpCUjW1iyHITos4NqcUe2jZfxeCRt6k4bwp11V2rwqfdlokrS9QRCee0EBu5-MZ7xYI.1diIhYQI1yBj5uiAFduFU4lJUsZF6weEJ2Um2yjoXpg&dib_tag=se&keywords=data+analyst+tshirt&qid=1722668459&sprefix=%2Caps%2C613&sr=8-4'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate, br, zstd","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
page = requests.get(URL, headers = headers)
soup1 = BeautifulSoup(page.content, "lxml")
print(soup1)


# In[5]:


soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
print(soup2)


# In[13]:


title = soup2.find(id = 'productTitle').get_text().strip()
price = soup2.find(class_="a-offscreen").get_text().strip()
print(title)
print(price)


# In[14]:


price = price.strip()[1:]


# In[15]:


price


# In[16]:


title = title.strip()


# In[17]:


title


# In[29]:


import csv
header = ['Title', 'Price','Date']
data = [title, price, today]
with open('AmazonScraping.csv','w', newline = '',encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[28]:


today = datetime.date.today()
print(today)


# In[30]:


import pandas as pd
df = pd.read_csv(r"C:\Users\ACER\AmazonScraping.csv")


# In[31]:


df


# # append data

# In[32]:


with open('AmazonScraping.csv','a+', newline = '',encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[49]:


def check_price():
    URL = 'https://www.amazon.com/Data-Analyst-Programmer-Accountant-T-Shirt/dp/B0C1TCPZG5/ref=sr_1_4?crid=CU1Y4O95IOPK&dib=eyJ2IjoiMSJ9.ZppBLSWPvPm5RFqNGsT3Vcf-TCA0UHx3_i_GqzvkgsU9Xg-IzMGnys93_FcapDMZxpymRVz9JNrsX0VVAEbuQVgQ7rgiPQPK_yn_QzqkZAr8GYFNOfOxsE80G7msFckKkIjHJ956Nz8rkNsyLukS8ytpqsA_Wo7pKSyZPDofi2aoQwGd_rfGax-O34Tmvvf4hRJfO0uBPidj3lUzK76wgHSza5musVLvbr0TMDoZYpCUjW1iyHITos4NqcUe2jZfxeCRt6k4bwp11V2rwqfdlokrS9QRCee0EBu5-MZ7xYI.1diIhYQI1yBj5uiAFduFU4lJUsZF6weEJ2Um2yjoXpg&dib_tag=se&keywords=data+analyst+tshirt&qid=1722668459&sprefix=%2Caps%2C613&sr=8-4'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate, br, zstd","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page = requests.get(URL, headers = headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(id = 'productTitle').get_text().strip()
    price = soup2.find(class_="a-offscreen").get_text().strip()
    price = price[1:]
    today = datetime.date.today()
    import csv
    header = ['Title', 'Price','Date']
    data = [title, price, today]
    with open('AmazonScraping.csv','a+', newline = '',encoding = 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[50]:


while(True):
    check_price()
    time.sleep(1)


# In[51]:


import pandas as pd
df = pd.read_csv(r"C:\Users\ACER\AmazonScraping.csv")
df


# In[ ]:





# In[ ]:





# In[ ]:




