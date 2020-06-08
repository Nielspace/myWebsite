#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


# In[2]:


data = sns.load_dataset('titanic')


# In[3]:


data.head()


# In[4]:


X = data.drop('survived', 1)
y = data.survived


# ## Spliter
# 
# 1. X_train and X_validation
# 2. y_train and y_validation
# 
# **PS:** Don't use transform training and validation datasets together
# 

# In[5]:


X_train, X_val, y_train, y_val = train_test_split(X,y, test_size = 0.2, random_state=23)


# In[6]:


X_train['sex'] = X_train.sex.map({'male':0,
                'female':1})

X_train.embarked = X_train.embarked.map({'S':1,
                                        'C':2,
                                        'Q':3})

X_train['class'] = X_train['class'].map({'First':1,
                                   'Second':2,
                                   'Third':3
                                  })


# In[7]:


drop_columns = ['who', 'adult_male', 'deck', 'embark_town', 'alive', 'alone']

X_train = X_train.drop(drop_columns, 1)


# In[8]:


X_train.head()


# In[9]:


X_train.isna().sum()


# In[10]:


X_train.age.fillna(X_train.age.median(), inplace=True)


# In[11]:


X_train.embarked.fillna(1, inplace=True)


# # Feature Union

# In[12]:


from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


# In[13]:


pca = PCA(n_components=0.95)
skb = SelectKBest(chi2, k=5)
combined_features = FeatureUnion(transformer_list=[("pca", pca), ("skb",skb)],n_jobs=-1)


# In[14]:


data = combined_features.fit_transform(X_train, y_train)


# In[15]:


X_train, y_train = data[:, :-1], data[:,-1]


# In[16]:


X_train.shape


# In[17]:


y_train.shape


# In[18]:


model = RandomForestClassifier(n_jobs=-1, n_estimators=20)


# In[19]:


y_train=y_train.astype('int')


# In[20]:


model.fit(X_train, y_train)


# In[22]:


model.score(X_train, y_train)


# ## Validation Transformation

# In[23]:


X_val['sex'] = X_val.sex.map({'male':0,
                'female':1})

X_val.embarked = X_val.embarked.map({'S':1,
                                        'C':2,
                                        'Q':3})

X_val['class'] = X_val['class'].map({'First':1,
                                   'Second':2,
                                   'Third':3
                                  })

drop_columns = ['who', 'adult_male', 'deck', 'embark_town', 'alive', 'alone']

X_val = X_val.drop(drop_columns, 1)


# In[30]:


X_val.embarked.fillna(1, inplace=True)
X_val.age.fillna(X_val.age.median(), inplace=True)


pca = PCA(n_components=0.95)
skb = SelectKBest(chi2, k=5)
combined_features = FeatureUnion(transformer_list=[("pca", pca), ("skb",skb)],n_jobs=-1)



dataVal = combined_features.fit_transform(X_val, y_val)
X_val, y_val = dataVal[:, :-1], dataVal[:,-1]

y_val=y_val.astype('int')



model.score(X_val, y_val)


# In[32]:


model


# In[ ]:


