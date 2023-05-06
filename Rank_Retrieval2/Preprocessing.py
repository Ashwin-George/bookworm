import json
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


ps = PorterStemmer()
f = open('/raw_data-text.json', 'r')
# print(main_words)

database_sentences = json.loads(f.read())
words=list(database_sentences.keys())
words2=[]
for w in words:
    words2.append(ps.stem(lemmatizer.lemmatize(w)))
print(words2)
    # print(w, " : ", ps.stem(w)
# print()
