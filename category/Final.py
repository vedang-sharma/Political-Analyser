#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import pandas as pd


# In[2]:


#Reading the data of Manifesto
with open('C:/Users/jayes/Desktop/collegeProject/mainefesto/extracted/C2019.xml', encoding = 'utf-8') as file_obj:
    df = pd.DataFrame(file_obj.readlines(), columns = ['sentences'])


# In[3]:


# In[4]:


df.reset_index(drop = True)
df.head(2)


# In[5]:


#Lemmatization
corpus = np.array([])

lemmatizer = WordNetLemmatizer()

print(len(df))
for i in range(len(df['sentences'])):
    try:
        review = re.sub('[^a-zA-Z]', ' ', df['sentences'][i+1])
        review = review.lower()
        review = review.split()
        review = [lemmatizer.lemmatize(word) for word in review if word not in set(stopwords.words('English'))] #Lemmatization of each word is done here

        corpus = np.append(corpus, ' '.join(review))
    except:
        continue


# In[6]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[7]:


#Creating the model and storing the values as a Data Frame
model = TfidfVectorizer()
X = model.fit_transform(corpus)

#Converting the 'X' into a Dataframe
data = pd.DataFrame(X.toarray(), columns = [model.get_feature_names_out()])
data.head(2)


# In[21]:


#Creating numpy array for keywords
tokens = []
names = ['Education', 'Infrastructure', 'Agriculture', 'Health', 'Economics']

for i in range(5):
    name = 'C:/Users/jayes/Desktop/collegeProject/mainefesto/extracted/'+names[i]+'.txt'
    with open(name, 'r', encoding = 'utf-8') as file_obj:
        text = file_obj.readlines()
        words = []
        #Removing the '\n' and appending the new keywords to the new numpy array
        for j in text: words.append(re.sub('\\n', '', j))
        words = np.array(words)
        tokens.append(words)
        
tokens = np.array(tokens, dtype = np.ndarray)


# In[31]:


#Lemmatizing the keywords for easier matching
for i in range(len(tokens)):
    for j in range(len(tokens[i])):
        tokens[i][j] = re.sub('[^a-zA-Z]', ' ', tokens[i][j]) #Removing unnecessary characters from the word
        tokens[i][j] = lemmatizer.lemmatize(tokens[i][j].lower())


# In[44]:


finale = [] #List to store all the TF - IDF values of a sentence

for i in range(len(corpus)):
    
    #TF - IDF values are stored for each sentence here
    val = [-1, [0], [0], [0], [0], [0]]
    
    for word in corpus[i].split():
        if word in set(tokens[0]): val[1].append(data[word].iloc[i][0])
        if word in set(tokens[1]): val[2].append(data[word].iloc[i][0])
        if word in set(tokens[2]): val[3].append(data[word].iloc[i][0])
        if word in set(tokens[3]): val[4].append(data[word].iloc[i][0])
        if word in set(tokens[4]): val[5].append(data[word].iloc[i][0])
    
    val[0] = i
    
    for i in range(1, 6):
        if sum(val[i]): val[i] = sum(val[i])/len(val[i])
        else: val[i] = 0
            
    finale.append(val)


# In[55]:


names = ['sno', 'edu', 'infra', 'agri', 'hea', 'eco']
finale = pd.DataFrame(finale, columns = names)

finale.to_csv('C:/Users/jayes/Desktop/collegeProject/mainefesto/extracted/C2019_Data.csv', index = False)