#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import xlrd as x


# In[5]:


df=pd.read_csv('emp.csv')


# In[6]:


df


# In[7]:


# Viewing data from df


# In[8]:


# for that use loc() --> called as locate function


# In[9]:


# Another is there called iloc() --> called as index based locate function


# In[12]:


df1 = df.loc[:,['name','gender']]


# In[13]:


df1


# In[14]:


df1 = df.iloc[:,[1,3]]


# In[15]:


df1


# In[16]:


df1 = df.iloc[0:3,[1,3]]


# In[17]:


df1


# In[18]:


df


# In[19]:


df.shape


# In[20]:


r,c = df.shape


# In[21]:


c


# In[22]:


r


# In[23]:


print(r)


# In[28]:


df.head()  # getting first 5 output


# In[29]:


df.tail()  # getting last 5 output


# In[33]:


df.head(2)


# In[34]:


df[2:5]


# In[35]:


df[0::2]  # printing alternate output


# In[37]:


df.columns


# In[38]:


df.name


# In[40]:


df[['name','age']]  # for showing multiple columns


# In[41]:


df.salary


# In[42]:


df.salary.max()


# In[43]:


df.describe()


# In[47]:


df.salary>12


# In[48]:


df3


# In[49]:


df[df.salary>12]


# In[50]:


df[df.salary>21]


# In[51]:


df[df.salary == df.salary.max()] # comparing with 


# In[52]:


x = df.sort_values('salary') 


# In[53]:


x


# In[54]:


df2 = pd.read_csv('read.csv')


# In[55]:


df2


# In[56]:


# here NaN is the missing value. This is not null value. Called "default marker for missing value" 


# In[59]:


# locating NaN [here df2 using as dataset]
df2.fillna(0)


# In[61]:


df2.fillna({'name':'NAME IS MISSING','salary': 0.0})


# In[74]:


df20 = pd.DataFrame({'name':['rd','vk','sg'],'gender':['M','M','M'],'age':[30,24,31]})


# In[75]:


df20



# In[76]:


df21 = pd.DataFrame({'name':['rd','vk','sg'],'position':['all','bat','ball'],'sal':[50000,80000,60000]})


# In[77]:


df21


# In[78]:


pd.merge(df20,df21,on='name',how='inner')


# In[79]:


pd.merge(df20,df21,on='name',how='left')


# In[80]:


pd.merge(df20,df21,on='name',how='right')


# In[81]:


pd.merge(df20,df21,on='name',how='outer')


# In[85]:


# data visualization
pip install matplotlib
# bar graph


# In[86]:


import matplotlib.pyplot as plt


# In[87]:


df2


# In[88]:


x = df2['name']


# In[89]:


y = df2['salary']


# In[90]:


x


# In[91]:


y


# In[92]:


plt.bar(x,y,label='employee data', color='red'
       )


# In[93]:


plt.xlabel('emp name')
plt.ylabel('emp salary')


# In[94]:


plt.xlabel('emp name')
plt.ylabel('emp salary')
plt.title('my company')
plt.legend()
plt.show()


# In[100]:


import matplotlib.pyplot as plt
import pandas as pd
a = pd.read_csv('ss.csv')
d=pd.DataFrame(a)
x = d['name']
y = d['age']
plt.bar(x,y,label='employee data', color='red')
plt.xlabel('emp name')
plt.ylabel('emp age')
plt.title('my company')
plt.legend()
plt.show()


# In[ ]:




