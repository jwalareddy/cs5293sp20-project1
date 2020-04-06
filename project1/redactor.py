import main
import numpy
import sys
import glob
path_of_file = "stats/stats.txt"
with open(path_of_file, 'w',encoding="utf-8") as file:
    file.write('')
    #file.close()
path1 = []
path2 = ''
#concept = ''
#sample_list = []
sample_list = sys.argv
flags = []
statistics = []
nam = 'names'
gen = 'genders'
dat = 'dates'
print(len(sample_list))
#del sample_list[0]
# all redaction actions are defined over here.
for i in range(len(sample_list)):
    print(sample_list[i])
    #if sample_list[i].startswith('--'):
        #flags.append(sample_list[i][2:])
    if sample_list[i] == '--input':
        path1.append(sample_list[i+1])
    elif sample_list[i] == '--output':
        path2 = sample_list[i+1]
    elif sample_list[i] == '--concept':
        concept = sample_list[i+1]
    elif sample_list[i] == '--stats':
        statistics.append(sample_list[i+1])
    elif sample_list[i].startswith('--'):
        flags.append(sample_list[i][2:])
for paths in path1:
    list_of_files = glob.glob(paths)
    for file1 in list_of_files:
        file2 = open(file1, encoding = "ISO-8859-1")
        data = file2.read()
        names_list = []
        list_of_genders = []
        gender_count = 0
        dates = []
        #list_of_concepts = []
        #count_of_concepts = []
        #print(f)
        if nam in flags:
            names_list = main.names(data)
        #if g in flags:
            #data, list_of_genders, gender_count = main.genders(data)
        if dat in flags:
            data,dates = main.dates(data)
        #data, list_of_concepts, count_of_concepts = main.concept(data, concept)
        status = main.stats(names_list, dates, list_of_genders, gender_count, statistics, file1)
        #data = main.redact(names_list, list_of_genders, dates, list_of_concepts, data)
        data = main.redact(names_list, list_of_genders, dates, data)
        #status = main.stats(names_list, dates, list_of_genders, gender_count, stats_list, f)
        #status = main.stats(names_list, dates, list_of_genders, gender_count, list_of_concepts, count_of_concepts, stats_list, f)
        path_of_file = "stats/stats.txt"
        with open(path_of_file, 'a',encoding="utf-8") as file:
            file.write(status)
            file.close()
        file3 = path2 + file1
        file3 = file3.replace('.txt', '.redacted')
        with open(file3, 'w', encoding = "utf-8")as file:
            file.write(data)
            file.close()

