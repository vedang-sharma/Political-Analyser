import re
import numpy as np
import nltk
from pdfminer.high_level import extract_text

#Extracting text data from the .pdf file to pdminer object
text = extract_text("C:/Users/jayes/Desktop/collegeProject/mainefesto/NDA2004.pdf")

clean_text = re.sub('\n', ' ', text)
header = '\d{4}.\w*.{2}\w* • \d*|\d{2} • \d{4} \w*.{2}\w*'


page_nums = np.arange(1, 71)

for i in page_nums:
    clean_text_2 = re.sub(header, ' ', clean_text)

clean_text_3 = re.sub('\s{2,}', ' ', clean_text_2)

footer = 'Untitled\S*.\S*.\S*.\S*.PM'

clean_text_4 = re.sub(footer, ' ', clean_text_3)

clean_text_5 = re.sub('\s\d{1,2}\.\s', ' ', clean_text_4)

ct = re.sub('Rs\.', '₹', clean_text_5)

sentences = nltk.sent_tokenize(ct)

with open('C:/Users/jayes/Desktop/collegeProject/mainefesto/extracted/NDA2004.xml', 'w+', encoding = 'utf-8', errors = 'ignore') as file_obj:
    for i in sentences:
        file_obj.write('\n')
        file_obj.write(i)