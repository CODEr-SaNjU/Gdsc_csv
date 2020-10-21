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

# Write  a program for split csv file in sub csvfiles

            # if request.method == 'POST':
    #     files = request.FILES['files']
    #     path_for_csv_file = f"/{files}"
    #     print(path_for_csv_file)
    #     with open(path_for_csv_file,'r') as csvfile:
    #         for csvline in csvfile:
    #             if csvline == '\n':
    #                 continue
    #             csvline = re.sub(',,+','',csvline)
    #             csvlinelist = csvline.split(',')
    #             if len(csvlinelist) == 1:
    #                 subcsvfile = open(csvline.strip('\n')+'.csv','w')
    #                 continue
    # return HttpResponse('csv created successfully')
    



 def createsubfiles(file_name):
        fulfile = open(file_name, 'r')  # giving filename

        fulread = fulfile.readlines()
        for i in range(len(fulread)):
            if i == 0:
                dict1['filepath'] = fulread[i]

            else:
                if '$' == fulread[i][0]:
                    if '/' in fulread[i]:
                        filenam = fulread[i].replace("/", " ")
                        dict1[filenam[0:-1]] = []
                    else:
                        filenam = fulread[i]
                        dict1[filenam[0:-1]] = []

                    for j in range(i, len(fulread)):
                        if j < len(fulread) - 1:
                            if '$' in fulread[j + 1]:
                                break
                            else:
                                dict1[filenam[0:-1]].append(fulread[j])
                        else:
                            dict1[filenam[0:-1]].append(fulread[j])

    filename = fpath1
    createsubfiles(filename)




