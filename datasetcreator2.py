import pandas as pd
import textextractor as txt
import nltk
import nltk.corpus as corpus
import sklearn
import re
import json
import numpy as np
# nltk.download()


data = (txt.extractsample())

# nltk.word_tokenize( )

tokenized_sentences2 = nltk.sent_tokenize(data)
count=0
tokenized_sentences={}
for sentence in tokenized_sentences2:
    sentence = re.sub(r'\W', ' ', sentence)
    sentence = re.sub(r'\s+', ' ', sentence)
    tokenized_sentences[count]=sentence
    count+=1
json_object=json.dumps(tokenized_sentences)
print(json_object)
with open('data-sentences.json','w') as outfile:
    outfile.write(json_object)