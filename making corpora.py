import re
from keras.preprocessing.text import Tokenizer
from keras.layers.preprocessing import text_vectorization,preprocessing_test_utils
import textextractor
import nltk.tokenize
data = nltk.tokenize.sent_tokenize(textextractor.extractsample())


# pd.read_csv('amazon_reviews.csv')

def preprocess(text):
    text_input = re.sub('[^a-zA-Z1-9]+', ' ', str(text))
    output = re.sub(r'\d+', '', text_input)
    return output.lower().strip()


# raw_data['review'] = raw_data.review.map(preprocess)
# corpus_cleaned = raw_data.astype(str).values.tolist()
processed_data = [preprocess(w) for w in data]
tokenizer = Tokenizer()
tokenizer.fit_on_texts(processed_data)


# print(processed_data)

input_sequences=[]

for text in processed_data:
    # tokenizer.fit_on_texts(text)

    tokenlist= tokenizer.texts_to_sequences(text)[0]
    print(tokenlist)
    print()
    for i in range(1,len(tokenlist)):
        n_gram_seq=tokenlist[:i+1
                   ]
        input_sequences.append(n_gram_seq)


print(input_sequences)