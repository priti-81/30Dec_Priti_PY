import pymysql
try:
    con=pymysql.connect(host='localhost',user='root',password='',database='Python')
    print('database connected..')
except Exception as e:
    print(e)

cur=con.cursor()
# create table
""" create_tbl='create table product(id integer primary key auto_increment,productname text,productprice integer)'
alter_tbl='alter table product auto_increment=101'
try:
    cur.execute(create_tbl)
    cur.execute(alter_tbl)
    print('table created and alter successfully..')
except Exception as e:
    print(e) """

""" # insert data
insert_data="insert into product (productname,productprice) values ('Parle-g',125),('Goodday',170),('Marigold',140),('Oreo',225)"
try:
    cur.execute(insert_data)
    con.commit()
    print('data inserted successfully..')
except Exception as e:
    print(e)

#update data
update_data='update product set productprice=130 where id=101'
try:
    cur.execute(update_data)
    con.commit()
    print('record updated successfully')
except Exception as e:
    print(e)

#alter data
alter_data='alter table product add column productquantity text'
try:
    cur.execute(alter_data)
    con.commit()
    print('one column add successfully')
except Exception as e:
    print(e)
 """
# insert data in new column
insert_data= 'insert into product where id=105,106,107, 108 values=1,2,3,4' 
try:
    cur.execute(insert_data)
    con.commit()
    print('record inserted in new column')
except Exception as e:
    print(e)