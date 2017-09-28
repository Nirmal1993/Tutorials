import smtplib
import time
from email.utils import COMMASPACE, formatdate
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from getpass import getpass
from smtplib import SMTP_SSL
from email import encoders
import mimetypes
from email.mime.multipart import MIMEMultipart
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
def email_file():
    fromaddr = input("Enter the from email address:")
    toaddr = input("Enter the TO email address:")
    # instance of MIMEMultipart
    msg = MIMEMultipart()
    # storing the senders email address  
    msg['From'] = fromaddr
    # storing the receivers email address 
    msg['To'] = toaddr
    # storing the subject 
    msg['Subject'] = "Subject of the Mail"
    # string to store the body of the mail
    body = "Body_of_the_mail"
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    # open the file to be sent 
    filename = "outfile.xlsx"
    attachment = open("C:\\Users\\Nirmal Manavalan\\AppData\\Local\\Programs\\Python\\Python36-32\\outfile.xlsx", "rb")
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    p.set_payload((attachment).read())
    # encode into base64
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com',587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(fromaddr, "windows2016")
    # Converts the Multipart msg into a string
    text = msg.as_string()
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
    # terminating the session
    s.quit()
      
while True:
   print("Enter option:")
   print("1. Add")
   print("2. Show All")
   print("3. Search")
   print("4. Delete")
   print("5. Export to excel")
   print("6.Email the file")
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
        email_file()
   elif opt==7:
        break;
   else:
      print("Please Enter a Valid Option")
mydb.close()
