import os

from nltk.tokenize import word_tokenize, sent_tokenize

from nltk.tag import StanfordNERTagger

arr = []
java_path = r"C:\Program Files\Java\jdk-11.0.11\bin\java.exe"
os.environ['JAVAHOME'] = java_path
st = StanfordNERTagger(
        r"C:\Users\ashwi\Downloads\stanford-ner-4.2.0\stanford-ner-2020-11-17\classifiers\english.all.3class.distsim.crf.ser\english.all.3class.distsim.crf.ser",
        r"C:\Users\ashwi\Downloads\stanford-ner-4.2.0\stanford-ner-2020-11-17\stanford-ner.jar",
        encoding='utf-8')

def get_tags(tokenized_words):
    # words=word_tokenize(tokenized_words)
    return st.tag(tokenized_words)

def parse(tokenized_text):
    # arr = []
    # java_path = r"C:\Program Files\Java\jdk-11.0.11\bin\java.exe"
    # os.environ['JAVAHOME'] = java_path

    # st = StanfordNERTagger(
    #     r"C:\Users\ashwi\Downloads\stanford-ner-4.2.0\stanford-ner-2020-11-17\classifiers\english.all.3class.distsim.crf.ser\english.all.3class.distsim.crf.ser",
    #     r"C:\Users\ashwi\Downloads\stanford-ner-4.2.0\stanford-ner-2020-11-17\stanford-ner.jar",
    #     encoding='utf-8')

    # tokenized_text = sent_tokenize(textString)
    tokenized_tags_list = []
    new_text_string = ''
    anaphora_p_sing = ['he', 'she', 'his', 'her', 'He', 'She', 'His', 'Her']
    anaphora_p_plural = ['they', 'their', 'They', 'Their']
    anaphora_l = ['this place', 'that place', 'the place', 'there,', 'there.', 'This place', 'That place', 'The place',
                  'There']

    person_list_last = []
    person_list_sentence = []
    org_list_last = []
    org_list_sentence = []
    loc_list_last = []
    loc_list_sentence = []
    coreference_list = []
    coreference_sol = []

    flag = 0
    flag_org = 0
    flag_loc = 0
    for i in range(0, len(tokenized_text)):
        # print(tokenized_text[i])
        tokenized_text1 = word_tokenize(tokenized_text[i])
        classified_text = st.tag(tokenized_text1)
        for j in range(0, len(tokenized_text1)):

            a = tokenized_text1[j]
            b = classified_text[j][1]
            if b == 'PERSON':

                if flag == 0:
                    if classified_text[j][0] in coreference_list:

                        for k in range(0, len(coreference_list)):
                            if coreference_list[k] == classified_text[j][0]:
                                if coreference_sol[k] in person_list_sentence:
                                    pass
                                else:
                                    person_list_sentence.append(coreference_sol[k])
                                break

                    else:
                        try:
                            if classified_text[j + 1][1] == 'PERSON':
                                flag = 1
                                full_name = classified_text[j][0] + ' '
                            else:
                                if classified_text[j][0] in person_list_sentence:
                                    pass
                                else:
                                    person_list_sentence.append(classified_text[j][0])
                        except:
                            if classified_text[j][0] in person_list_sentence:
                                pass
                            else:
                                person_list_sentence.append(classified_text[j][0])
                else:
                    full_name += classified_text[j][0] + ' '
                    try:
                        if classified_text[j + 1][1] == 'PERSON':
                            flag = 1

                        else:
                            flag = 0
                            full_name = full_name[0:len(full_name) - 1]
                            if full_name in person_list_sentence:
                                pass
                            else:

                                person_list_sentence.append(full_name)
                            if full_name not in coreference_sol:
                                individual = word_tokenize(full_name)
                                for k in individual:
                                    coreference_list.append(k)
                                    coreference_sol.append(full_name)

                    except:
                        flag = 0
                        full_name = full_name[0:len(full_name) - 1]
                        person_list_sentence.append(full_name)
                        individual = word_tokenize(full_name)
                        for k in individual:
                            coreference_list.append(k)
                            coreference_sol.append(full_name)
            elif b == 'ORGANIZATION':
                if flag_org == 0:
                    if classified_text[j][0] in coreference_list:
                        for k in range(0, len(coreference_list)):
                            if coreference_list[k] == classified_text[j][0]:
                                if coreference_sol[k] in org_list_sentence:
                                    pass
                                else:
                                    org_list_sentence.append(coreference_sol[k])
                                break

                    try:
                        if classified_text[j + 1][1] == 'ORGANIZATION':
                            flag_org = 1
                            full_name = classified_text[j][0] + ' '
                        else:
                            if classified_text[j][0] in org_list_sentence:
                                pass
                            else:
                                org_list_sentence.append(classified_text[j][0])
                    except:
                        if classified_text[j][0] in org_list_sentence:
                            pass
                        else:
                            org_list_sentence.append(classified_text[j][0])
                else:
                    full_name += classified_text[j][0] + ' '
                    try:
                        if classified_text[j + 1][1] == 'ORGANIZATION':
                            flag_org = 1

                        else:
                            flag_org = 0
                            full_name = full_name[0:len(full_name) - 1]
                            if full_name in org_list_sentence:
                                pass
                            else:

                                org_list_sentence.append(full_name)
                            if full_name not in coreference_sol:
                                individual = word_tokenize(full_name)
                                for k in individual:
                                    coreference_list.append(k)
                                    coreference_sol.append(full_name)

                    except:
                        flag_org = 0
                        full_name = full_name[0:len(full_name) - 1]
                        org_list_sentence.append(full_name)
                        individual = word_tokenize(full_name)
                        for k in individual:
                            coreference_list.append(k)
                            coreference_sol.append(full_name)
            elif b == 'LOCATION':
                if flag_loc == 0:
                    if classified_text[j][0] in coreference_list:
                        for k in range(0, len(coreference_list)):
                            if coreference_list[k] == classified_text[j][0]:
                                if coreference_sol[k] in loc_list_sentence:
                                    pass
                                else:
                                    loc_list_sentence.append(coreference_sol[k])
                                break

                    try:
                        if classified_text[j + 1][1] == 'LOCATION':
                            flag_loc = 1
                            full_name = classified_text[j][0] + ' '
                        else:
                            if classified_text[j][0] in loc_list_sentence:
                                pass
                            else:
                                loc_list_sentence.append(classified_text[j][0])
                    except:
                        if classified_text[j][0] in org_list_sentence:
                            pass
                        else:
                            loc_list_sentence.append(classified_text[j][0])
                else:
                    full_name += classified_text[j][0] + ' '
                    try:
                        if classified_text[j + 1][1] == 'LOCATION':
                            flag_loc = 1

                        else:
                            flag_loc = 0
                            full_name = full_name[0:len(full_name) - 1]
                            if full_name in loc_list_sentence:
                                pass
                            else:
                                loc_list_sentence.append(full_name)
                            if full_name not in coreference_sol:
                                individual = word_tokenize(full_name)
                                for k in individual:
                                    coreference_list.append(k)
                                    coreference_sol.append(full_name)

                    except:
                        flag_loc = 0
                        full_name = full_name[0:len(full_name) - 1]
                        loc_list_sentence.append(full_name)
                        individual = word_tokenize(full_name)
                        for k in individual:
                            coreference_list.append(k)
                            coreference_sol.append(full_name)
            else:
                pass
            a = []
            for l in anaphora_p_sing:
                if l in tokenized_text1:
                    if len(person_list_sentence) != 0:
                        if person_list_sentence[len(person_list_sentence) - 1] not in a:
                            a.append(person_list_sentence[len(person_list_sentence) - 1])
                    else:
                        try:
                            a.append(person_list_last[0])
                            if person_list_last[0] not in person_list_sentence:
                                person_list_sentence.append(person_list_last[0])

                        except:
                            pass

            for l in anaphora_p_plural:
                if l in tokenized_text1:
                    if len(person_list_sentence) > 1:
                        for m in person_list_sentence:
                            if m not in a:
                                a.append(m)
                    elif len(person_list_sentence) == 1:
                        if person_list_sentence[0] not in a:
                            a.append(person_list_sentence[0])
                        try:
                            for n in person_list_last:
                                if n not in a:
                                    a.append(n)
                                    person_list_sentence.append(n)

                        except:
                            pass
                    else:
                        try:
                            for n in person_list_last:
                                if n not in a:
                                    a.append(n)
                                    person_list_sentence.append(n)
                        except:
                            pass

            for l in anaphora_l:
                if l in tokenized_text1 and ',' in tokenized_text1:
                    if len(loc_list_sentence) != 0:
                        if loc_list_sentence[len(loc_list_sentence) - 1] not in a:
                            a.append(loc_list_sentence[len(loc_list_sentence) - 1])
                    else:
                        try:
                            a.append(loc_list_last[0])
                            if loc_list_last[0] not in loc_list_sentence:
                                loc_list_sentence.append(loc_list_last[0])

                        except:
                            pass

                    if len(org_list_sentence) != 0:
                        if org_list_sentence[len(org_list_sentence) - 1] not in a:
                            a.append(org_list_sentence[len(org_list_sentence) - 1])
                    else:
                        try:
                            a.append(org_list_last[0])
                            if org_list_last[0] not in org_list_sentence:
                                org_list_sentence.append(org_list_last[0])

                        except:
                            pass

        person_list_last = person_list_sentence
        person_list_sentence = []
        org_list_last = org_list_sentence
        org_list_sentence = []
        loc_list_last = person_list_sentence
        loc_list_sentence = []
        arr.append(a)
        # print('Anaphora resolved:')
        # print(a)
        # print('\n')
    return arr
# print(a)
