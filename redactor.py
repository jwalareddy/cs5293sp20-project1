import main
import numpy
import sys
import glob

file_path = "stats/stats.txt"
with open(file_path, 'w',encoding="utf-8") as file:
    file.write('')
    file.close()
path1 = []
path2 = ''
concept = ''
sample_list = []
sample_list = sys.argv
flags = []
stats_list = []
n = 'names'
g = 'genders'
d = 'dates'
#print(len(sample_list))
del sample_list[0]

# all redaction actions are defined over here.
for i in range(len(sample_list)):
#    print(sample_list[i])
    if sample_list[i] == '--input':
        path1.append(sample_list[i+1])
    
    elif sample_list[i] == '--output':
        path2 = sample_list[i+1]
    
    elif sample_list[i] == '--concept':
        concept = sample_list[i+1]
    
    elif sample_list[i] == '--stats':
        stats_list.append(sample_list[i+1])

    elif sample_list[i].startswith('--'):
        flags.append(sample_list[i][2:])

for paths in path1:
    files = glob.glob(paths)
    
    for f in files:
        my_file = open(f, encoding = "ISO-8859-1")
        data = my_file.read()
        names_list = []
        list_of_genders = []
        gender_count = 0
        dates = []        
        list_of_concepts = []
        count_of_concepts = []
        print(f)
        if n in flags:
            data, names_list = main.names(data)
        if g in flags:
            data, list_of_genders, gender_count = main.genders(data)
        if d in flags:
            data,dates = main.dates(data)
        
        data, list_of_concepts, count_of_concepts = main.concept(data, concept)
        
        data = main.redact(names_list, list_of_genders, dates, list_of_concepts, data)
        status = main.stats(names_list, dates, list_of_genders, gender_count, list_of_concepts, count_of_concepts, stats_list, f)
        
        
        file_path = "stats/stats.txt"
        with open(file_path, 'a',encoding="utf-8") as file:
            file.write(status)
            file.close()
        
        
        f_name = path2 + f
        f_name = f_name.replace('.txt', '.redacted')
        with open(f_name, 'w', encoding = "utf-8")as file:
            file.write(data)
            file.close()


