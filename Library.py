import mysql.connector  
import module
mydb=mysql.connector.connect(host='localhost', user='root', password='XXXXXX')#Password of MySQL
mycursor=mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE library")
except:
    pass

mydb2=mysql.connector.connect(host='localhost', user='root', password='XXXXXXX', database='library')#Password of MySQL
mycursor2=mydb2.cursor()
try:
    mycursor2.execute("""CREATE TABLE admin
                        (BookID integer(4) NOT NULL PRIMARY KEY,
                        BookName varchar(25) NOT NULL,
                        BookAuthor varchar(40),
                        Quantity integer(2),
                        Rate integer)""")
    mycursor2.execute("""CREATE TABLE student
                        (BookID integer(4) NOT NULL,
                        StudentName varchar(25) NOT NULL,
                        PhoneNo numeric(10,0),
                        DateOfIssue date,
                        DateOfReturn date,
                        Status varchar(10))""")
except:
    pass

while True:
    print('1. Admin')
    print('2. Student')
    print('3.To quit')
    a=int(input('Enter User:'))
    print()
    if a==1:
        print('Logged in as Admin')
        print('1. To Add Books')
        print('2. Book Search')
        print('3. Delete Book')
        print('4. Display All Books')
        print('5. Display Issues')
        print('6.To Exit')
        while True:
            b=int(input("Enter Choice:"))
            print()
            if b==1:
                module.addbook(mycursor2,mydb2)
            elif b==2:
                search=input("Book to be Searched: ")
                myrec=module.booksearch(mycursor2,search)
                if myrec!=None:
                    print(myrec)
                else:
                    print("No book found!")
            elif b==3:
                module.deletebook(mycursor2)
            elif b==4:
                tablename='admin'
                module.display(mycursor2,tablename)
            elif b==5:
                tablename='student'
                module.display(mycursor2,tablename)
            elif b==6:
                break
            else:
                print("Invalid Choice!")
    elif a==2:
        print('Logged in as Student')
        print('1. Book Search')
        print('2. Issue Book')
        print('3. Return book')
        print('4. Display Student Issues')
        print('5. To Exit')
        while True:
            c=int(input("Enter Choice: "))
            print()
            if c==1:
                search=input("Book to be Searched: ")
                print(module.booksearch(mycursor2,search))
            elif c==2:
                module.issuebook(mycursor2,mydb2)
            elif c==3:
                module.returnbook(mycursor2,mydb2)
            elif c==4:
                module.displayissues(mycursor2)
            elif c==5:
                break
            else:
                print("Invalid choice")
    elif a==3:
        break
    else:
        pass
