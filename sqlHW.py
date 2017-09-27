import pymysql
from xlsxwriter.workbook import Workbook
from tabulate import tabulate 
mydb = pymysql.connect('localhost','root','root','Student')
cur=mydb.cursor()
def save_record():
    idno=int(input("Enter the id::"))
    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    query=("insert into studentdetails values(%d,'%s',%d);" %(idno,name,age))
    cur.execute(query)
    mydb.commit()
def show_all():
    query1=("select * from studentdetails;")
    cur.execute(query1)
    data=cur.fetchall()
    dat1=list(data)
    print(tabulate(dat1,['idno','Name','Age']))
def search_record(idno):
    query=("select * from studentdetails where idno = %d"%(idno))
    cur.execute(query)
    data=cur.fetchall()
    data1=list(data)
    print(tabulate(data1,['idno','Name','Age']))
def delete_record(idno):
    query=("delete from studentdetails where idno = %d"%(idno))
    cur.execute(query)
    mydb.commit()
def excel_file():
    query = ("select * from studentdetails;")
    cur.execute(query)
    workbook = Workbook('outfile.xlsx')
    sheet = workbook.add_worksheet()
    for r, rows in enumerate(cur.fetchall()):
        for c, cols in enumerate(rows):
            sheet.write(r, c, cols)
def record_check():
    Id=int(input("Enter ID"))
    query=("select * from studentdetails where idno=%d"%(Id))
    cur.execute(query)
    data=cur.fetchall()
    if not data:
        print('Record doesnt exist')
    else:
        print('Record found')
        print(data)
while True:
   print("Enter option:")
   print("1. Add")
   print("2. Show All")
   print("3. Search")
   print("4. Delete")
   print("5. Export to excel")
   print("6.Check if record exists by entering ID")
   print("7. Quit")
   opt=int(input("Enter your option::"))
   if opt==1:
        save_record()
   elif opt==2:
        show_all()
   elif opt==3:
        idno=int(input("Please enter a id to search::"))
        search_record(idno)
   elif opt==4:
        idno=int(input("Please enter a id to delete::"))
        delete_record(idno)
   elif opt==5:
        excel_file()
   elif opt==6:
        record_check()
   elif opt==7:
        break;
   else:
      print("Please Enter a Valid Option")
mydb.close()
