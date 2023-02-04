import pandas as pd
import textextractor as txt
import nltk
import nltk.corpus as corpus
import sklearn
import re
import json

# nltk.download()


data = (txt.extractsample()).lower()

# nltk.word_tokenize( )

tokenized_sentences2 = nltk.sent_tokenize(data)

tokenized_sentences = []
for sentence in tokenized_sentences2:
    sentence = re.sub(r'\W', ' ', sentence)
    sentence = re.sub(r'\s+', ' ', sentence)
    tokenized_sentences.append(re.sub('\n', '', sentence))

for sentence in tokenized_sentences:
    print(sentence)

tokenized_words = nltk.word_tokenize(data)

# print(len(tokenized_words))
# print(tokenized_words)

stop_words = set(corpus.stopwords.words("english"))
punctuations = {',', '.', '(', ')', '\"', '\''}

# print("\n\n", stop_words)
# for sentence in tokenized_sentences:
#     print('\"',sentence,'\"')


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
print(json_object, '\n');
# vocab2=vocab[ : 7]
wordpos = nltk.pos_tag(vocab)
chunked = nltk.ne_chunk(wordpos)
chunked.draw()
print(wordpos)
print(len(vocab))

# Serializing json

# Writing to sample.json
with open("data-text.json", "w") as outfile:
    outfile.write(json_object)

#
# filtered_sentences = [w for w in tokenized_words if (not w in stop_words) and (not w in punctuations)]
#
# print(len(filtered_sentences), "\n\n", filtered_sentences)
#
# wordcount2={}
# for word in filtered_sentences :
#     if word not in wordcount2.keys():
#         wordcount2[word]=1
#     else:
#         wordcount2[word]+=1
#
# print()
# print(wordcount2 ,"\n",len(wordcount2))
