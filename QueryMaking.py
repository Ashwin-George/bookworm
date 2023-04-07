import nltk.corpus as corpus
import nltk
import regex as re
import json

query = input('Enter a question : ')

# nltk.word_tokenize( )

database_sentences = re.sub(r'\W', ' ', query)
database_sentences = re.sub(r'\s+', ' ', query)

tokenized_words = nltk.word_tokenize(query)
stop_words = set(corpus.stopwords.words('english'))
main_words = [w for w in tokenized_words if w not in stop_words]
f = open('data-text.json', 'r')

database_word = json.loads(f.read())
f = open('data-sentences.json', 'r')
# print(main_words)

database_sentences = json.loads(f.read())
candidates = {}
for word in main_words:
    if word not in database_word:
        continue

    for sentence_idx in database_sentences:
        # sentence_idx=int(idx)
        if word in database_sentences[sentence_idx].lower():
            if sentence_idx not in candidates:
                candidates[sentence_idx] = 1
            else:
                candidates[sentence_idx] += 1
ans = ""
max_occuring = []
# candidates=[]
maxfreq = 0
if len(candidates) != 1:
    for i in candidates:
        if candidates[i] > maxfreq:
            max_occuring = []
            max_occuring.append(i)
            maxfreq = candidates[i]
        elif candidates[i] == maxfreq:
            max_occuring.append(i)
else:
    max_occuring = candidates
# print(candidates)
for i in max_occuring:
    ans += database_sentences[i]
print(ans)
