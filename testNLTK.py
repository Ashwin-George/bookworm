import textextractor as txt
import nltk
import nltk.corpus as corpus
import re


data = (txt.extractsample()).lower()

# nltk.word_tokenize( )nl

stop_words = set(corpus.stopwords.words("english"))
punctuations = {',', '.', '(', ')', '\"', '\''}
# print(stop_words)

# print(tokenized_sentences[1])
# print(tokenized_sentences2[1])