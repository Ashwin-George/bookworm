import pandas as pd
import textextractor as txt
import nltk
import nltk.corpus as corpus
import sklearn
import re
import json
from utils import anaphora_resolution
import numpy as np
# nltk.download()


data = (txt.extractsample())
# nltk.word_tokenize( )
tokenized_sentences2 = nltk.sent_tokenize(data)
coreference=anaphora_resolution.parse(tokenized_sentences2)
# print(coreference)
count=0
tokenized_sentences={}
for sentence in tokenized_sentences2:
    sentence = re.sub(r'\W', ' ', sentence)
    sentence = re.sub(r'\s+', ' ', sentence)
    arr=[]
    arr.append(sentence)
    arr.append(coreference[count])
    tokenized_sentences[count]=arr
    count+=1
json_object=json.dumps(tokenized_sentences)
print(json_object)
with open('raw_data/data-sentences_wr.json','w') as outfile:
    outfile.write(json_object)