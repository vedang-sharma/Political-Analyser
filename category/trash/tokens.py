import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer

string = []

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# removed stop words and lemmatized each words
with open("C:/Users/jayes/Desktop/collegeProject/mainefesto/temp/infrastructure.txt",'r',encoding='utf8') as temp:
    for i in temp:
        line = i[:-1]
        lol = ""
        for word in line.split(" "):
	        if not word in stop_words:
                 lol += lemmatizer.lemmatize(word)+" "
        string.append(lol)

# write the new string on to a file
with open("C:/Users/jayes/Desktop/collegeProject/mainefesto/temp/infratemp.txt",'w') as temp:
    for i in string:
        temp.write(i+"\n")