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
    set_of_words = nltk.word_tokenize(data)
    set_of_taggsets = nltk.pos_tag(set_of_words)
    namedEntity = nltk.ne_chunk(set_of_taggsets)
    name = ""
    names_list = []
    person = []
    for subtree in namedEntity.subtrees(filter=lambda t: t.label()=='PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1:
            for part in person:
                name +=part + ' '
            if name[:-1] not in names_list:
                names_list.append(name[:-1])
            name=''
        else:
            names_list.append(person[0])
        person=[]
    return (names_list)

def dates(data):
    text_parsed = CommonRegex(data)
    list_of_dates = text_parsed.dates
    #alternately, if i use regular expression, to find dates.
    #list1 = re.findall(r'\d {1,4}.\d{1,2}.\d{1,4}|\d{1,2}?[ \t.-]*[A-Za-z]+[ \t.-]* \d{1,4}|\w{3,9}[ \t.-]*\d{1,2}[ \t.-]*\d{1,4}|\w{3,9}[ \t.-]*\d{1,4}', text)
    #return(list1)
    return data, list_of_dates
def genders(data):
    #alternately, i can use a regular expression to find the genders redaction.
    """
    pattern = r' [hH]e | [Ss]he | [Hh]is | [Hh]er | [Hh]im | [Hh]imself | [Hh]erself | [Hh]ers | [sS]on | [Dd]addy| mom| dad| brother| sister| mommy | man| men| wom[ae]n'
    list3 = re.findall(pattern,text)
    return list3
    """
    list_of_genders=['he', 'she', 'himself', 'herself', 'male', 'female', 'him', 'her', 'his', 'man', 'woman', 'men', 'women', 'husband', 'wife']
    return data, list_of_genders
#The wordnet.synsets() function from the wordnet package is used to find the synonms of the given word. The synonms of the word are matched with the sentences present within the tex
#t file and the sentences matched are redacted with a unicode full block character ('\u2588').
def concept(data, concept):
    sentences = nltk.sent_tokenize(data)
    synonym = wordnet.synsets(concept)
    synonym1 = set(chain.from_iterable([word.lemma_names() for word in synonym]))
    for sentence in sentences:
        if any(item in sentence.lower() for item in synonym1):
            data = data.replace(sentence,'█'*len(sentence))
    return data

def redact(names_list, list_of_genders, dates, data):
    total = names_list + list_of_genders + dates
    for element in total:
        element = r'\b' + element + r'\b'
        block = len(element) * '\u2588'
        data = re.sub(element, block, data)
    return data
def stats(names_list, dates, list_of_genders, gender_count, statistics, file1):
    status = ''
    total = len(names_list) +  len(dates) + gender_count
    st = statistics[0]
    status += ("Following are the redactions for the files specified {}\n".format(file1))
    status += ("names redacted {} \n".format(len(names_list)))
    status += ("dates redacted {} \n".format(len(dates)))
    status += ("genders redacted{} \n".format(len(list_of_genders)-(gender_count)))
    status += ("Total redacted terms of extremely sensitive data names and dates{} \n".format(total))
    if st == 'stdout':
        print(status)
    elif st == 'stderr':
        err = ''
        sys.stderr.write(err)
    else:
        file_path = "stats.txt"
        with open(file_path, 'a',encoding="utf-8") as file:
            file.write(status)
            file.close()
    return status
#alternately instead of this, we can write individual functions and then do the  redaction process in that individual function and return the values to the main for depicting the st
#atistics. for redacting genders, we can use TreebankWordDetokenizer to tokenize the text. for dates, we can use the current one only, commonregex for parsing the text.
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
"""
#I also executed the file using the TreebankWordDetokenizer,and it is also running,
"""
def redact_genders(file):

    genders=['He', 'She', 'Himself', 'Herself', 'Male', 'Female', 'Him', 'Her', 'His', 'Hisself', 'Man', 'Woman', 'Men', 'Women', 'Husband', 'Wife', 'Gay']
    words = word_tokenize(file)
    
    for w in words:
        for term in genders:
            if w.lower()==term and not None:
                file=file.replace(w,'█'*len(w)) 
    file=re.sub(r'\bHe\b','██',file)
"""
