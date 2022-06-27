#!/usr/bin/env python
# coding: utf-8

# In[1]:


education = []

with open('Education.txt', 'r') as file_obj:
    education = file_obj.readlines()


# In[2]:


edu = [] #Removing '\n'
for i in education:
    edu.append(i[0: -1])
    
edu.append('education')
edu[0: 5]


# In[3]:


import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# In[4]:


lemmatizer = WordNetLemmatizer()

c = []

with open('2004.xml', 'r', encoding = 'UTF-8') as file_obj: #UTF-8 zaroori hai warna wo ajeeb character jayenge
    c = file_obj.readlines()


# In[5]:


corpus = []
for i in c:
    corpus.append(i[0: -1])


# In[8]:


import pandas as pd
df = pd.DataFrame(corpus)


# In[9]:


df.columns = ['text']
df.head()


# In[10]:


import re


# In[11]:


corpus = []


# In[12]:


for i in range(len(df['text'])):
    review = re.sub('[^a-zA-Z]', ' ', df['text'][i])
    review = review.lower()
    review = review.split()
    
    review = [lemmatizer.lemmatize(word) for word in review if word not in set(stopwords.words('English'))]
    corpus.append(' '.join(review))


# In[13]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[14]:


model = TfidfVectorizer()
X = model.fit_transform(corpus)


# In[68]:


print(corpus[0])
print(X[0, 743])

