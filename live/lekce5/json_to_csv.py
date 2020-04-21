import json, csv

vstup = 'data.json'
vystup = 'csv_vystup.csv'

#https://realpython.com/python-csv/#writing-csv-file-from-a-dictionary-with-csv

with open(vstup,'r',encoding='utf-8') as _file, open(vystup, mode='w') as csv_file:
    
    data = json.load(_file)
    #print(data)

    fieldnames = ["first_name","last_name","email","gender"]

    # moznost jak dat jinou defaultni hodnotu nez '' v pripade ze nemam hodnotu
    # ve slovniku --> pouziti parametru restval='...' v DictWriteru
    #writer = csv.DictWriter(csv_file, fieldnames=fieldnames, restval='NULL')
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames,)
    writer.writeheader()    
    
    for row in data:
        print(row)
        writer.writerow(row)  
   
   