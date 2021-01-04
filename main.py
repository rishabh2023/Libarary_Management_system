import mysql.connector as dbc
import pandas as pd
from getpass import getpass
import re
import random
import smtplib
from datetime import datetime,timedelta,date
import math
import matplotlib.pyplot as plt
print('To Start the program you have to fill your credentials...')
while True:
    a = str(input('Enter your Username:'))
    b = getpass('Enter your password:')
    try:
        if a == 'admin' and b == '1234':
            mydb=dbc.connect(host='localhost',user='root',database=' library ')
            mycursor=mydb.cursor()
            
            while True:
                print('''**************************** Welcome *******************************************************
    1.Manage Books Details
    2.Manage Membership Record
    3.Manage Daily Record of Readers
    4.Manage Issue Record
    5.Manage Return Record
    6.Placing Order for Memeber
    7.Memeber Instance
    8.Statistics Data Visualization
    9.Exit
*****************************************************************************************************   ''')
            
                chooice1 = str(input('Enter your choice:'))
                if chooice1 == 'Exit' or chooice1 == '9':
                    print('Thankyou Vist again.. ')
                    break
                else:
                    if chooice1 == '1':
                        print('1.Add Book Details')
                        print('2.Delete Book Details')
                        print('3.Update Book Details')
                        print('4.Show All Books Details')
                        binput = str(input('Enter your what you what to do in book_detail:'))
                        if binput == '1' or binput == 'Add Book Details':
                            
                            while True:
                                book_id=input('Enter Book Id:')
                                if book_id == '':
                                    print('Book Id cannot be Empty something unique must be there..')
                                    continue
                                else:
                                    mycursor.execute('Select * from booksdetails where book_id = '+book_id)
                                    res = mycursor.fetchall()
                                    if len(res) == 0:
                                        break
                                    else:
                                        print('Book Id Already Exists..')
                                        continue
                            while True:
                                book_name=str(input('Enter Book Name:'))
                                if book_name == '':
                                    print('This field is mandatory..')
                                    print('It cannot be remain empty..')
                                    continue
                                else:
                                    break
                            category=str(input('Enter Category of Book:'))
                            while True:
                                try:
                                    quantity=int(input('Enter quantity of book:'))
                                    break
                                except:
                                    print('Quantity Should Not be in words It should be Numbers.....')
                            while True:
                                try:
                                    total_pages=int(input('Enter Total Pages:'))
                                    break
                                except:
                                    print('Total Pages Should Not be in words It should be Number.....')
                        
                            publisher=str(input('Enter Publisher Name:'))

                            while True:
                                try:
                                    edition=int(input('Enter Edition Year:'))
                                    break
                                except:
                                    print('Edition Year Should Not be in words It should be Number.....')
                            while True:
                                try:
                                    book_cost=int(input('Enter Book cost:'))
                                    book_cost = str(book_cost)
                                    break
                                except:
                                    print('This field is mandatory..')
                                    print('It cannot be remain empty..')                    
                            mycursor.execute('insert into BooksDetails values(%s,%s,%s,%s,%s,%s,%s,%s)',(book_id,book_name,category,quantity,total_pages,publisher,edition,book_cost))
                            mydb.commit()
                            print('Book Successfully Added in Database....')
                            o = input('Press Enter For main main menu')
                        elif binput == '2':
                            while True:
                                try:
                                    delb = str(input('Enter Book Id Which you want to delete:'))
                                    mycursor.execute('Select book_id from BooksDetails where book_id ='+delb)
                                    myresult = mycursor.fetchall()
                                    dl = len(myresult)
                                    if dl == 0 :
                                        print('Book Id that you have Entered is Not Found in Our Database Please Try again...')
                                    else:
                                        mycursor.execute('delete from BooksDetails where  book_id ='+delb)
                                        print('Book Id '+delb+ ' is Successfully Deleted From the Database...')
                                        o = input('Press Enter For main main menu')
                                        break
                                    mydb.commit()
                                except:
                                    print('Book Id cannot be Empty.... Please Enter Book ID...')
                        elif binput == '3':
                            print('''
    1.Book_name
    2.Category
    3.Quantity
    4.Total_page
    5.Publisher
    6.Edition
    7.Book_cost
                            ''')

                            lst1 = ['book_name','category','quantity','total_page','publisher','edition','book_cost','book_name']
                            while True:
                                try:
                                    ubook= int(input('Select column Which you want to change(only enter number at which your choice is there):'))
                                    if ubook >= 8 or ubook < 0 :
                                        print('Invalid Please Try With Valid Choice...')
                                    else:
                                        break
                                except:
                                    print('Please Enter Valid Choice its Empty.. ')
                            

                            while True:
                                try:
                                    rvalue = str(input('Enter Book ID:'))
                                    mycursor.execute('Select book_id from BooksDetails where book_id ='+rvalue)
                                    myresult = mycursor.fetchall()
                                    dl = len(myresult)
                                    if dl == 0 :
                                        print('Book Id that you have Entered is Not Found in Our Database Please Try again...')
                                    else:
                                        if  ubook == 4:
                                            while True:
                                                try:
                                                    mupdatev = int(input('Enter a New Set value of '+str(lst1[ubook-1])+' :'))
                                                    mupdatev = str(mupdatev)
                                                    break
                                                except:
                                                    print('Quantity Should Not be in words It should be Numbers.....')
                                        else:
                                            mupdatev = (input('Enter a New Set value:'))

                                        mycursor.execute('update booksdetails set '+str(lst1[ubook-1])+'='+'%s'+ 'where book_id ='+'%s',(mupdatev,rvalue))
                                        print('Value Successfully Changed...')
                                        mydb.commit()
                                        o = input('Press Enter For main main menu')
                                        break
                                    mydb.commit()
                                except:
                                    print('Book Id cannot be Empty.... Please Enter Book ID...')
                        elif binput == '4':
                            q=pd.read_sql('select * from '+ 'booksdetails',mydb)
                            print(q)
                            o = input('Press Enter For main main menu')
                    elif chooice1 == '2':
                        print('1.Add New Members')
                        print('2.Update Existance Member')
                        print('3.View Member Details')
                        minput = input('Enter your choice:')
                        if minput == '1' : 
                            print('Some points must keep in mind while creatind Member ID')
                            print('1.Id should be unique this information you will get from our program if it match with other Id..')
                            print('2.Id length should be greater than or equal to 5 and less than or equal to 10.. ')
                            member_id=input('Create New Member Id:')
                            while True:
                                try:
                                    mycursor.execute('Select member_id from membership where member_id ='+member_id)
                                    myresult = mycursor.fetchall()
                                    dl = len(myresult)
                                    if len(member_id) != 8:
                                        print('Id length should be  equal to 8 only.. ')
                                        member_id=input('Create New Member Id:')  
                                    elif dl == 1:
                                        print('Id That you have Created is already exits please Try again with different one..')
                                        member_id=input('Create New Member Id:')
                                    else:
                                        print('ID Successfully Created...')
                                        break
                                except:
                                    print('Member ID Should not be Empty something unique must be there and length of the Id must grater than or equal to 5 and less than equal to 10 Characters...') 
                                    member_id=input('Create New Member Id:')

                            while True:
                                member_name=input('Enter member name:')
                                chck = any(i.isdigit() for i in member_name )
                                try:
                                    member_name = int(member_name)
                                    print('Member Name Should Not be in Numbers.... ')
                                except:
                                    if member_name == '':
                                        print('Member Name Should not be Empty...')
                                    elif len(member_name) <= 3:
                                        print('Member Name Must be Greater than or equal to 3...')
                                    elif chck == True:
                                        print('Member Name Should not contain digits... please try again...')
                                    else:
                                        break
                            while True:
                                phone_no=input('Enter Phone No:')
                                if phone_no == '':
                                    print('It should not be Empty')
                                elif len(phone_no) != 10:
                                    print('It must be in 10 digits..')
                                else:
                                    try:
                                        phone_no=int(phone_no)
                                        break
                                
                                    except:
                                        print('It Should be in digits..')
                            while True:
                                cho = input('Do you have Email ID(YES/NO):')
                                if cho == 'yes' or cho == 'y' or cho == 'YES' or cho == 'Y':
                                    break
                                elif cho == 'no' or cho == 'n' or cho == 'NO' or cho == 'N':
                                    break
                                else:
                                    print('It takes only yes or no..')
                            ae = random.randint(1000,9999)
                            
                            if cho == 'yes' or cho == 'y' or cho == 'YES' or cho == 'Y':
                                while True:
                                    email_id=input('Enter email id of member:')
                                    if email_id == '':
                                        print('It should not be Empty..')
                                    else:
                                        break
                                while True:
                                    chck1 = input('Are you sure Email address you have entered is correct(yes/no):')
                                    if chck1 == 'yes' or chck1 == 'YES' or chck1 == 'y' or chck1 == 'Y': 
                                        
                                        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                                        if re.search(regex,email_id):
                                            try:
                                                SenderAddress = "" # Here Enter Senders Email address
                                                passwrd1  = 'kjmzlppyullangls'
                                                server = smtplib.SMTP('smtp.gmail.com',587)
                                                server.starttls()
                                                server.login(SenderAddress,passwrd1)
                                                msg = 'Dear ' + str(member_name) + 'Your Library Membership Account Email ID verification Code is...'+str(ae)+'. From Now onwards you will get important notifications from library \nRegards \nThankyou'
                                                subject = 'Library Email Address Verification'
                                                body = 'subject:{}\n\n{}'.format(subject,msg)
                                                server.sendmail(SenderAddress,email_id,body)
                                                server.quit() 
                                                print('Verification code is successfully sended on your email address please check it..')
                                                break
                                            except:
                                                print('No Internet connection try again...')  
                                                at = input('Press Enter to try again.. ')  
                                        else:
                                            print('Email address that you have enter is not valid please try again with valid email id...')
                                            email_id=input('Enter correct email id of member:')
                                    elif chck1 == 'no' or chck1 == 'NO' or chck1 == 'n' or chck1 == 'N': 
                                        email_id=input('Enter correct email id of member:')
                                    else:
                                        print('It should not be Empty and it takes only yes or no...')
                        
                                while True:
                                    try:
                                        otp = int(input('Enter OTP to verify your Email address:'))
                                        if otp == ae:
                                            print('Email address Successfully verified....')
                                            break                   
                                        else:
                                            print('Code You have entered is not correct...')
                                            print('Please try again with valid code...')
                                    except:
                                        print('It should be in digits..please try again')
                            elif cho == 'no' or cho == 'n' or cho == 'NO' or cho == 'N':
                                email_id = ''
                                pass                    
                            doj=datetime.now()
                            doj = datetime.date(doj)
                            while True:
                                age = input('Enter member age:')
                                if age == '':
                                    print('It should not be empty..It is mandatory to fill..')
                                    continue
                                try:
                                    age = int(age)
                                    if age >= 5 and age <=90:
                                        break
                                    else:
                                        print('Sorry we are giving membership to peoples whose age is between 5 to 90 years...')
                                except:
                                    print('Age you have entered is invalid..')
                                    print('It should be in digits..')
                                    print('Please try again with valid one...')
                            while True:
                                address=input('Enter address of member:')
                                if address == '':
                                    print('It should not be empty it is mandatory to fill..')
                                    print('Please try again..')
                                    continue
                                try:
                                    address = int(address)
                                    print('It should not be only in digits some words must be there..')
                                except:
                                    break
                            print('Plans Details...')
                            print('SN.              Days                              Price')
                            print('1.                90                                300/- ')
                            print('2.                150                               450/- ')
                            print('3.                180                               500/-')
                            print('4.                365(1 year)                       1000/-')
                            while True:
                                fees1=input('Enter plan no that you have selected:')
                                if fees1 == '':
                                    print('It should not be Empty Enter your valid choice...')
                                elif fees1 == '1':
                                    fees = 300
                                    da = '90 Days(3 months)'
                                    fees = int(fees)
                                    a = datetime.now()
                                    a = datetime.date(a)
                                    dov = a + timedelta(90)
                                    break
                                elif fees1 == '2':
                                    fees = int(450)
                                    da = '150 days(5 Months)'
                                    a = datetime.now()
                                    a = datetime.date(a)
                                    dov = a + timedelta(150)
                                    break
                                elif fees1 == '3':
                                    fees = int(500)
                                    da = '180 days(6 Months)'
                                    a = datetime.now()
                                    a = datetime.date(a)
                                    dov = a + timedelta(180)
                                    break
                                elif fees1 == '4':
                                    fees = int(1000)
                                    da = '365 days(full 1 year)'
                                    a = datetime.now()
                                    a = datetime.date(a)
                                    dov = a + timedelta(365)
                                    break
                                else:
                                    print('It only takes plan number that you have selected... ')
                            mycursor.execute('insert into  membership values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',( member_id ,member_name,str(phone_no) ,email_id ,age,doj,dov,address,fees))
                            mycursor.execute('INSERT INTO members_instance(member_id,member_name,joining_date,valid_last_date,address) VALUES (%s,%s,%s,%s,%s)',(member_id,member_name,doj,dov,address))
                            mydb.commit()
                            if email_id != '':
                                SenderAddress = "" # Here Enter Senders Email address
                                passwrd1  = 'kjmzlppyullangls'
                                server = smtplib.SMTP('smtp.gmail.com',587)
                                server.starttls()
                                server.login(SenderAddress,passwrd1)
                                msg = 'Dear ' + str(member_name) + ', Congratulations Your Library Membership Account is successfully actived for '+da+'from today or account is valid from '+str(doj.day)+'-'+str(doj.month)+'-'+str(doj.year)+' to '+str(dov.day)+'-'+str(dov.month)+'-'+str(dov.year)+'.\n In between this period you will get important notification from our libaray..IF any new book according to your choice is added in libary we will notify you.\nThankyou for Becoming our libaray member..\n Our Best wishes with you. \n Thankyou' 
                                subject = 'Congratulations Your account Successfully Activated'
                                body = 'subject:{}\n\n{}'.format(subject,msg)
                                server.sendmail(SenderAddress,email_id,body)
                                server.quit() 
                                print('Membership successfully granted by the library...')
                            else:
                                print('Membership successfully granted by the library...')
                                pass
                        elif minput == '2':
                            print('''
                            1.Phone Number
                            2.Email ID
                            3.Address
                            4.Membership''')
                            lst2 = ['phone_number' ,'email_id','address']
                            while True:
                                try:
                                    ubook= int(input('Enter your choice(it takes only numbers):'))
                                    if ubook <= 4 and ubook >=1:
                                        break
                                    else:
                                        print('Your Choice is Invalid please try again...')
                                except:
                                    print('Your choice is Invalid please try again...')
                            
                            while True:
                                try:
                                    rvalue = str(input('Enter Member ID in which you want to make updates:'))
                                    mycursor.execute('Select member_id from membership where member_id ='+rvalue)
                                    myresult = mycursor.fetchall()
                                    dl = len(myresult)
                                    if dl == 0 :
                                        print('Member Id that you have Entered is Not Found in Our Database Please Try again...')
                                    else:
                                        print('Member Id that you entered is successfully found in our database..')
                                        break
                                    mydb.commit()
                                except:
                                
                                    print('Member ID cannot be Empty.... Please Enter Member ID...')
                            if ubook == 2:
                                print(rvalue)
                                ae = random.randint(1000,9999)
                                while True:
                                    email_id=input('Enter email id of member:')
                                    if email_id == '':
                                        print('It should not be Empty..')
                                    else:
                                        break
                                while True:
                                    chck1 = input('Are you sure Email address you have entered is correct(yes/no):')
                                    if chck1 == 'yes' or chck1 == 'YES' or chck1 == 'y' or chck1 == 'Y': 
                                        
                                        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                                        if re.search(regex,email_id):
                                            try:
                                                mycursor.execute('Select member_name from membership where member_id = '+str(rvalue))
                                                myresult = mycursor.fetchall()
                                                member_name = myresult[0][0]
                                                SenderAddress = "" # Here Enter Senders Email address
                                                passwrd1  = 'kjmzlppyullangls'
                                                server = smtplib.SMTP('smtp.gmail.com',587)
                                                server.starttls()
                                                server.login(SenderAddress,passwrd1)
                                                msg = 'Dear ' + str(member_name) + ' Your Library Membership Account Email ID verification Code is...'+str(ae)+'. From Now onwards you will get important notifications from library \nRegards \nThankyou'
                                                subject = 'Library Email Address Verification'
                                                body = 'subject:{}\n\n{}'.format(subject,msg)
                                                server.sendmail(SenderAddress,email_id,body)
                                                server.quit() 
                                                print('Verification code is successfully sended on your email address please check it..')
                                                break
                                            except:
                                                print('No Internet connection try again...')  
                                                at = input('Press Enter to try again.. ')  
                                        else:
                                            print('Email address that you have enter is not valid please try again with valid email id...')
                                            email_id=input('Enter correct email id of member:')
                                    elif chck1 == 'no' or chck1 == 'NO' or chck1 == 'n' or chck1 == 'N': 
                                        email_id=input('Enter correct email id of member:')
                                    else:
                                        print('It should not be Empty and it takes only yes or no...')
                        
                                while True:
                                    try:
                                        otp = int(input('Enter OTP to verify your Email address:'))
                                        if otp == ae:
                                            print('Email address Successfully verified....')
                                            mycursor.execute('update membership set '+str(lst2[ubook-1])+'='+'%s'+ 'where  member_id ='+'%s',(email_id,rvalue))
                                            mydb.commit()
                                            break                   
                                        else:
                                            print('Code You have entered is not correct...')
                                            print('Please try again with valid code...')
                                    except:
                                        print('It should be in digits..please try again')
                            else:
                                if ubook == 4:
                                    mycursor.execute('Select last_date from membership where member_id ='+rvalue)
                                    rem = mycursor.fetchall()
                                    ab = datetime.now()
                                    cd = ab.date()
                                    if cd > rem[0][0]:
                                        print('Plans Details...')
                                        print('SN.              Days                              Price')
                                        print('1.                90                                300/- ')
                                        print('2.                150                               450/- ')
                                        print('3.                180                               500/-')
                                        print('4.                365(1 year)                       1000/-')
                                        while True:
                                            fees1=input('Enter plan no that you have selected:')
                                            if fees1 == '':
                                                print('It should not be Empty Enter your valid choice...')
                                            elif fees1 == '1':
                                                fees = 300
                                                da = '90 Days(3 months)'
                                                fees = int(fees)
                                                a = datetime.now()
                                                a = datetime.date(a)
                                                dov = a + timedelta(90)
                                                break
                                            elif fees1 == '2':
                                                fees = int(450)
                                                da = '150 days(5 Months)'
                                                a = datetime.now()
                                                a = datetime.date(a)
                                                dov = a + timedelta(150)
                                                break
                                            elif fees1 == '3':
                                                fees = int(500)
                                                da = '180 days(6 Months)'
                                                a = datetime.now()
                                                a = datetime.date(a)
                                                dov = a + timedelta(180)
                                                break
                                            elif fees1 == '4':
                                                fees = int(1000)
                                                da = '365 days(full 1 year)'
                                                a = datetime.now()
                                                a = datetime.date(a)
                                                dov = a + timedelta(365)
                                                break
                                            else:
                                                print('It only takes plan number that you have selected... ')
                                        mycursor.execute("update membership set date_of_joining = '{0}' , last_date = '{1}' where  member_id = '{2}'".format(cd,dov,rvalue))
                                        mydb.commit()
                                        print('Congratulations your Membership limit exceeded successfully')
                                        oo = input('Press Enter for Main Menu:')
                                    else:
                                        print('Member already having membership...')
                                        print('If it expire then member can updates its membership')
                                        oo = input('Press Enter for Main Menu:')
                                else:
                                    mupdatev = input('Enter a Set  new value:')
                                    mycursor.execute('update membership set '+str(lst2[ubook-1])+'='+'%s'+ 'where  member_id ='+'%s',(mupdatev,rvalue))
                                    mydb.commit()
                
                        elif minput == '3':
                            q=pd.read_sql('select * from  membership',mydb)
                            print(q)
                            ok = input('Press Enter for main menu:')
                    elif chooice1 == '3':
                        print('1.Add Data')
                        print('2.Show Data')
                        dainput = input('Enter your Choice:')
                        if dainput == '1':
                            while True:
                                persona_name=str(input('Enter guest name:'))
                                if persona_name == '':
                                    print('Guest cannot be empty..')
                                    continue
                                try:
                                    persona_name = int(persona_name)
                                    print('It should be in words..')
                                    print('Guest Name cannot be in digits please try again with valid choice.. ')
                                except:
                                    break
                                
                            while True:
                                phone_no=input('Enter Guest Phone No:')
                                if phone_no == '':
                                    print('It should not be Empty it is mandatory to fill..')
                                elif len(phone_no) != 10:
                                    print('Phone number is invalid..')
                                else:
                                    try:
                                        phone_no=int(phone_no)
                                        break
                                
                                    except:
                                        print('It Should be in digits..')
                            email=input('Enter email id of guest:')
                            while True:
                                occupation=input('Enter occupation of Guest:')
                                if occupation == '':
                                    print('It is mandatory to fill..')
                                    continue
                                else:
                                    try:
                                        occupation = int(occupation)
                                        print('It should not be in integer is should br in words..')
                                    except:
                                        break
                            while True:
                                address=input('Enter address of Guest:')
                                if address == '':
                                    print('It should not be empty it is mandatory to fill..')
                                    print('Please try again..')
                                    continue
                                try:
                                    address = int(address)
                                    print('It should not be only in digits some words must be there..')
                                except:
                                    break
                            b  = datetime.now()
                            date = datetime.date(b)
                            mycursor.execute('insert into  daily_record values(%s,%s,%s,%s,%s,%s)',( persona_name,phone_no,email , occupation, address,date))
                            mydb.commit()
                        elif dainput == '2':
                            q=pd.read_sql('select * from '+ 'daily_record',mydb)
                            print(q)
                            ool = input('Press Enter for main menu: ') 
                        else:
                            print('Sorry,your choice is not valid..')
                    elif chooice1 == '4':
                        print('1.Issue New Book')
                        print('2.View Issue Record')
                        print('3.View Penalty')
                        isinput = input('Enter your Choice:')
                        if isinput == '1':
                            while True:
                                try:
                                    mi = str(input('Enter Member Id on which you want to issue:'))
                                    mycursor.execute('Select member_id,member_name from membership where member_id ='+mi)
                                    myresult = mycursor.fetchall()
                                    dl = len(myresult)
                                    if dl == 0 :
                                        print('Member Id that you have Entered is Not Found in Our Database Please Try again...')
                                    else:
                                        print('Member ID '+str(mi)+' Found With Member Name '+str(myresult[0][1]))
                                        conf = input('Is it correct(Yes)?:')
                                        if conf == 'yes' or conf == 'y' or conf == 'Yes' or conf == 'Y':
                                            break
                                        else:
                                            print('Try again..')
                                            continue
                                except:
                                    print('Memeber Id cannot be Empty.... Please Enter Member ID...')
                            while True:
                                try:
                                    bi = str(input('Enter Book Id on which you want to issue:'))
                                    mycursor.execute('Select book_id,book_name from booksdetails where book_id = '+bi)
                                    myresult = mycursor.fetchall()
                                    dl = len(myresult)
                                    if dl == 0 :
                                        print('Book Id that you have Entered is Not Found in Our Database Please Try again...')
                                    else:
                                        print('Book ID '+str(bi)+' Found With Book Name '+str(myresult[0][1]))
                                        conf = input('Is it correct(Yes)?:')
                                        if conf == 'yes' or conf == 'y' or conf == 'Yes' or conf == 'Y':
                                            break
                                        else:
                                            print('Try again..')
                                            continue
                                except:
                                    print('Book Id cannot be Empty.... Please Enter Book ID...')
                            mycursor.execute('Select book_name,publisher from booksdetails where book_id = '+bi)
                            myresult1 = mycursor.fetchall()
                            bn=myresult1[0][0]
                            publisher=myresult1[0][1]
                            mycursor.execute('Select member_name,address from membership where member_id = '+mi)
                            myresult2 = mycursor.fetchall()
                            membername = myresult2[0][0]
                            add = myresult2[0][1]
                            b  = datetime.now()
                            mn = datetime.date(b)
                            a = datetime.now()
                            a = datetime.date(a)
                            ld = a + timedelta(7)
                            mpenanlty = 0
                            mycursor=mydb.cursor()
                            mycursor.execute('Select last_date from membership where member_id = '+str(mi))
                            myresult221 = mycursor.fetchall()
                            myresult211 = myresult221[0][0]
                            fa = datetime.now()
                            fa = datetime.date(fa)
                            if fa<=myresult211:
                                q=pd.read_sql('select * from  booksdetails',mydb)                
                                c=0
                                for i in q.book_id:
                                    if i==bi:
                                        z=q.iloc[[c],[3]]-1
                                        z=z.at[c,'quantity']
                                        if z<0:
                                            print('This book is out of stock')
                                            break
                                        z=str(z)                            
                                        bz=str(bi)
                                        a = datetime.now()
                                        a = datetime.date(a)
                                        year = a.year
                                        month = a.month
                                        day = a.day
                                        mycursor.execute('Select member_id from issue_records where issue_date ='+str(year)+str(month)+str(day)+ ' and member_id ='+str(mi))
                                        myresult = mycursor.fetchall()
                                        cheklst = []
                                        for m in myresult:
                                            cheklst.append(m)
                                        check = len(cheklst)
                                        mycursor.execute('Select member_id from issue_records where member_id ='+str(mi))
                                        myresult11 = mycursor.fetchall()
                                        cheklst11 = []
                                        for j in myresult11:
                                            cheklst.append(j)
                                        check1 = len(cheklst11)
                                        mycursor.execute('Select member_id from issue_records where member_id = '+str(mi)+' and book_id = '+str(bi))
                                        myresult22 = mycursor.fetchall()
                                        cheklst22 = []
                                        for k in myresult22:
                                            cheklst22.append(k)
                                        check2 = len(cheklst22)
                                        if check <=2 and check1 <= 4 and check2 == 0:
                                            mycursor.execute('Select no_of_books_issues from members_instance where member_id = '+str(mi))
                                            myresulti = mycursor.fetchall()
                                            ni = int(myresulti[0][0])+1
                                            mycursor.execute('update members_instance set no_of_books_issues = '+str(ni)+ ' where member_id = '+str(mi))
                                            mycursor.execute('update booksdetails set quantity ='+ z +' where book_id = "'+bz+'";')
                                            mycursor.execute('insert into  issue_records values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',( mi,bi,bn,publisher,membername,mn,ld,add,mpenanlty)) 
                                            mydb.commit()
                                            print('Book Issued Successfully of Given Id...')
                                        elif check >=3:
                                            print("Sorry Member's Todays limit of issuing book is full..")
                                            print("So Today we can't issue the book for Member..")
                                            f = input('Press Enter for main menu')
                                        elif check1 > 4:
                                            print('Member already having 4 books we cannot issue more book..')
                                            f = input('Press Enter for main menu')
                                        elif check2 > 0:
                                            print('We cannot issue more than one book on the same Member ID ')
                                            print('Member already having the same Book..')
                                            f = input('Press Enter for main menu')
                                        c=c+1 
                            else:
                                print("You are not eligible for issuing the book because your membership is Expired please try after taking membership again..")                                           
                        elif isinput == '2':
                            q=pd.read_sql('select * from issue_records',mydb)
                            print(q)    
                    elif chooice1 == '5':
                        print('1.Return Book')
                        print('2.View Return Record')
                        isinput = input('Enter your Choice:')
                        if isinput == '1':
                            while True:
                                mi=input('Enter member id:')
                                bi=input('Enter book id:')
                                if mi == '' or bi == '':
                                    print('Cannot be Empty..')
                                    continue
                                else:
                                    mycursor=mydb.cursor()
                                    mycursor.execute('Select member_id from issue_records where member_id ='+str(mi)+' and book_id = '+str(bi))
                                    myresult = mycursor.fetchall()
                                    a = []
                                    for i in myresult:
                                        a.append(i)
                                    ch = len(a)
                                    if ch == 0:
                                        print('Please check Book id or member_id it may be invalid..')
                                        continue
                                    else:
                                        break
                            mycursor=mydb.cursor()
                            mycursor.execute('Select * from issue_records where member_id ='+str(mi)+' and book_id = '+str(bi))
                            myresult = mycursor.fetchall()
                            bn=myresult[0][2]
                            membername = myresult[0][4]
                            publisher=myresult[0][3]
                            add = myresult[0][7]
                            a = datetime.now()
                            a = datetime.date(a)
                            year = a.year
                            month = a.month
                            day = a.day 
                            mycursor=mydb.cursor()
                            mycursor.execute('Select last_date from issue_records where member_id = '+str(mi)+' and book_id = '+str(bi))
                            myresult = mycursor.fetchall()
                            mdate = myresult[0][0]
                            year1 = mdate.year
                            month1 = mdate.month
                            day1 = mdate.day
                            c = date(year,month,day)
                            b = date(year1,month1,day1)
                            d = c-b
                            chd = d.days
                            if chd>0:
                                up = chd*5
                                mycursor=mydb.cursor()
                                mycursor.execute('Select penalty from issue_records where member_id = '+str(mi)+' and book_id = '+str(bi))
                                myresult = mycursor.fetchall()
                                mpan  = myresult[0][0]
                                if mpan != up:
                                    mycursor.execute('update issue_records set penalty ='+ str(up) +' where book_id = '+str(bi)+' and member_id = '+str(mi))
                                    mydb.commit()
                            mycursor.execute('Select penalty,issue_date,last_date from issue_records where member_id = '+str(mi)+' and book_id = '+str(bi))
                            myresult = mycursor.fetchall()
                            mpan1  = myresult[0][0]
                            if mpan1 > 0:
                                print('you have to pay '+str(mpan1)+' rupees panalty Because you are '+ str(chd)+' days Late to submit book..')
                                pansub = int(input('Enter Panalty:'))
                                if str(pansub) == str(mpan1):
                                    mycursor.execute('Select total_penalty from members_instance where member_id = '+str(mi))
                                    myresulti = mycursor.fetchall()
                                    ni = int(myresulti[0][0])+pansub
                                    mycursor.execute('update members_instance set total_penalty = '+str(ni)+' where member_id = '+str(mi))
                                    mycursor=mydb.cursor()
                                    mycursor.execute('Select quantity from booksdetails where book_id = '+str(bi))
                                    myresult22 = mycursor.fetchall()
                                    myres = myresult22[0][0]+1
                                    mycursor.execute('Select no_of_books_returned from members_instance where member_id = '+str(mi))
                                    myresulti = mycursor.fetchall()
                                    ni = int(myresulti[0][0])+1
                                    mycursor.execute('update members_instance set no_of_books_returned = '+str(ni)+' where member_id = '+str(mi))
                                    mycursor.execute('update booksdetails set quantity ='+ str(myres) +' where book_id = '+str(bi))
                                    mycursor.execute('insert into returned_records values(%s,%s,%s,%s,%s,%s,%s,%s)',( mi,bi,bn,publisher,membername,myresult[0][1],myresult[0][2],add)) 
                                    mycursor.execute('Delete From issue_records where member_id = '+str(mi)+' and book_id = '+str(bi))
                                    mydb.commit()
                                    print('Book Returned in libaray successfully..')
                                else:
                                    print('You have to pay '+str(mpan1)+' rupees only not more nor less')
                            else:
                                mycursor=mydb.cursor()
                                mycursor.execute('Select quantity from booksdetails where book_id = '+str(bi))
                                myresult22 = mycursor.fetchall()
                                myres = myresult22[0][0]+1
                                mycursor.execute('Select no_of_books_returned from members_instance where member_id = '+str(mi))
                                myresulti = mycursor.fetchall()
                                ni = int(myresulti[0][0])+1
                                mycursor.execute('update members_instance set no_of_books_returned = '+str(ni)+' where member_id = '+str(mi))
                                mycursor.execute('update booksdetails set quantity ='+ str(myres) +' where book_id = '+str(bi))
                                mycursor.execute('insert into returned_records values(%s,%s,%s,%s,%s,%s,%s,%s)',( mi,bi,bn,publisher,membername,myresult[0][1],myresult[0][2],add)) 
                                mycursor.execute('Delete From issue_records where member_id = '+str(mi)+' and book_id = '+str(bi))
                                mydb.commit()
                                print('Book Returned in libraray successfully..') 
                        elif isinput == '2':
                            q=pd.read_sql('select * from  returned_records',mydb)
                            print(q)
                            ok = input('Press Enter for main menu')
                    elif chooice1 == '6':
                        print('1.New order')
                        print('2.Delivering order')
                        print('3.Cancel order')
                        print('4.View Orders')
                        oinput = input('Enter your choice:')
                        if oinput == '1':
                            while True:
                                try:
                                    mi = str(input('Enter Member Id on which you want to order:'))
                                    mycursor.execute('Select member_id,member_name from membership where member_id ='+mi)
                                    myresult = mycursor.fetchall()
                                    dl = len(myresult)
                                    if dl == 0 :
                                        print('Member Id that you have Entered is Not Found in Our Database Please Try again...')
                                    else:
                                        print('Member ID '+str(mi)+' Found With Member Name '+str(myresult[0][1]))
                                        conf = input('Is it correct(Yes)?:')
                                        if conf == 'yes' or conf == 'y' or conf == 'Yes' or conf == 'Y':
                                            break
                                        else:
                                            print('Try again..')
                                            continue
                                except:
                                    print('Memeber Id cannot be Empty.... Please Enter Member ID...')
                            mycursor.execute('Select email_id from membership where member_id = '+mi)
                            eres = mycursor.fetchall()
                            eres = eres[0][0]
                            if eres == '':
                                print("Sorry Member's email id is not verified in our libaray")
                                print('Firstly they have to verify their Email Id in our library then they take advantage to this fuction.. ')
                                print('Email Id Not verified..')
                            else:
                                while True:
                                    try:
                                        bi = str(input('Enter Book Id that you want to order:'))
                                        mycursor.execute('Select book_id,book_name from booksdetails where book_id = '+bi)
                                        myresult = mycursor.fetchall()
                                        dl = len(myresult)
                                        if dl == 0 :
                                            print('Book Id that you have Entered is Not Found in Our Library Please Try again...')
                                        else:
                                            print('Book ID '+str(bi)+' Found With Book Name '+str(myresult[0][1]))
                                            conf = input('Is it correct(Yes)?:')
                                            if conf == 'yes' or conf == 'y' or conf == 'Yes' or conf == 'Y':
                                                break
                                            else:
                                                print('Try again..')
                                                continue
                                    except:
                                        print('Book Id cannot be Empty.... Please Enter Book ID...')
                                mycursor.execute('Select book_name,publisher from booksdetails where book_id = '+bi)
                                myresult1 = mycursor.fetchall()
                                bn=myresult1[0][0]
                                publisher=myresult1[0][1]
                                mycursor.execute('Select member_name,address from membership where member_id = '+mi)
                                myresult2 = mycursor.fetchall()
                                membername = myresult2[0][0]
                                add = myresult2[0][1]
                                b  = datetime.now()
                                mn = datetime.date(b)               
                                bz=str(bi)
                                a = datetime.now()
                                a = datetime.date(a)
                                year = a.year
                                month = a.month
                                day = a.day
                                mycursor.execute('Select member_id from order_book where Date_of_order ='+str(year)+str(month)+str(day)+ ' and member_id ='+str(mi))
                                myresult = mycursor.fetchall()
                                cheklst = []
                                for m in myresult:
                                    cheklst.append(m)
                                check = len(cheklst)
                                mycursor.execute('Select member_id from order_book where member_id ='+str(mi))
                                myresult11 = mycursor.fetchall()
                                cheklst11 = []
                                for j in myresult11:
                                    cheklst.append(j)
                                check1 = len(cheklst11)
                                mycursor.execute('Select member_id from order_book where member_id = '+str(mi)+' and book_id = '+str(bi))
                                myresult22 = mycursor.fetchall()
                                cheklst22 = []
                                mycursor.execute('Select book_cost from booksdetails where book_id = '+str(bi))
                                myresult11m = mycursor.fetchall()
                                mresp = myresult11m[0][0]
                                for k in myresult22:
                                    cheklst22.append(k)
                                check2 = len(cheklst22)
                                print('You have to pay '+str(mresp)+' rupees..')
                                paytm = str(input('Current payment status(yes/no):'))
                                if paytm == 'yes' or paytm == 'y' or paytm == 'Y' or paytm == 'YES':
                                    payment_status = 'yes'
                                else:
                                    payment_status = 'no'
                                    if check <=2  and check2 == 0:
                                        mycursor.execute('insert into  order_book values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(bn,bi,publisher,payment_status,mi,mresp,mn,membername,str(date(1111,11,11))))
                                        mydb.commit()
                                        print('Book Ordered Successfully of Given Id...')
                                        print('You will get book after 5 days.. ')
                                    elif check >2:
                                        print("Sorry Member's Todays limit of ordering book is full..")
                                        print("So Today we can't order the book for Member..")
                                        f = input('Press Enter for main menu')
                                    elif check2 > 0:
                                        print('We cannot order more than one book on the same Member ID ')
                                        print('Member already having the same Book..')
                                        f = input('Press Enter for main menu')
                        elif oinput == '2':
                            while True:
                                try:
                                    mi = str(input('Enter Member Id on which you ordered book:'))
                                    mycursor.execute('Select member_id,member_name from membership where member_id ='+mi)
                                    myresult = mycursor.fetchall()
                                    dl = len(myresult)
                                    if dl == 0 :
                                        print('Member Id that you have Entered is Not Found in Our Database Please Try again...')
                                    else:
                                        print('Member ID '+str(mi)+' Found With Member Name '+str(myresult[0][1]))
                                        conf = input('Is it correct(Yes)?:')
                                        if conf == 'yes' or conf == 'y' or conf == 'Yes' or conf == 'Y':
                                            break
                                        else:
                                            print('Try again..')
                                            continue
                                except:
                                    print('Memeber Id cannot be Empty.... Please Enter Member ID...')

                            mycursor.execute('Select email_id from membership where member_id = '+mi)
                            eres = mycursor.fetchall()
                            eres = eres[0][0]
                            if eres == '':
                                print("Sorry Member's email id is not verified in our libaray")
                                print('Firstly they have to verify their Email Id in our library then they take advantage to this fuction.. ')
                                print('Email Id Not verified..')
                            else:
                                while True:
                                    try:
                                        bi = str(input('Enter Book Id that you ordered:'))
                                        mycursor.execute('Select book_id,book_name from booksdetails where book_id = '+bi)
                                        myresult = mycursor.fetchall()
                                        dl = len(myresult)
                                        if dl == 0 :
                                            print('Book Id that you have Entered is Not Found in Our Library Please Try again...')
                                        else:
                                            print('Book ID '+str(bi)+' Found With Book Name '+str(myresult[0][1]))
                                            conf = input('Is it correct(Yes)?:')
                                            if conf == 'yes' or conf == 'y' or conf == 'Yes' or conf == 'Y':
                                                break
                                            else:
                                                print('Try again..')
                                                continue
                                    except:
                                        print('Book Id cannot be Empty.... Please Enter Book ID...')
                                mycursor.execute('Select Date_of_order,Date_of_delivery from order_book where member_id = '+str(mi)+' and book_id = '+str(bi))
                                myresult4 = mycursor.fetchall()
                                if len(myresult4) == 0:
                                    print('Your member id and book id does not match...')
                                    oo = input('Press Enter For main menu:')
                                else:
                                    od = myresult4[0][0]
                                    ld = od + timedelta(5)
                                    b  = datetime.now()
                                    cd = datetime.date(b)
                                    mld = myresult4[0][1]
                                    if  mld == date(1111,11,11):
                                        if  cd >= ld:
                                            mycursor.execute('Select payment_status from order_book where member_id = '+str(mi)+' and book_id = '+str(bi))
                                            myresult = mycursor.fetchall()
                                            if myresult[0][0] == 'no':
                                                mycursor.execute('Select book_cost from booksdetails where book_id = '+str(bi))
                                                myresult11m = mycursor.fetchall()
                                                mresp = myresult11m[0][0]   
                                                print('Your Book payment is due..')
                                                print('You have to pay '+str(mresp)+' rupees..then we will handover the book to you..')
                                                while True:
                                                    paytm = int(input('Enter Payment:'))

                                                    if paytm == int(mresp):
                                                        date1 = datetime.now()
                                                        date1 = date1.date()
                                                        mycursor.execute('Update order_book set payment_status = "yes" where book_id = '+str(bi)+' and member_id = '+str(mi))
                                                        mycursor.execute("Update order_book set Date_of_delivery = '{0}' where book_id = '{1}' and member_id = '{2}'".format(date1,bi,mi))
                                                        mydb.commit()
                                                        print('Book delivered Successfully')
                                                        break
                                                    else:
                                                        print('Sorry please submit only '+str(mresp)+' rupees not more nor less..')
                                            
                                            else:
                                                date1 = datetime.now()
                                                date1 = date1.date()
                                                mycursor.execute("Update order_book set Date_of_delivery = '{0}' where book_id = '{1}' and member_id = '{2}'".format(date1,bi,mi))
                                                print('Book delivered Successfully')
                                        else:
                                            print('We will handover your ordered book on '+str(ld.day)+'-'+str(ld.month)+'-'+str(ld.year))
                                            kk = input('Press Enter for main menu:')

                                    elif  mld != date(1111,11,11):
                                        print('The Book your ordered is already delivered successfully on this member Id ..')
                                        a = input('Press enter for main menu: ')
                                            
                                    else:
                                        print('We will handover your ordered book on '+str(ld.day)+'-'+str(ld.month)+'-'+str(ld.year))
                                        kk = input('Press Enter for main menu:')
                        elif oinput == '3':
                            print('Note')
                            print('->Member cannot cancel order after 2 days of order or member only cancel order within two days only..')
                            print('->If your payment is done so your money will be refunded.')
                            while True:
                                try:
                                    mi = str(input('Enter Member Id on which you ordered book:'))
                                    mycursor.execute('Select member_id,member_name from order_book where member_id ='+mi)
                                    myresult = mycursor.fetchall()
                                    dl = len(myresult)
                                    if dl == 0 :
                                        print('Member Id that you Entered is not ordered anything yet member not found..')
                                    else:
                                        print('Member ID '+str(mi)+' Found With Member Name '+str(myresult[0][1]))
                                        conf = input('Is it correct(Yes)?:')
                                        if conf == 'yes' or conf == 'y' or conf == 'Yes' or conf == 'Y':
                                            break
                                        else:
                                            print('Try again..')
                                            continue
                                except:
                                    print('Memeber Id cannot be Empty.... Please Enter Member ID...')
                            mycursor.execute('Select email_id from membership where member_id = '+mi)
                            eres = mycursor.fetchall()
                            eres = eres[0][0]
                            if eres == '':
                                print("Sorry Member's email id is not verified in our libaray")
                                print('Firstly they have to verify their Email Id in our library then they take advantage to this fuction.. ')
                                print('Email Id Not verified..')
                            else:
                                while True:
                                    try:
                                        bi = str(input('Enter Book Id that you ordered:'))
                                        mycursor.execute('Select book_id,book_name from order_book where book_id = '+bi)
                                        myresult = mycursor.fetchall()
                                        dl = len(myresult)
                                        if dl == 0 :
                                            print('Book Id that you have Entered is Not ordered yet...')
                                        else:
                                            print('Book ID '+str(bi)+' Found With Book Name '+str(myresult[0][1]))
                                            conf = input('Is it correct(Yes)?:')
                                            if conf == 'yes' or conf == 'y' or conf == 'Yes' or conf == 'Y':
                                                break
                                            else:
                                                print('Try again..')
                                                continue
                                    except:
                                        print('Book Id cannot be Empty.... Please Enter Book ID...') 
                                mycursor.execute('Select member_name,book_name,Date_of_order,payment_status,price from order_book where book_id = '+ str(bi) +' and member_id = '+ str(mi))
                                myresultl = mycursor.fetchall()
                                ol = myresultl[0][2]
                                a = datetime.now()
                                cd = datetime.date(a)
                                ld1 = ol+timedelta(2)
                                if cd > ld1 :
                                    print('We cannot cancel your order because you are so late')
                                else:
                                    if myresultl[0][3] == 'yes':
                                        rn = random.randint(1000,9999)
                                        mycursor.execute('Select email_id,member_name from membership where member_id ='+str(mi))
                                        myresulte = mycursor.fetchall()
                                        email_id = myresulte[0][0]
                                        while True:
                                            try:
                                                member_name = myresulte[0][1]
                                                SenderAddress = "" # Here Enter Senders Email address
                                                passwrd1  = 'kjmzlppyullangls'
                                                server = smtplib.SMTP('smtp.gmail.com',587)
                                                server.starttls()
                                                server.login(SenderAddress,passwrd1)
                                                msg = 'Dear ' + str(member_name) + ' Your Order cancellation confirmation Code is...'+str(rn)+'. Please give this code to libarian.. \nRegards \nThankyou'
                                                subject = 'Order Cancellation Code'
                                                body = 'subject:{}\n\n{}'.format(subject,msg)
                                                server.sendmail(SenderAddress,email_id,body)
                                                server.quit() 
                                                print('Confirmation code is successfully sended on Members email address please check it..')
                                                break
                                            except:
                                                print('No Internet connection try again...')  
                                                at = input('Press Enter to try again.. ')
                                        print(str(myresultl[0][4])+' rupees is refunded back by the libary to member_id '+str(mi))
                                        while True:
                                            try:
                                                ccode = int(input('Enter Cancelation code:'))
                                                break
                                            except:
                                                print('Please Enter only four digits integer value..')
                                                continue
                                        if rn == ccode:
                                            print('Code successfully Verified..')
                                            mycursor.execute('Select email_id,member_name from membership where member_id ='+str(mi))
                                            myresulte = mycursor.fetchall()
                                            email_id = myresulte[0][0]
                                            while True:
                                                try:
                                                    member_name = myresulte[0][1]
                                                    SenderAddress = "" # Here Enter Senders Email address
                                                    passwrd1  = 'kjmzlppyullangls'
                                                    server = smtplib.SMTP('smtp.gmail.com',587)
                                                    server.starttls()
                                                    server.login(SenderAddress,passwrd1)
                                                    msg = 'Dear ' + str(member_name) +',\nYour Order of the book is Successfully Cancelled... \nRegards \nThankyou'
                                                    subject = 'Order Cancellation information'
                                                    body = 'subject:{}\n\n{}'.format(subject,msg)
                                                    server.sendmail(SenderAddress,email_id,body)
                                                    server.quit() 
                                                    break
                                                except:
                                                    print('No Internet connection try again...')  
                                                    at = input('Press Enter to try again.. ')
                                            mycursor.execute('Delete From order_book where book_id = '+bi+' and member_id = '+str(mi))
                                            mydb.commit()
                                            print('Order Cancelled Successfully')       
                                    else:
                                        mycursor.execute('Select email_id,member_name from membership where member_id ='+str(mi))
                                        myresulte = mycursor.fetchall()
                                        email_id = myresulte[0][0]
                                        while True:
                                            try:
                                                member_name = myresulte[0][1]
                                                SenderAddress = "" # Here Enter Senders Email address
                                                passwrd1  = 'kjmzlppyullangls'
                                                server = smtplib.SMTP('smtp.gmail.com',587)
                                                server.starttls()
                                                server.login(SenderAddress,passwrd1)
                                                msg = 'Dear ' + str(member_name) +',\nYour Order of the book is Successfully Cancelled... \nRegards \nThankyou'
                                                subject = 'Order Cancellation information'
                                                body = 'subject:{}\n\n{}'.format(subject,msg)
                                                server.sendmail(SenderAddress,email_id,body)
                                                server.quit() 
                                                break
                                            except:
                                                print('No Internet connection try again...')  
                                                at = input('Press Enter to try again.. ')
                                        mycursor.execute('Delete From order_book where book_id = '+bi+' and member_id = '+str(mi))
                                        mydb.commit()
                                        print('Order Cancelled Successfully')     
                        elif oinput == '4':
                            q=pd.read_sql('select * from '+ 'order_book',mydb)
                            print(q)
                            kk = input('Press enter for main menu:')
                    elif chooice1 == '7':
                        ai = input('Enter Member ID:')
                        q=pd.read_sql('select * from members_instance where member_id ='+ai,mydb)
                        print(q)
                        ok = input('Press Enter for main menu:')
                    elif chooice1 == '8':
                        print('1.Membership')
                        print('2.Total Issue')
                        print('3.Total Return')
                        print('4.Total Panalty')

                        cav = input('Enter your choice:')
                        if cav == '1':
                            print('Please select X-axis')
                            print('1.Member ID')
                            print('2.Member name')
                            print('3.Date of joining')
                            xa = input('Enter Your Choice:')
                            print('Please Select Y-axis')
                            print('1.Age')
                            print('2.Fees Submit')
                            xa1 = input('Enter your Choice:')
                            if xa == '1' and xa1 == '1':
                                xaxis = []
                                yaxis = []
                                mycursor.execute('Select member_id from membership')
                                vmi = mycursor.fetchall()
                                for row in vmi:
                                    xaxis.append(row[0])
                                mycursor.execute('Select age from membership')
                                vage = mycursor.fetchall()
                                for row in vage:
                                    yaxis.append(row[0])
                                fig = plt.figure(figsize = (10, 5)) 
                                plt.bar(xaxis, yaxis, color ='Red', edgecolor = 'Black',width = 0.2) 
                                plt.xlabel("Members ID") 
                                plt.ylabel("Members Age") 
                                plt.title("Relationship Between Members Id and Members Age") 
                                plt.show() 
                            elif xa == '1' and xa1 == '2':
                                xaxis = []
                                yaxis = []
                                mycursor.execute('Select member_id from membership')
                                vmi = mycursor.fetchall()
                                for row in vmi:
                                    xaxis.append(row[0])
                                mycursor.execute('Select fee_submit from membership')
                                vage = mycursor.fetchall()
                                for row in vage:
                                    yaxis.append(row[0])
                                fig = plt.figure(figsize = (10, 5)) 
                                plt.bar(xaxis, yaxis, color ='Red', edgecolor = 'Black', width = 0.2) 
                                plt.xlabel("Members ID") 
                                plt.ylabel("Members Fees Submit") 
                                plt.title("Relationship Between Members Id and Members Fees Submit") 
                                plt.show() 
                            elif xa == '2' and xa1 == '1':
                                xaxis = []
                                yaxis = []
                                mycursor.execute('Select member_name from membership')
                                vmi = mycursor.fetchall()
                                for row in vmi:
                                    xaxis.append(row[0])
                                mycursor.execute('Select age from membership')
                                vage = mycursor.fetchall()
                                for row in vage:
                                    yaxis.append(row[0])
                                fig = plt.figure(figsize = (10, 5)) 
                                plt.bar(xaxis, yaxis, color ='Red', edgecolor = 'Black', width = 0.2) 
                                plt.xlabel("Members Name") 
                                plt.ylabel("Members Age") 
                                plt.title("Relationship Between Members Name and Members Age") 
                                plt.show() 
                            elif xa == '2' and xa1 == '2':
                                xaxis = []
                                yaxis = []
                                mycursor.execute('Select member_name from membership')
                                vmi = mycursor.fetchall()
                                for row in vmi:
                                    xaxis.append(row[0])
                                mycursor.execute('Select fee_submit from membership')
                                vage = mycursor.fetchall()
                                for row in vage:
                                    yaxis.append(row[0])
                                fig = plt.figure(figsize = (10, 5)) 
                                plt.bar(xaxis, yaxis, color ='Red', edgecolor = 'Black', width = 0.2) 
                                plt.xlabel("Members Name") 
                                plt.ylabel("Members Fees Submit") 
                                plt.title("Relationship Between Members Name and Members Fees Submit") 
                                plt.show() 
                            elif xa == '3' and xa1 == '1':
                                xaxis = []
                                yaxis = []
                                mycursor.execute('Select date_of_joining from membership')
                                vmi = mycursor.fetchall()
                                for row in vmi:
                                    xaxis.append(str(row[0]))
                                mycursor.execute('Select age from membership')
                                vage = mycursor.fetchall()
                                for row in vage:
                                    yaxis.append(row[0])
                                fig = plt.figure(figsize = (10, 5)) 
                                plt.bar(xaxis, yaxis, color ='Red', edgecolor = 'Black', width = 0.1) 
                                plt.xlabel("Date of Joining") 
                                plt.ylabel("Members Age") 
                                plt.title("Relationship Between Date of Joining and Members Age") 
                                plt.show() 
                            elif xa == '3' and xa1 == '2':
                                xaxis = []
                                yaxis = []
                                mycursor.execute('Select date_of_joining from membership')
                                vmi = mycursor.fetchall()
                                for row in vmi:
                                    xaxis.append(str(row[0]))
                                mycursor.execute('Select fee_submit from membership')
                                vage = mycursor.fetchall()
                                for row in vage:
                                    yaxis.append(row[0])
                                fig = plt.figure(figsize = (10, 5)) 
                                plt.bar(xaxis, yaxis, color ='Red', edgecolor = 'Black', width = 0.2) 
                                plt.xlabel("Date Of Joining") 
                                plt.ylabel("Members Fees Submit") 
                                plt.title("Relationship Between Members Date Of Joining and Members Fees Submit") 
                                plt.show() 
                        elif cav == '2':
                            print('Please select X-axis')
                            print('1.Member ID')
                            print('2.Member name')
                            xa = input('Enter Your Choice:')
                            print('You Dont have to select Y-axis it is by default Total no of book issued..')
                            if xa == '1':
                                xaxis = []
                                yaxis = []
                                mycursor.execute('Select member_id from members_instance')
                                vmi = mycursor.fetchall()
                                for row in vmi:
                                    xaxis.append(row[0])
                                mycursor.execute('Select no_of_books_issues from members_instance')
                                vage = mycursor.fetchall()
                                for row in vage:
                                    yaxis.append(int(row[0]))
                                fig = plt.figure(figsize = (10, 5)) 
                                plt.bar(xaxis, yaxis, color ='Red', edgecolor = 'Black', width = 0.2) 
                                plt.xlabel("Members ID") 
                                plt.ylabel("Total No books Issued") 
                                plt.title("Relationship Between Members Id and Total No books Issued") 
                                plt.show() 
                            elif xa == '2':
                                xaxis = []
                                yaxis = []
                                mycursor.execute('Select member_name from members_instance')
                                vmi = mycursor.fetchall()
                                for row in vmi:
                                    xaxis.append(row[0])
                                mycursor.execute('Select no_of_books_issues from members_instance')
                                vage = mycursor.fetchall()
                                for row in vage:
                                    yaxis.append(int(row[0]))
                                fig = plt.figure(figsize = (10, 5)) 
                                plt.bar(xaxis, yaxis, color ='Red', edgecolor = 'Black', width = 0.2) 
                                plt.xlabel("Members Name") 
                                plt.ylabel("Total No books Issued") 
                                plt.title("Relationship Between Members Name and Total No books Issued") 
                                plt.show()
                        elif cav == '3':
                            print('Please select X-axis')
                            print('1.Member ID')
                            print('2.Member name')
                            xa = input('Enter Your Choice:')
                            print('You Dont have to select Y-axis it is by default Total no of books Returned..')
                            if xa == '1':
                                xaxis = []
                                yaxis = []
                                mycursor.execute('Select member_id from members_instance')
                                vmi = mycursor.fetchall()
                                for row in vmi:
                                    xaxis.append(row[0])
                                mycursor.execute('Select no_of_books_returned from members_instance')
                                vage = mycursor.fetchall()
                                for row in vage:
                                    yaxis.append(int(row[0]))
                                fig = plt.figure(figsize = (10, 5)) 
                                plt.bar(xaxis, yaxis, color ='Red', edgecolor = 'Black', width = 0.2) 
                                plt.xlabel("Members ID") 
                                plt.ylabel("Total No books Returned") 
                                plt.title("Relationship Between Members Id and Total No books Returned") 
                                plt.show() 
                            elif xa == '2':
                                xaxis = []
                                yaxis = []
                                mycursor.execute('Select member_name from members_instance')
                                vmi = mycursor.fetchall()
                                for row in vmi:
                                    xaxis.append(row[0])
                                mycursor.execute('Select no_of_books_returned from members_instance')
                                vage = mycursor.fetchall()
                                for row in vage:
                                    yaxis.append(int(row[0]))
                                fig = plt.figure(figsize = (10, 5)) 
                                plt.bar(xaxis, yaxis, color ='Red', edgecolor = 'Black', width = 0.2) 
                                plt.xlabel("Members Name") 
                                plt.ylabel("Total No books Returned") 
                                plt.title("Relationship Between Members Name and Total No books Returned") 
                                plt.show()
                        elif cav == '4':
                            print('Please select X-axis')
                            print('1.Member ID')
                            print('2.Member name')
                            xa = input('Enter Your Choice:')
                            print('You Dont have to select Y-axis it is by default Total Pananlty Paid by Members')
                            if xa == '1':
                                xaxis = []
                                yaxis = []
                                mycursor.execute('Select member_id from members_instance')
                                vmi = mycursor.fetchall()
                                for row in vmi:
                                    xaxis.append(row[0])
                                mycursor.execute('Select total_penalty from members_instance')
                                vage = mycursor.fetchall()
                                for row in vage:
                                    yaxis.append(int(row[0]))
                                fig = plt.figure(figsize = (10, 5)) 
                                plt.bar(xaxis, yaxis, color ='Red', edgecolor = 'Black', width = 0.2) 
                                plt.xlabel("Members ID") 
                                plt.ylabel("Total Penalty") 
                                plt.title("Relationship Between Members Id and Total Total Penalty Paid by Members") 
                                plt.show() 
                            elif xa == '2':
                                xaxis = []
                                yaxis = []
                                mycursor.execute('Select member_name from members_instance')
                                vmi = mycursor.fetchall()
                                for row in vmi:
                                    xaxis.append(row[0])
                                mycursor.execute('Select total_penalty from members_instance')
                                vage = mycursor.fetchall()
                                for row in vage:
                                    yaxis.append(int(row[0]))
                                fig = plt.figure(figsize = (10, 5)) 
                                plt.bar(xaxis, yaxis, color ='Red', edgecolor = 'Black', width = 0.2) 
                                plt.xlabel("Members Name") 
                                plt.ylabel("Total No books Returned") 
                                plt.title("Relationship Between Members Name and Total Penalty Paid by Members") 
                                plt.show()
                                
                    else:
                        print('Your Choice is not Valid Please Try Again...')      

        elif a == 'developer' and b == 'oooo':
            mydb=dbc.connect(host='localhost',user='root')
            mycursor=mydb.cursor()
            mycursor.execute('create database if not exists library')
            mydb=dbc.connect(host='localhost',user='root',database=' library ')
            mycursor=mydb.cursor()
            mycursor.execute('''create table if not exists BooksDetails(book_id varchar(10) not null primary key,book_name varchar(30) not null,category varchar(10),quantity int(3),total_page int(5),publisher varchar(30),edition varchar(15),book_cost decimal(6,2) not null)''')
            mycursor.execute('create table if not exists membership(member_id varchar(10) not null primary key,member_name varchar(30) not null,phone_number char(10),email_id varchar(30),age int(2),date_of_joining date,last_date date,address varchar(30),fee_submit decimal(6,2))')
            mycursor.execute('create table if not exists issue_records(member_id varchar(10) not null ,book_id  varchar(10) not null,book_name varchar(18),publisher varchar(20),member_name varchar(30),issue_date date,last_date date,address varchar(30),penalty int(5),foreign key(member_id) references membership(member_id))')
            mycursor.execute('create table if not exists returned_records(member_id varchar(10) not null,book_id varchar(10) not null,book_name varchar(18),publisher varchar(20),member_name varchar(30),issue_date date,last_date date,address varchar(30),foreign key(member_id) references membership(member_id))')
            mycursor.execute('create table if not exists members_instance(member_id varchar(10) not null,no_of_books_issues varchar(10) not null DEFAULT "0",total_penalty varchar(10) not null DEFAULT "0",member_name varchar(20),joining_date date,valid_last_date date,address varchar(30),no_of_books_returned varchar(10) not null DEFAULT "0")')
            mycursor.execute('create table if not exists daily_record(person_name varchar(20),phone_number char(10),email_id varchar(20),occupation varchar(8),address varchar(20),dates date)')
            mycursor.execute('create table if not exists order_book(book_name varchar(20),book_id varchar(10), publisher varchar(20),payment_status varchar(5),member_id varchar(20),price varchar(10),Date_of_order date,member_name varchar(20),Date_of_delivery date)')
            print('Database and Tables Created successfully now to can run the program..')
        elif a != 'admin' or b != '1234':   
            print('Sorry username or password is not correct')
            continue   
        break
    except:
        print('Warning...')
        print("Developer is not established program yet in your system please contact with developer to run this program.You cannot run Program without the permission of developer.If you not contact with developer and run again and again your system may damaged.So please don't to this contact with developer as much as possible..")
        print('Thankyou')