import pandas as pd
import textextractor as txt
import nltk
import nltk.corpus as corpus
from  nltk import PunktSentenceTokenizer
import sklearn
import re
from utils import anaphora_resolution
from TextExtraction import textgenerator2

import json
# nltk.download()

train_text=corpus.state_union.raw("2005-GWBush.txt")
data = (txt.extractsample()).lower()
custom_sent_tokenizer=PunktSentenceTokenizer(train_text)
# nltk.word_tokenize( )

tokenized_sentences2 = nltk.sent_tokenize(data)
tokenized_sentences = []
for sentence in tokenized_sentences2:
    sentence = re.sub(r'\W', ' ', sentence)
    sentence = re.sub(r'\s+', ' ', sentence)
    tokenized_sentences.append(re.sub('\n', '', sentence))

# for sentence in tokenized_sentences:
#     print(sentence)

tokenized_words = nltk.word_tokenize(data)
data2=textgenerator2.extractSample()
data2=data2.lower()
tokenized_words2 = nltk.word_tokenize(data2)
tagged_words=anaphora_resolution.get_tags(tokenized_words2)

tagged_words=[w for w in tagged_words if not w[1]=='O']
print(tagged_words)
stop_words = set(corpus.stopwords.words("english"))
punctuations = {',', '.', '(', ')', '\"', '\''}



print()

vocab = {}
count = -1
for sentence in tokenized_sentences:
    count += 1
    for word in nltk.word_tokenize(sentence):
        if word in stop_words:
            continue
        else:
            if word not in vocab.keys():
                idx = []
                idx.append(count)
                vocab[word] = idx
            else:
                vocab[word].append(count)

json_object = json.dumps(vocab)
# print(json_object, '\n');
# vocab2=vocab[ : 7]
# wordpos = nltk.pos_tag(vocab)
# chunked = nltk.ne_chunk(wordpos)
# chunked.draw()
# print(wordpos)
print(len(vocab))

# Serializing json

# with open("raw_data/data-text.json", "w") as outfile:
#     outfile.write(json_object)

