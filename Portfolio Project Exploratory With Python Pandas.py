#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries


# In[1]:


import pandas as pd
import seaborn as sns


# In[2]:


df = pd.read_csv("TWO_CENTURIES_OF_UM_RACES.csv")


# In[3]:


# See the data thats been imported:


# In[4]:


df.head(10)


# In[5]:


df.shape


# In[6]:


df.dtypes


# In[7]:


# CLean up data
# Only want USA racers, 50k, 50 miles and in 2020


# In[8]:


# Step 1: show 50mi or 50km


# In[9]:


array_data = df["Event distance/length"].unique()


# In[10]:


print(list(array_data))


# In[11]:


# combine 50km and 50mi with isin


# In[12]:


df[df["Event distance/length"].isin(['50km','50mi'])]


# In[13]:


df[(df["Event distance/length"].isin(['50km','50mi'])) & (df["Year of event"] == 2020)]


# In[14]:


df[df["Event name"].str.split("(").str.get(1).str.split(")").str.get(0) == 'USA']


# In[15]:


df[(df["Event distance/length"].isin(['50km','50mi'])) & (df["Year of event"] == 2020) & (df["Event name"].str.split("(").str.get(1).str.split(")").str.get(0) == 'USA')]


# In[16]:


df2 = df[(df["Event distance/length"].isin(['50km','50mi'])) & (df["Year of event"] == 2020) & (df["Event name"].str.split("(").str.get(1).str.split(")").str.get(0) == 'USA')]


# In[17]:


df2.head(10)


# In[18]:


df2.shape


# In[19]:


#Remove (USA) from event name


# In[20]:


df2["Event name"].str.split("(").str.get(0)


# In[21]:


df2["Event name"] = df2["Event name"].str.split("(").str.get(0)


# In[22]:


df2


# In[23]:


#Clean up athlete age


# In[24]:


df2["Athlete_Age"] = 2024 - df2["Athlete year of birth"]


# In[25]:


#Remove h from athlete performance


# In[26]:


df2["Athlete performance"] = df2["Athlete performance"].str.split("h").str.get(0)


# In[27]:


df2.head(5)


# In[28]:


#Drop columns: Athlete Club, Athlete Country, Athlete year of birth, Athlete Age Category


# In[29]:


df2 = df2.drop(["Athlete club","Athlete country","Athlete year of birth","Athlete age category"],axis = 1)


# In[30]:


df2.head()


# In[31]:


df2.isna().sum()


# In[32]:


df2[df2["Athlete_Age"].isna()]


# In[33]:


df2 = df2.dropna()


# In[34]:


#Check for duplicates


# In[35]:


df2[df2.duplicated()]


# In[36]:


#Reset index:


# In[37]:


df2.reset_index(drop = True )


# In[38]:


#Fix types:


# In[39]:


df2.dtypes


# In[40]:


df2["Athlete_Age"] = df2["Athlete_Age"].astype(int)


# In[41]:


df2["Athlete average speed"] = df2["Athlete average speed"].astype(float)


# In[42]:


df2 = df2.reset_index(drop = True )


# In[43]:


df2


# In[44]:


df2 = df2.rename(columns = {"Year of event":'year',
                           "Event dates": "race_day",
                           "Event name": "race_name",
                           "Event distance/length": "race_length",
                            "Event number of finishers": "race_number_of_finishers",
                           "Athlete performance": "athlete_performance",
                           "Athlete gender": "athlete_gender",
                           "Athlete average speed": "athlete_avg_speed", 
                           "Athlete ID": "athlete_id",
                            "Athlete_Age": "athlete_age"
                           })


# In[45]:


#Reorder columns:


# In[46]:


df3 = df2[["race_day","race_name","race_length","race_number_of_finishers","athlete_id","athlete_gender","athlete_age","athlete_performance","athlete_avg_speed"]]


# In[47]:


df3


# In[48]:


#Find athlete id = 222509


# In[49]:


df3[df3["athlete_id"] == 222509]


# In[50]:


#Charts and graphs:


# In[51]:


sns.histplot(df3, x ='race_length', hue = 'athlete_gender')


# In[52]:


sns.displot(df3[df3['race_length'] == '50mi']['athlete_avg_speed'])


# In[53]:


sns.violinplot(data = df3, x = 'race_length', y = 'athlete_avg_speed', hue = 'athlete_gender', split = True, inner = 'quartile')


# In[55]:


sns.lmplot(df3, x = 'athlete_age', y = 'athlete_avg_speed', hue = 'athlete_gender')


# In[56]:


#Difference in speed for the 50k and 50mi male to female


# In[57]:


df3.groupby(['race_length','athlete_gender'])['athlete_avg_speed'].mean()


# In[58]:


#What age group are the best in the 50m race (20 + race min)


# In[64]:


df3.query('race_length == "50mi"').groupby('athlete_age')['athlete_avg_speed'].agg(['mean','count']).sort_values('mean',ascending = False).query('count>19').head(15)


# In[65]:


#Season for the data --> slower in summer than winter?
#spring: 3-5
#summer: 6-8
#fall: 9-11
#winter: 12-2


# In[68]:


df3['race_month'] = df3['race_day'].str.split('.').str.get(1)


# In[78]:


df3.head()


# In[75]:


df3['race_month'] = df3['race_month'].astype(int)


# In[76]:


df3.dtypes


# In[80]:


df3['race_season'] = df3['race_month'].apply(lambda x: 'Winter' if x>11 else 'Fall' if x>8 else 'Summer' if x>5 else 'Spring' if x>2 else 'Winter')


# In[82]:


df3.head()


# In[83]:


df3.groupby('race_season')['athlete_avg_speed'].agg(['mean','count']).sort_values('mean', ascending = False)


# In[84]:


# 50miler only:


# In[86]:


df3.query('race_length == "50mi"').groupby('race_season')['athlete_avg_speed'].agg(['mean','count']).sort_values('mean', ascending = False)


# In[ ]:





# In[ ]:




