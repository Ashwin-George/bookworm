import textextractor as txt
import nltk
import nltk.corpus as corpus
import re


data = (txt.extractsample()).lower()

# nltk.word_tokenize( )
tokenized_sentences = nltk.sent_tokenize(data)
tokenized_sentences2=[]
for sentence in tokenized_sentences:
    tokenized_sentences2.append(re.sub('\n','',sentence))

tokenized_sentence=tokenized_sentences2
for sentence in tokenized_sentences2:
    print( sentence )

stop_words = set(corpus.stopwords.words("english"))
punctuations = {',', '.', '(', ')', '\"', '\''}
# print(stop_words)

# print(tokenized_sentences[1])
# print(tokenized_sentences2[1])