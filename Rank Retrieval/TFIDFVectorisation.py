from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
import nltk
import nltk.corpus as cps
import pandas as pd

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


ps = PorterStemmer()

def sliming(corpus):
    data=[]
    stop_words = set(cps.stopwords.words("english"))
    # print(stop_words)
    for sentence in corpus :
        new_sen=""
        tokenized=nltk.word_tokenize(sentence.lower())
        filteredsentence=[w for w in tokenized if ( not w in stop_words)]
        for w in filteredsentence  :
             new_sen=new_sen+" "+ps.stem(
                 w
                 # lemmatizer.lemmatize(w)
             )
        data.append(new_sen)
    # print(data)
    return data




f = open('D:\pythonpro\TheNarrator\data-sentences.json', 'r')
# print(main_words)

database_sentences = json.loads(f.read())
corpus1=list(database_sentences.values())
corpus=sliming(corpus1)
# print(sentences)
tr_idf_model  = TfidfVectorizer()
tf_idf_vector = tr_idf_model.fit_transform(corpus)
print(type(tf_idf_vector), tf_idf_vector.shape)
tf_idf_array = tf_idf_vector.toarray()

for i in tf_idf_array:
    print(i," ",len(i))

# print(tf_idf_array)

words_set = tr_idf_model.get_feature_names_out()

print(words_set)
df_tf_idf = pd.DataFrame(tf_idf_array, columns = words_set)

print(df_tf_idf)

dummy_queries=["who is sniffer","What are scientists been using since 199","who has obsessive, high energy personalities"]

# for query in dummy_queries:
new_vec=tr_idf_model.transform(dummy_queries)
print(new_vec.toarray())
similarity_scores = cosine_similarity(new_vec, tf_idf_vector)
# print(np.array(similarity_scores))
for arr in similarity_scores:
    maxs=np.argmax(arr)
    print(corpus[maxs])

# for i in similarity_scores:
#     print("Document {} has a similarity score of {:.4f}".format(i + 1, similarity_scores[0][i]))

# tr_idf_model.transform()