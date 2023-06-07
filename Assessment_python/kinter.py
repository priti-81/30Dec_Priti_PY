from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector

# mysql part
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='tkinter')
    print('Database connected.. ')
    cur=mydb.cursor()
except Exception as e:
    print(e)

""" create_tbl="create table registeruser (id integer primary key auto_increment, Name varchar(20),contact int(10),Email varchar(20), Gender varchar(10),city varchar(10),state varchar(10))"

try:
    cur.execute(create_tbl)
    print('table created successfully...')

except Exception as e:
    print(e)
 """

# tkinter project part
w = Tk()
w.geometry('400x400')
w.resizable(width=False,height=False)
# w.minsize(400, 500)
# w.maxsize(400, 500)
w.title('Registeration Form')

Label(w,bg='orange',fg='black',text='Please enter details below',font='arial 10 bold',width=50).grid(row=0,column=0,columnspan=4,pady=5)

name=StringVar()
town=StringVar()
state=StringVar()
contact=StringVar()
email=StringVar()
btn1=IntVar()



def submit():
    n=name.get()
    c=town.get()
    s=state.get()
    t=contact.get()
    e=email.get()
    f=btn1.get()
    p=[n,c,s,t,e,f]
    if  f == 1:
        output="male"
    else:
        output="female"

    if "" in p:
             messagebox.showerror("error!", "please! fill all the details")  
    else:
            messagebox.showinfo("Success..", "your registration done successfully..") 
            w.quit()
    insert_data=f"insert into registeruser(Name,contact,Email,Gender,city,state) values('{n}','{t}','{e}','{output}','{c}','{s}')"
    try:
        cur.execute(insert_data)
        mydb.commit()
        print('Record inserted successfully..')
    except Exception as ex:
        print(ex)
        
    # return print(f'{n},{c},{e},{t},{s},{output}')

def validation1():
    try:
        if name.get().isdigit():
            messagebox.showerror("error!", "only alphabets allow")
    except Exception as ep:
        messagebox.showerror('error',ep)
    return TRUE

    
def validation2():

    try:
        if '@'not in email.get() :
              messagebox.showerror("error!", "please! write proper email")  
        elif "" in e:
             messagebox.showerror("error!", "please! fill all the details")  
    except Exception as ep:
        messagebox.showerror('error',ep)
    return TRUE

    




Label(w,text='Name*',font='arial 13 ').grid(row=1,column=0,pady=5)
Entry(w,width=27,font=10,relief=GROOVE,textvariable=name,validate='focusout',validatecommand=validation1).grid(row=1,column=1,pady=3,columnspan=2)

Label(w,text='Contact*',font='arial 13 ').grid(row=2,column=0,pady=5)
Entry(w,width=27,font=10,relief=GROOVE,textvariable=contact).grid(row=2,column=1,pady=3,columnspan=2)

Label(w,text='Email*',font='arial 13 ').grid(row=3,column=0,pady=5)
Entry(w,width=27,font=10,relief=GROOVE,textvariable=email,validate='focusout',validatecommand=validation2).grid(row=3,column=1,pady=3,columnspan=2)


Label(w,text='Gender*',font='arial 13 ').grid(row=4,column=0,)
Radiobutton(w,text='Male',variable=btn1,value=1,font=10,).grid(row=4,column=1,columnspan=2,sticky=W)
Radiobutton(w,text='Female',variable=btn1,value=2,font=10,).grid(row=4,column=1,sticky=E)

city=['Ahmedabad','Rajkot','Surat','Baroda','Jamnagar','other']

Label(w,text='City*',font='arial 13 ').grid(row=5,column=0,pady=5)
ttk.Combobox(w,values=city,width=37,textvariable=town).grid(row=5,column=1,pady=3,columnspan=2)

Label(w,text='State*',font='arial 13 ').grid(row=6,column=0,pady=5)
ttk.Combobox(w,values=city,width=37,textvariable=state).grid(row=6,column=1,pady=3,columnspan=2)

Button(w,command=submit,text='Register',fg='white',bg='blue',width=20,font='arial 10 bold',relief='raised').grid(row=7,column=1,pady=60,columnspan=1)

w.mainloop()

