# Import required libraries
import nltk
import Pronoun_resolution.hobbs as utilhob
# nltk.download('punkt')/
# nltk.download('averaged_perceptron_tagger')

from nltk import pos_tag, word_tokenize, RegexpParser,Tree

# Example text
# sample_text = "The quick brown fox jumps over the lazy dog"

sample_text = "John said he likes dogs"
# Find all parts of speech in above sentence
tagged = pos_tag(word_tokenize(sample_text))

# #Extract all parts of speech from any text
# chunker = RegexpParser("NP: {<DT>?<JJ>*<NN> P: {<IN>},V: {<V.*>},PP: { <p> <NP>},VP: {<V> <NP|PP>*}")
# utilhob.hobbs()

# Extract all parts of speech from any text
chunker = RegexpParser("""
                       NP: {<DT>?<JJ>*<NN>}    #To extract Noun Phrases
                       P: {<IN>}               #To extract Prepositions
                       V: {<V.*>}              #To extract Verbs
                       PP: {<p> <NP>}          #To extract Prepositional Phrases
                       VP: {<V> <NP|PP>*}      #To extract Verb Phrases
                       """)

# Print all parts of speech in above sentence
output = chunker.parse(tagged)
print("After Extracting\n", output)
utilhob.hobbs([output],(1, 1, 1, 0, 0))
# output.draw();
# print(Tree.fromstring(output))from nltk.tokenize import word_tokenize, sent_tokenize
#
# from nltk.tag import StanfordNERTagger
#
#
# st = StanfordNERTagger('/Users/Downloads/stanford-ner-2020-11-17/classifiers/english.all.3class.distsim.crf.ser.gz',
# 					   '/Users/Downloads/stanford-ner-2020-11-17/stanford-ner.jar',
# 					   encoding='utf-8')
#
# text_string='''
# Sir Jagadish Chandra Bose was a scientist of many talents. He was born on 30 November, 1858 in Bikrampur, West Bengal. He was a polymath, physicist, biologist, botanist and archaeologist. Bose pioneered the study of radio and microwave optics. He joined the Presidency College of the University of Calcutta as a professor of physics. There, despite racial discrimination and a lack of funding and equipment, Bose carried on his scientific research. He made important contributions to the study of plants. He has laid the foundation of experimental science in the Indian sub-continent. He was the first person to use semiconductor junctions to detect radio signals. What’s more, he is also probably the father of open technology, as he made his inventions and work freely available for others to further develop and his reluctance for patenting his work is legendary.
# Another of his well known inventions is the crescograph. He measured plant response to various stimuli and hypothesized that plants can feel pain, understand affection etc. At the time when Bose was a student at Cambridge, Prafulla Chandra Roy was a student at Edinburgh. They met in London and became intimate friends.
# While most of us are aware of his scientific prowess, we might not be aware of his talent as an early writer of science fiction! He is in fact considered the father of Bengali science fiction.
# '''
#
# tokenized_text = sent_tokenize(text_string)
# tokenized_tags_list=[]
# new_text_string=''
# anaphora_p_sing=['he','she','his','her','He','She','His','Her']
# anaphora_p_plural=['they','their','They','Their']
# anaphora_l=['this place','that place','the place','there,','there.','This place','That place','The place','There']
#
# person_list_last=[]
# person_list_sentence=[]
# org_list_last=[]
# org_list_sentence=[]
# loc_list_last=[]
# loc_list_sentence=[]
# coreference_list=[]
# coreference_sol=[]
#
#
# flag=0
# flag_org=0
# flag_loc=0
# for i in range(0,len(tokenized_text)):
#     print(tokenized_text[i])
#     tokenized_text1 = word_tokenize(tokenized_text[i])
#     classified_text = st.tag(tokenized_text1)
#     for j in range(0,len(tokenized_text1)):
#
#         a=tokenized_text1[j]
#         b=classified_text[j][1]
#         if b=='PERSON':
#
#             if flag==0:
#                 if classified_text[j][0] in coreference_list:
#
#                     for k in range(0,len(coreference_list)):
#                         if coreference_list[k]==classified_text[j][0]:
#                             if coreference_sol[k] in person_list_sentence:
#                                 pass
#                             else:
#                                 person_list_sentence.append(coreference_sol[k])
#                             break
#
#                 else:
#                     try:
#                         if classified_text[j+1][1]=='PERSON':
#                             flag=1
#                             full_name=classified_text[j][0]+' '
#                         else:
#                             if classified_text[j][0] in person_list_sentence:
#                                 pass
#                             else:
#                                 person_list_sentence.append(classified_text[j][0])
#                     except:
#                         if classified_text[j][0] in person_list_sentence:
#                             pass
#                         else:
#                             person_list_sentence.append(classified_text[j][0])
#             else:
#                 full_name+=classified_text[j][0]+' '
#                 try:
#                     if classified_text[j+1][1]=='PERSON':
#                         flag=1
#
#                     else:
#                         flag=0
#                         full_name=full_name[0:len(full_name)-1]
#                         if full_name in person_list_sentence:
#                             pass
#                         else:
#
#                             person_list_sentence.append(full_name)
#                         if full_name not in coreference_sol:
#                             individual=word_tokenize(full_name)
#                             for k in individual:
#                                 coreference_list.append(k)
#                                 coreference_sol.append(full_name)
#
#                 except:
#                     flag=0
#                     full_name=full_name[0:len(full_name)-1]
#                     person_list_sentence.append(full_name)
#                     individual=word_tokenize(full_name)
#                     for k in individual:
#                         coreference_list.append(k)
#                         coreference_sol.append(full_name)
#         elif b=='ORGANIZATION':
#             if flag_org==0:
#                 if classified_text[j][0] in coreference_list:
#                     for k in range(0,len(coreference_list)):
#                         if coreference_list[k]==classified_text[j][0]:
#                             if coreference_sol[k] in org_list_sentence:
#                                 pass
#                             else:
#                                 org_list_sentence.append(coreference_sol[k])
#                             break
#
#
#                 try:
#                     if classified_text[j+1][1]=='ORGANIZATION':
#                         flag_org=1
#                         full_name=classified_text[j][0]+' '
#                     else:
#                         if classified_text[j][0] in org_list_sentence:
#                             pass
#                         else:
#                             org_list_sentence.append(classified_text[j][0])
#                 except:
#                     if classified_text[j][0] in org_list_sentence:
#                         pass
#                     else:
#                         org_list_sentence.append(classified_text[j][0])
#             else:
#                 full_name+=classified_text[j][0]+' '
#                 try:
#                     if classified_text[j+1][1]=='ORGANIZATION':
#                         flag_org=1
#
#                     else:
#                         flag_org=0
#                         full_name=full_name[0:len(full_name)-1]
#                         if full_name in org_list_sentence:
#                             pass
#                         else:
#
#                             org_list_sentence.append(full_name)
#                         if full_name not in coreference_sol:
#                             individual=word_tokenize(full_name)
#                             for k in individual:
#                                 coreference_list.append(k)
#                                 coreference_sol.append(full_name)
#
#                 except:
#                     flag_org=0
#                     full_name=full_name[0:len(full_name)-1]
#                     org_list_sentence.append(full_name)
#                     individual=word_tokenize(full_name)
#                     for k in individual:
#                         coreference_list.append(k)
#                         coreference_sol.append(full_name)
#         elif b=='LOCATION':
#             if flag_loc==0:
#                 if classified_text[j][0] in coreference_list:
#                     for k in range(0,len(coreference_list)):
#                         if coreference_list[k]==classified_text[j][0]:
#                             if coreference_sol[k] in loc_list_sentence:
#                                 pass
#                             else:
#                                 loc_list_sentence.append(coreference_sol[k])
#                             break
#
#
#                 try:
#                     if classified_text[j+1][1]=='LOCATION':
#                         flag_loc=1
#                         full_name=classified_text[j][0]+' '
#                     else:
#                         if classified_text[j][0] in loc_list_sentence:
#                             pass
#                         else:
#                             loc_list_sentence.append(classified_text[j][0])
#                 except:
#                     if classified_text[j][0] in org_list_sentence:
#                         pass
#                     else:
#                         loc_list_sentence.append(classified_text[j][0])
#             else:
#                 full_name+=classified_text[j][0]+' '
#                 try:
#                     if classified_text[j+1][1]=='LOCATION':
#                         flag_loc=1
#
#                     else:
#                         flag_loc=0
#                         full_name=full_name[0:len(full_name)-1]
#                         if full_name in loc_list_sentence:
#                             pass
#                         else:
#                             loc_list_sentence.append(full_name)
#                         if full_name not in coreference_sol:
#                             individual=word_tokenize(full_name)
#                             for k in individual:
#                                 coreference_list.append(k)
#                                 coreference_sol.append(full_name)
#
#                 except:
#                     flag_loc=0
#                     full_name=full_name[0:len(full_name)-1]
#                     loc_list_sentence.append(full_name)
#                     individual=word_tokenize(full_name)
#                     for k in individual:
#                         coreference_list.append(k)
#                         coreference_sol.append(full_name)
#         else:
#             pass
#         a=[]
#         for l in anaphora_p_sing:
#             if l in tokenized_text1:
#                 if len(person_list_sentence)!=0:
#                     if person_list_sentence[len(person_list_sentence)-1] not in a:
#                         a.append(person_list_sentence[len(person_list_sentence)-1])
#                 else:
#                     try:
#                         a.append(person_list_last[0])
#                         if person_list_last[0] not in person_list_sentence:
#                             person_list_sentence.append(person_list_last[0])
#
#                     except:
#                         pass
#
#         for l in anaphora_p_plural:
#             if l in tokenized_text1:
#                 if len(person_list_sentence)>1:
#                     for m in person_list_sentence:
#                         if m not in a:
#                             a.append(m)
#                 elif len(person_list_sentence)==1:
#                     if person_list_sentence[0] not in a:
#                         a.append(person_list_sentence[0])
#                     try:
#                         for n in person_list_last:
#                             if n not in a:
#                                 a.append(n)
#                                 person_list_sentence.append(n)
#
#                     except:
#                         pass
#                 else:
#                     try:
#                         for n in person_list_last:
#                             if n not in a:
#                                 a.append(n)
#                                 person_list_sentence.append(n)
#                     except:
#                         pass
#
#         for l in anaphora_l:
#             if l in tokenized_text1 and ',' in tokenized_text1:
#                 if len(loc_list_sentence)!=0:
#                     if loc_list_sentence[len(loc_list_sentence)-1] not in a:
#                         a.append(loc_list_sentence[len(loc_list_sentence)-1])
#                 else:
#                     try:
#                         a.append(loc_list_last[0])
#                         if loc_list_last[0] not in loc_list_sentence:
#                             loc_list_sentence.append(loc_list_last[0])
#
#                     except:
#                         pass
#
#                 if len(org_list_sentence)!=0:
#                     if org_list_sentence[len(org_list_sentence)-1] not in a:
#                         a.append(org_list_sentence[len(org_list_sentence)-1])
#                 else:
#                     try:
#                         a.append(org_list_last[0])
#                         if org_list_last[0] not in org_list_sentence:
#                             org_list_sentence.append(org_list_last[0])
#
#                     except:
#                         pass
#
#
#
#
#     person_list_last=person_list_sentence
#     person_list_sentence=[]
#     org_list_last=org_list_sentence
#     org_list_sentence=[]
#     loc_list_last=person_list_sentence
#     loc_list_sentence=[]
#     print('Anaphora resolved:')
#     print(a)
#     print('\n')