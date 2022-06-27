import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

# word_tokenize accepts
# a string as an input, not a file.
stop_words = set(stopwords.words('english'))
file1 = open("C:/Users/jayes/Desktop/collegeProject/mainefesto/temp/BJP1984.xml")

# Use this to read file content as a stream:
line = file1.read()
words = line.split()
for r in words:
	if not r in stop_words:
		appendFile = open('C:/Users/jayes/Desktop/collegeProject/mainefesto/temp/Fil_BJP1984.xml','a')
		appendFile.write(" "+r)
		appendFile.close()
        
# ch1 = "agriculture"
# ch2 = "economy"
# ch3 = "education"
# ch4 = "health"
# ch5 = "infrastructure"
# temp += " "+ch1 +" "+ ch2 +" "+ ch3 +" "+ ch4 +" "+ ch5

# # print(temp)

# string = temp.split()

# # create object
# tfidf = TfidfVectorizer()

# # get tf-df values
# result = tfidf.fit_transform(string)

# # get idf values
# print('\nidf values:')
# for ele1, ele2 in zip(tfidf.get_feature_names(), tfidf.idf_):
# 	if ele1 == ch1 or ele1 == ch2 or ele1 == ch3 or ele1 == ch4 or ele1 == ch5:
# 		print(ele1, ':', ele2)
