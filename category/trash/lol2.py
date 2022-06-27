import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer
import pandas as pd
import csv  

string = []

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# removed stop words and lemmatized each words
with open("C:/Users/jayes/Desktop/collegeProject/mainefesto/temp/NDA2004.xml",'r',encoding='utf8') as temp:
    for i in temp:
        line = i[:-1]
        lol = ""
        for word in line.split(" "):
	        if not word in stop_words:
                 lol += lemmatizer.lemmatize(word)+" "
        string.append(lol)


tfidf = TfidfVectorizer()

# get tf-df values
result = tfidf.fit_transform(string)

df = pd.DataFrame(result.toarray(),columns=tfidf.get_feature_names_out())

eco = open("C:/Users/jayes/Desktop/collegeProject/mainefesto/temp/ecotemp.txt",'r')
econo = []
agri = open("C:/Users/jayes/Desktop/collegeProject/mainefesto/temp/agrotemp.txt",'r')
agro = []
educ = open("C:/Users/jayes/Desktop/collegeProject/mainefesto/temp/edutemp.txt",'r')
edu = []
health = open("C:/Users/jayes/Desktop/collegeProject/mainefesto/temp/healthtemp.txt",'r')
hea = []
infra = open("C:/Users/jayes/Desktop/collegeProject/mainefesto/temp/infratemp.txt",'r')
infr = []

for index in range(len(string)):
    for e in eco:
        temp = e[:-1].split()
        for i in temp:
            if i in string[index]:
                try:
                    econo.append(df[i][index])
                except:
                    pass
    
    for a in agri:
        temp = a[:-1].split()
        for i in temp:
            if i in string[index]:
                try:
                    agro.append(df[i][index])
                except:
                    pass
    
    for e in educ:
        temp = e[:-1].split()
        for i in temp:
            if i in string[index]:
                try:
                    edu.append(df[i][index])
                except:
                    pass
    
    for h in health:
        temp = h[:-1].split()
        for i in temp:
            if i in string[index]:
                try:
                    hea.append(df[i][index])
                except:
                    pass
    
    for inf in infra:
        temp = inf[:-1].split()
        for i in temp:
            if i in string[index]:
                try:
                    infr.append(df[i][index])
                except:
                    pass
    
    aaaa = sum(agro)/len(agro) if len(agro) != 0 else 0
    eeee = sum(econo)/len(econo) if len(econo) != 0 else 0
    eduu = sum(edu)/len(edu) if len(edu) != 0 else 0
    heaa = sum(hea)/len(hea) if len(hea) != 0 else 0
    infr = sum(infr)/len(infr) if len(infr) != 0 else 0

    # with open("C:/Users/jayes/Desktop/collegeProject/mainefesto/temp/csvFile.csv",'a') as csvFile:
    #     writer = csv.writer(csvFile)
    #     writer.writerow(datadb)
    
    res = string[index]+","+str(aaaa)+","+str(eeee)+","+str(eduu)+","+str(heaa)+","+str(infr)
    print(res)
    econo = []
    agro = []
    edu = []
    hea = []
    infr = []