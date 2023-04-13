from tkinter import *
w= Tk()
w.geometry('300x200')

user=StringVar()
p_ass=StringVar()

def submit():
    u=user.get()
    p=p_ass.get()

    print(u)
    print(p)

lbl=Label(text='UserName',border=5,font='bold')
lbl.grid(row=0,column=0)

en=Entry(w,width=30,textvariable=user)
en.grid(row=0,column=1)


lbl2=Label(text='Password',border=5,font='bold')
lbl2.grid(row=3,column=0)

en=Entry(w,width=30,show='*',textvariable=p_ass)
en.grid(row=3,column=1)

btn=Button(w,text='submit',font='bold',command=submit)
btn.grid(row=5,column=1)
w.mainloop()
