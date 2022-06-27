import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer

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

# write the new string on to a file
# with open("C:/Users/jayes/Desktop/collegeProject/mainefesto/temp/LemBJP1984.xml",'w') as temp:
#     for i in string:
#         temp.write(i+"\n")

dic = {}

# create object
tfidf = TfidfVectorizer()

# get tf-df values
result = tfidf.fit_transform(string)

print((list(result.data[:10])))

for ele1, ele2 in zip(tfidf.get_feature_names(), tfidf.idf_):
    dic[ele1] = ele2

print(len(dic))

# eco = open("C:/Users/jayes/Desktop/collegeProject/mainefesto/temp/ecotemp.txt",'r')
# econo = []
# agri = open("C:/Users/jayes/Desktop/collegeProject/mainefesto/temp/agrotemp.txt",'r')
# agro = []
# educ = open("C:/Users/jayes/Desktop/collegeProject/mainefesto/temp/edutemp.txt",'r')
# edu = []
# health = open("C:/Users/jayes/Desktop/collegeProject/mainefesto/temp/healthtemp.txt",'r')
# hea = []
# infra = open("C:/Users/jayes/Desktop/collegeProject/mainefesto/temp/infratemp.txt",'r')
# infr = []

# for index in range(len(string)):
#     for e in eco:
#         temp = e[:-1].split()
#         for i in temp:
#             if i in string[index]:
#                 try:
#                     econo.append(dic[i])
#                 except:
#                     pass
    
#     for a in agri:
#         temp = a[:-1].split()
#         for i in temp:
#             if i in string[index]:
#                 try:
#                     agro.append(dic[i])
#                 except:
#                     pass
    
#     for e in educ:
#         temp = e[:-1].split()
#         for i in temp:
#             if i in string[index]:
#                 try:
#                     edu.append(dic[i])
#                 except:
#                     pass
    
#     for h in health:
#         temp = h[:-1].split()
#         for i in temp:
#             if i in string[index]:
#                 try:
#                     hea.append(dic[i])
#                 except:
#                     pass
    
#     for inf in infra:
#         temp = inf[:-1].split()
#         for i in temp:
#             if i in string[index]:
#                 try:
#                     infr.append(dic[i])
#                 except:
#                     pass
    
#     aaaa = sum(agro)/len(agro) if len(agro) != 0 else 0
#     eeee = sum(econo)/len(econo) if len(econo) != 0 else 0
#     eduu = sum(edu)/len(edu) if len(edu) != 0 else 0
#     heaa = sum(hea)/len(hea) if len(hea) != 0 else 0
#     infr = sum(infr)/len(infr) if len(infr) != 0 else 0

#     print(string[index],",",aaaa,",",eeee,",",eduu,",",heaa,",",infr)
#     econo = []
#     agro = []
#     edu = []
#     hea = []
#     infr = []

# print(econo,":",sum(econo)/len(econo))
# print(agro,":",sum(agro)/len(agro))
# print(edu,":",sum(edu)/len(edu))
# print(hea,":",sum(hea)/len(hea))
# print(infr,":",sum(infr)/len(infr))