import csv
ifile  = open('CSV.csv', "rb")
reader = csv.reader(ifile)
ofile  = open('CSV.csv', "wb")
writer = csv.writer(ofile, delimiter='q', quotechar='"', quoting=csv.QUOTE_ALL)
 
for row in reader:
    writer.writerow(row)
 
ifile.close()
ofile.close()

        
