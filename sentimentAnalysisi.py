# -*- coding: utf-8 -*-
"""allineedislovetonight.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tZwMezKHB9iCXZpsxxarROTRwgmy7wVD
"""

# !pip install transformers sentencepiece

# imported needed lib

from os import truncate
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
import numpy as np
import re
from scipy.special import softmax

# defining the model

MODEL = 'nlptown/bert-base-multilingual-uncased-sentiment'
preprocessor = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

# list of all the manifestos csv file

# 'BJP1984','BJP1989','BJP1991','BJP1996','BJP1999','BJP2009',,'C1999','C2009','C2014','C2019'
manifestos = ['BJP1998','BJP2004','BJP2014']

for manifesto in manifestos:
  # print("=============================")
  try:
    sentences = pd.read_csv('https://raw.githubusercontent.com/vedang-sharma/Political-Analyser/main/data/cleaned_manifestos/'+manifesto+'.csv')

    sentences.columns = ['index', 'sentences']
    results = []

    for i in sentences['sentences']:
      encoded_input = preprocessor.encode(i, return_tensors = 'pt')
      output = model(encoded_input)
      results.append(output[0].detach().numpy())

    res = []

    for i in results:
      res.append(i[0])

    # this csv is with tf-idf values

    df = pd.read_csv('https://raw.githubusercontent.com/vedang-sharma/Political-Analyser/main/category/'+manifesto+'_Data.csv')

    df_2 = pd.DataFrame(res, columns = ['negative', 'semi-negative', 'neutral', 'semi-positive', 'positive'])

    df_2.head()

    # concate the two csv files

    df_final = pd.concat([df, df_2], axis = 1)
    df_final.head()

    df.to_csv('C:/Users/jayes/Desktop/collegeProject/mainefesto/finalCSV/'+manifesto+'_final.csv')
  
  except:
    continue
