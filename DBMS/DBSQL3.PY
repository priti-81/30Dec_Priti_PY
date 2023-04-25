import sqlite3
try:
    con=sqlite3.connect('python.db')
    print('database connected!')
except Exception as e:
    print(e)

# create table
create_tbl='create table studinfo (id integer primary key autoincrement,name text,subject text)'
try:
    con.execute(create_tbl)
    print('table created successfully..')
except Exception as e:
    print(e)

#insert data
insert_data="insert into studinfo(name,subject) values('priti','python'),('niki','c#'),('kush','java'),('suman','ruby')"

try:
    con.execute(insert_data)
    con.commit()
    print('data inserted successfully')

except Exception as e:
    print(e)

#data update
update_data="update studinfo set name= 'krish' where id=3"
try:
    con.execute(update_data)
    con.commit()
    print('record updated')
except Exception as e:
    print(e)

 #delete data
delete_data="delete from studinfo where id=4"
try:
    con.execute(delete_data)
    con.commit()
    print('record deleted')

except Exception as e:
    print(e)

""" drop_tbl="drop table studinfo"
try:
    con.execute(drop_tbl)
    con.commit()
    print('table data deleted..')
except Exception as e:
    print(e) """

# show data
cur=con.cursor()
select_data="select * from studinfo"
try:
    cur.execute(select_data)
    con.commit()
    print(cur.fetchall())
    #print(cur.fetchmany(2))
    #print(cur.fetchone())

    # for i in cur.fetchall():
        #print(i)

except Exception as e:
    print(e)