import mysql.connector

print('press 1 for Insert record in Database')
print('press 3 for update record in Database')
print('press 9 for delete record in Database')
print('press 4 for show record in Database')
print('press 5 for Exit')


try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='python')
    print('Database connected.. ')
    cur=mydb.cursor()
except Exception as e:
    print(e)

#tbl_name=input('enter taable name: ')
    
create_tbl="create table Book (id integer primary key auto_increment,BookAuthor varchar(20),BookTitle text)"
    
try:
    cur.execute(create_tbl)
    print('table created successfully...')

except Exception as e:
    print(e)

def insert_tbl():
    c=input('Enter BookAuthor name: ')
    d=input('Enter Booktitle Name: ')


    insert_data=f"insert into Book(BookAuthor,BookTitle) values('{c}','{d}')"
    try:
        cur.execute(insert_data)
        mydb.commit()
        print('Record inserted successfully..')
    except Exception as e:
        print(e)
        
def update_data():
    n=input('enter new BookAuthor: ')
    n2=input('enter new BookTitle: ')
    n3=input('enter id: ')
    data=f"update Book set BookAuthor='{n}',BookTitle='{n2}' where id='{n3}'"
    try:
        cur.execute(data)
        mydb.commit()
        print('data updataed...')
    except Exception as e:
        print(e)

def delete_data():
    d=input('Enter id no u want to delete: ')
    try:
        data1=f"delete from Book where id= '{d}'"
        cur.execute(data1)
        mydb.commit()
        print('data deleted..')
    except Exception as e:
        print(e)

def show_data(): 
    t='select * from Book '
    try:
        cur.execute(t)
        t1=input('print y if u fetch all data: ')
        if t1=='y':
            print(cur.fetchall())
        else:
           t2=int(input('enter no of line: '))
           print(cur.fetchmany(t2))
    except Exception as e:
        print(e)

        
for i in range(5):
    a=int(input('enter your choice: '))
    if a==1:
        insert_tbl()
    elif a==3:
        update_data()
    elif a==4:
        show_data()
    elif a==9:
        delete_data()
    elif a==5:
        exit()
    

