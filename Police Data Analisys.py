#!/usr/bin/env python
# coding: utf-8

# # Working  on Real Project with  python 
# (A Part Of Big Data Analysis)
# 
# Police Dataset 
# 

# # Here,
# the data from a ploice check post is given.
# This data is available as a CSV file. We are going to analyze this data set using the pandas DataFrame.
# 

# In[13]:


import pandas as pd
pol=pd.read_csv(r"C:\Users\Dell\Desktop\Police data in pyton\Police data.csv")
pol.head(1)


# In[4]:


pol.dtypes


# In[7]:


pol.shape


# In[8]:


pol.count()


# In[9]:


pol.index


# In[11]:


pol.nunique()


# In[12]:


pol.head(5)


# # Instruction (For Data Cleaning )
# 1 .  Remove the columns that only contains mssing values
# 

# In[33]:


pol.isnull().sum()


#                                                 pol.drop(columns="country_name",inplace=True)   ## Answer 44

# In[36]:


pol.isnull().sum()


# In[37]:


pol


# In[32]:


pol


# # Question ( Based on Filtering + Values counts)
# 2. For Speeding , were Men or Women stopped more often ?
# 

# In[46]:


import pandas as pd
pl=pd.read_csv(r"C:\Users\Dell\Desktop\987\Police data.csv")
pl.head(1)


# In[47]:


pl.violation.value_counts()


# In[56]:


pl[pl.violation=="Speeding"].driver_gender.value_counts()   # Answer 


# In[59]:





# # Question (Group by ) 
# 3.  Does gender affect who gets searched a stop
# 

# In[60]:


pl


# In[65]:


pl.search_conducted.value_counts()


# In[63]:


pl.groupby("driver_gender").search_conducted.sum()  # answer


# In[71]:


pl[pl.search_conducted==True].driver_gender.value_counts()  # Answer  


# In[75]:


pl[pl.search_conducted==True].driver_gender.count()


# # Question ( mapping + data +type casting )
# 4 . What is the Mean  stop _duration?
# 

# In[145]:


import pandas as pd
pls=pd.read_csv(r"C:\Users\Dell\Desktop\898\Police2.csv")
pls.head(5)


# In[149]:


pls.stop_duration.value_counts()


# In[150]:


pls.stop_duration.map({"0-15 Min":7.5,"16-30 Min":23,"30+ Min":45})


# In[152]:


pls.stop_duration=pls.stop_duration.map({"0-15 Min":7.5,"16-30 Min":23,"30+ Min":45})


# In[154]:


pls.stop_duration.mean()


# In[157]:


pls.dtypes


# # Question  (Group by ,Describe)
# 
# 5. Compare  the age distributions for each violation.
# 

# In[159]:


pls.head()


# In[160]:


pls.violation.unique()


# In[163]:


pls.groupby("violation").driver_age.describe()    # Answer


# In[ ]:




