import re

path_for_csv_file = r'C:\Users\AMIT\Downloads\Sample Analysis File.csv'

with open(path_for_csv_file,'r') as csvfile:
    csvfile = csvfile.readlines()
    print(csvfile)
    for csvline in csvfile:
        if csvline == '\n':
            continue
        csvline = re.sub(',,+','',csvline)
        csvlinelist = csvline.split(',')
        if len(csvlinelist) == 1:
            subcsvfile = open(csvline.strip('\n')+'.csv','w')
            continue
        subcsvfile.write(csvline)