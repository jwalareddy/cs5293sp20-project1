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

    
    return data, name_list


def dates(data):
    text_parsed = CommonRegex(data)
    list_of_dates = text_parsed.dates

    return data, list_of_dates

def genders(data):
    list_of_genders=['he','she','him','her','his','hers','male','female','man','woman','men','women']
    return data, list_of_genders

#The wordnet.synsets() function from the wordnet package is used to find the synonms of the given word. The synonms of the word are matched with the sentences present within the text file and the sentences matched are redacted with a unicode full block character ('\u2588').
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
        for count in list_of_concepts:
            if count.lower() in sentence.lower():
                length = len(sentence)
                block = length * '\u2588'
                data = data.replace(sentence, block)
                count_of_concepts += 1
    return data, list_of_concepts, count_of_concepts

def redact(names_list, list_of_genders, dates, list_of_concepts, data):
    total = names_list + list_of_genders + dates
    for element in total:
        length = len(element)
        element = r'\b' + element + r'\b'
        block = length * '\u2588'
        data = re.sub(element, block, data)

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
        if count_of_concepts == 0:
            err += ("There are no matches for concept in the file to be redacted\n")

        sys.stderr.write(err)

    else:
        
        file_path = "stats.txt"
        with open(file_path, 'a',encoding="utf-8") as file:
            file.write(status)
            file.close()

    return status


#alternately instead of this, we can write individual functions and then do the  redaction process in that individual function and return the values to the main for depicting the statistics. for redacting genders, we can use TreebankWordDetokenizer to tokenize the text. for dates, we can use the current one only, commonregex for parsing the text.
"""
def redact_names(a):
    names = []
    file1 = []
    data = a
    for i in range(len(data)):
        redacted_data = data[i]
        sentences = nltk.sent_tokenize(redacted_data)
        tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
        tags = [nltk.pos_tag(sentence) for sentence in tokens]
        chunks = nltk.ne_chunk_sents(tags, binary = False)
        for tree in chunks:
            names.extend(extract_names(tree))
        for e in names:
            redacted_data = redacted_data.replace(e,'██')
        file1.append(redacted_data)
    return file1

def redact_genders(file):
    genders=['He', 'She', 'Himself', 'Herself', 'Male', 'Female', 'Him', 'Her', 'His', 'Hisself', 'Man', 'Woman', 'Men', 'Women', 'Husband', 'Wife', 'Gay']
    g_file = []
    concept = file
    for d in range(len(concept)):
            redact_genders = concept_file[d]
            gender_sentences = nltk.sent_tokenize(redact_genders)
            gender_tokens = [nltk.word_tokenize(sentence) for sentence in gender_sentences]
            gender_tokens = nltk.word_tokenize(redact_genders)        
            
            for n, i in enumerate(gender_tokens):
                 for g in range(len(genders)):
                     if i.lower() == genders[g]:
                         gender_tokens[n] = '██'
            gender_tokens = TreebankWordDetokenizer().detokenize(gender_tokens)
            g_file.append(gender_tokens)
    return g_file 
"""
