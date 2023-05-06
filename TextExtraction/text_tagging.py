import textgenerator2
import pandas as pd
import nltk
import nltk.corpus as corpus
from nltk import PunktSentenceTokenizer
import sklearn
import re
from utils import anaphora_resolution
import spacy
from spacy import displacy
from spacy import tokens


def print_tags(sentences):
    # sentences = sentences[0:5]
    for sentence in sentences:
        tokenized_words = nltk.word_tokenize(sentence, "english", True)
        # data_tagged=anaphora_resolution.get_tags(tokenized_words)
        # data_tagged=[w for w in data_tagged if not w[1]=='O']
        print(sentence)
        data_tagged = nlp(sentence)
        for ent in data_tagged.ents:
            print(ent.text, '---', ent.label_)
        # print(data_tagged)
        print()

def glossary():
    print(spacy.glossary.explain('GPE'))

nlp = spacy.load('en_core_web_sm')
data = textgenerator2.extractSample()
sentences = nltk.sent_tokenize(data)
print_tags(sentences)