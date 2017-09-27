import csv
with open('CSV.csv','r',newline="",encoding='utf-8')as f:
    file=csv.reader(f)
    for row in file:
        print(','.join(row))
    
    

