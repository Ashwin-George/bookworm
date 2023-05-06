
from sentence_transformers import SentenceTransformer
import json



f = open(r'D:\\pythonpro\\TheNarrator\\raw_data\\data-sentences.json', 'r')
# print(main_words)
sentences = json.loads(f.read())

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
print(embeddings)