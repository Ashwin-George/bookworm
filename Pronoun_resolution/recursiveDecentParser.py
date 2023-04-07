# import nltk
#
# grammar = nltk.CFG.fromstring("""
#     S -> NP VP
#     NP -> PRP | N
#     VP -> V | V NP
#     PRP -> 'he'
#     N -> 'John' | 'dogs'
#     V -> 'said' | 'likes'
# """)
#
# rd_parser = nltk.RecursiveDescentParser(grammar)
#
# sentence = "John said he likes dogs"
# tokens = sentence.split()
#
# parsed = False
# for tree in rd_parser.parse(tokens):
#     print(tree)
#     parsed = True
#
# if not parsed:
#     print("Unable to parse sentence:", sentence)
import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> PRP | N
    VP -> V | V NP
    PRP -> 'he'
    N -> 'John' | 'dogs'
    V -> 'said' | 'likes'
""")

sr_parser = nltk.ShiftReduceParser(grammar)

sentence = "John said he likes dogs"
tokens = sentence.split()

parsed = False
for tree in sr_parser.parse(tokens):
    print(tree)
    parsed = True

if not parsed:
    print("Unable to parse sentence:", sentence)
