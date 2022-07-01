#!/usr/bin/env python
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# In[2]:


#Creating numpy array for keywords
edu = np.array([])

with open('Education.txt', 'r', encoding = 'utf-8') as file_obj:
    words = file_obj.readlines()
    
    for i in str(words).split(): #Removing the '\n' and appending the new keywords to the new numpy array
        edu = np.append(edu, i)


# In[3]:


import pandas as pd


# In[4]:


#Reading the data of Manifesto
with open('2004.xml', encoding = 'utf-8') as file_obj:
    df = pd.DataFrame(file_obj.readlines(), columns = ['sentences'])


# In[5]:


df.drop(df.index[[0, 918]], inplace = True) #Don't do this, this was my mistake


# In[6]:


df.reset_index(drop = True)
df.head()


# In[7]:


import re


# In[8]:


#Lemmatization
corpus = np.array([])

lemmatizer = WordNetLemmatizer()

for i in range(len(df['sentences'])):
    review = re.sub('[^a-zA-Z]', ' ', df['sentences'][i+1])
    review = review.lower()
    review = review.split()
    review = [lemmatizer.lemmatize(word) for word in review if word not in set(stopwords.words('English'))] #Lemmatization of each word is done here
    
    corpus = np.append(corpus, ' '.join(review))


# In[9]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[10]:


#Creating the model and storing the values as a Data Frame
model = TfidfVectorizer()
X = model.fit_transform(corpus)

data = pd.DataFrame(X.toarray(), columns = [model.get_feature_names_out()]) #Converting the 'X' into a Dataframe
data.head()


# In[11]:


#Lemmatizing the keywords for easier matching
e = []
for i in range(len(edu)):
    edu[i] = re.sub('[^a-zA-Z]', ' ', edu[i]) #Removing unnecessary characters from the word
    edu[i] = lemmatizer.lemmatize(edu[i].lower())
    
edu 


# In[31]:


finale = [] #List to store all the TF - IDF values of a sentence

for i in range(len(corpus)):
    val = [] #TF - IDF values are stored for each sentence here
    
    for word in corpus[i].split():
        if word in set(edu):
            val.append(data[word].iloc[i][0])
        
    if len(val):
        finale.append([sum(val)/len(val), i])
        
finale


# In[37]:


edu_df = pd.DataFrame(finale, columns = ['val', 'sno'])
edu_df.to_csv('2004_education.csv')

