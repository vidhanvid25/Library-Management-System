def addbook(cursor,database):
    bid=input("Book ID: ")
    name=input("Name of book: ")
    author=input("Author Name: ")
    qt=input("Quantity: ")
    rate=input("Rate: ")
    cursor.execute("INSERT INTO admin VALUES('%s','%s','%s','%s','%s')"%(bid,name,author,qt,rate))
    database.commit()
    print('Record Added')
    print()

def booksearch(cursor,search):
    cursor.execute("SELECT * FROM admin WHERE BookName='%s'"%(search,))
    myrec=cursor.fetchone()
    return myrec

def deletebook(cursor):
    delete=input("Book to be Deleted: ")
    try:
        cursor.execute("DELETE FROM admin WHERE BookName='%s'"%(delete,))
        print("Successfully Deleted")
    except:
        print('No Book found')
    print()

def display(cursor,table):
    if table=='admin':
        cursor.execute("SELECT * FROM admin")
    else:
        cursor.execute("SELECT * FROM student")
    rec=cursor.fetchall()
    for x in rec:
        print(x)
    print()
        
def displayissues(cursor):
    name=input("Student Name: ")
    try:
        cursor.execute("SELECT * FROM student WHERE StudentName='%s'"%(name,))
        print()
    except:
        print("Invalid name entered")
    rec=cursor.fetchall()
    for x in rec:
        print(x)
    print()

def issuebook(cursor,database):
    bnm=input("Book to be issued: ")
    myrec=booksearch(cursor,bnm)
    bqt=int(myrec[3])
    ind1=myrec[0]
    try:
        cursor.execute("SELECT COUNT(*) FROM student WHERE BookID='%s' AND Status='%s'"%(ind1,'Issued'))
        tup=cursor.fetchone()
        ct=tup[0]
        if ct<bqt:
            snm=input("Your Name: ")
            pno=input("Phone Number: ")
            date=input('Issue Date in yyyy/mm/dd: ')
            cursor.execute("INSERT INTO student VALUES('%s','%s','%s','%s',NULL,'%s')"%(ind1,snm,pno,date,'Issued'))
            database.commit()
            print("Issued Successfully")
        else:
            print("Book Not Available")
    except:
        print("No book Available")
    print()

def returnbook(cursor,database):
    bnm=input("Book to be Returned: ")
    myrec=booksearch(cursor,bnm)
    ind1=myrec[0]
    snm=input("Student Name: ")
    date=input('Return Date in yyyy/mm/dd: ')
    data=(date,'Returned',ind1,snm,)
    query="UPDATE student SET DateOfReturn=%s, Status=%s WHERE BookID=%s AND StudentName=%s"
    try:
        cursor.execute(query,data)
    except:
        print("No such record")
    database.commit()
    print('Book Returned')
    print()

