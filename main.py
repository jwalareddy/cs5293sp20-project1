import re
import nltk
import numpy
import tempfile
import urllib
import argparse
import sys
from commonregex import CommonRegex
from nltk.corpus import wordnet
def names(data):
    name = ""
    name_list = []
    set_of_words = nltk.word_tokenize(data)
    set_of_taggsets = nltk.pos_tag(set_of_words)
    namedEntity = nltk.ne_chunk(set_of_taggsets, binary = False)
    
    for subtree in namedEntity.subtrees():
        if subtree.label() == 'PERSON':
            label1 = []
            print((subtree.leaves()))
            for leaf in subtree.leaves():
                label1.append(leaf[0])
            name = ' '.join(label1)
            if name not in name_list:
                name_list.append(name)

#    for name in name_list:
#        data = data.replace(name, '\u2588') #failing
    return data, name_list


def dates(data):
    text_parsed = CommonRegex(data)
    list_of_dates = text_parsed.dates

#    for date in list_of_dates:
#        data = data.replace(date, '\u2588')
    return data, list_of_dates

def genders(data):
    list_of_genders=['he','she','him','her','his','hers','male','female','man','woman','men','women']
#    c1 = data.count('\u2588')
#    for gender in list_of_genders:
#        raw_text = r'\b' + gender + r'\b'
#        data = re.sub(raw_text, '\u2588', data, flags = re.IGNORECASE)
#    c2 = data.count('\u2588')
#    gender_count = c2 - c1
    return data, list_of_genders

def concept(data, concept):
    list_of_concepts = []
    count_of_concepts = 0
    list_of_synonymns = wordnet.synsets(concept)
    for synonymn in list_of_synonymns:
        temp = synonymn.lemma_names()
        for element in temp:
            if element not in list_of_concepts:
                list_of_concepts.append(element)

    list_of_sentences = nltk.sent_tokenize(data)
    for sentence in list_of_sentences:
        for c in list_of_concepts:
            if c.lower() in sentence.lower():
                m = len(sentence)
                bl = m * '\u2588'
                data = data.replace(sentence, bl)
                count_of_concepts += 1
    return data, list_of_concepts, count_of_concepts

def redact(names_list, list_of_genders, dates, list_of_concepts, data):
    total = names_list + list_of_genders + dates
    for element in total:
        m = len(element)
        element = r'\b' + element + r'\b'
        bl = m * '\u2588'
        data = re.sub(element, bl, data)

    return data

def stats(names_list, dates, gen_list, gender_count, list_of_concepts, count_of_concepts, stats_list, f):
    status = ''
    total = len(names_list) + count_of_concepts + len(dates) + gender_count
    st = stats_list[0]
    status += ("Status for the file {}\n".format(f))
    status += ("The following number of names are redacted from the file {} \n".format(len(names_list)))
    status += ("The following number of dates are redacted from the file {} \n".format(len(dates)))
    status += ("The following number of genders are redacted from the file {} \n".format(gender_count))
    status += ("The following number of sentences are redacted from the file {} \n".format(count_of_concepts))
    status += ("The total number of redactions in the file are {} \n".format(total))

    if st == 'stdout':
        print(status)

    elif st == 'stderr':
        err = ''
        if len(names_list) == 0:
            err += ("There are no names in the file to be redacted\n")
        if len(dates) == 0:
            err += ("There are no dates in the file to be redacted\n")
        if gender_count == 0:
            err += ("There are no genders in the file to be redacted\n")
        if count_of_concepts == 0:
            err += ("There are no matches for concept in the file to be redacted\n")

        sys.stderr.write(err)

    else:
#        os.system("touch {}".format("stats.txt"))
        file_path = "stats.txt"
        with open(file_path, 'a',encoding="utf-8") as file:
            file.write(status)
            file.close()

    return status
