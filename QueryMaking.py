import nltk.corpus as corpus
import nltk
import regex as re
import json
query=input('Enter a question : ')

# nltk.word_tokenize( )

sentence = re.sub(r'\W', ' ', query)
sentence = re.sub(r'\s+', ' ', query)

tokenized_words = nltk.word_tokenize(query)
stop_words=set(corpus.stopwords.words('english'))
main_words=[w for w in tokenized_words if w not in stop_words]
f=open('data-text.json','r')

database_word=json.loads(f.read())
f=open('data-sentences.json','r')
print(main_words)

database_sentences=json.loads(f.read())
candidates={}
for word in main_words :
    sentences=database_word[word]
    for no in sentences :
        if  no not in candidates :
            candidates[no]=1
        else:
            candidates[no]+=1

print(candidates)
