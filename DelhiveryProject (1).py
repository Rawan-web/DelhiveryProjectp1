#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[45]:


pd.read_csv("D:/TECHNO CO WORD PROJECTS/project/delhivery.csv")


# In[46]:


df=pd.read_csv("D:/TECHNO CO WORD PROJECTS/project/delhivery.csv")


# In[47]:


df.shape


# In[48]:


df['od_start_time']= pd.to_datetime(df['od_start_time'])


# In[49]:



df.fillna(df.mean())


# In[ ]:


df.fillna(df.mean())


# In[ ]:


pd.actual_time.unique()
pd


# In[ ]:


X =dataset.iloc[ : , :-1].values


# In[ ]:


Y =dataset.iloc[ : , -1].values


# In[ ]:


print(X)


# In[ ]:


print(Y)


# In[ ]:


Handling missing data


# In[ ]:


from skylearn.impute import SimpleImputer


# In[ ]:


imputer = SimpleImputer(missing_values = np.nan , strategy = 'mean')


# In[ ]:


imputer.fit(X[:, 12:20])


# In[ ]:


X[: ,12:20] =imputer.transform(X[:, 12:20])


# In[ ]:


print(X)


# In[ ]:


ENCODE CATEGORICAL DATA


# In[ ]:


from sklearn.compose import ColumnTransformer


# In[ ]:


from sklearn.preprocessing import OneHotEncoder


# In[ ]:


ct =ColumnTransformer(transformers = [('encoder', OneHotEncoder(),[4])],remainder='passthrough')


# In[ ]:


X = np.array(ct.fit_transform(X))


# In[ ]:


print(x)


# In[ ]:


from sklearn.preprocessing import LabelEncoder


# In[ ]:


le = LabelEncoder()
Y = le.fit_transform(Y)


# In[ ]:


print(Y)


# In[ ]:




