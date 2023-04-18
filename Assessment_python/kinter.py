from tkinter import *
from tkinter import ttk
w = Tk()
w.geometry('400x400')
w.resizable(width=False,height=False)
# w.minsize(400, 500)
# w.maxsize(400, 500)
w.title('Registeration Form')

Label(w,bg='orange',fg='black',text='Please enter details below',font='arial 10 bold',width=50).grid(row=0,column=0,columnspan=4,pady=5)


t=['Name*','Contact*','Email*']
for i in range(3):
    Label(w,text=t[i],font='arial 13 ').grid(row=i+1,column=0,pady=5)
    Entry(w,width=27,font=10,relief=GROOVE).grid(row=i+1,column=1,pady=3,columnspan=2)


Label(w,text='Gender*',font='arial 13 ').grid(row=4,column=0,)
Radiobutton(w,text='Male',value=1,font=10).grid(row=4,column=1,columnspan=2,sticky=W)
Radiobutton(w,text='Female',value=2,font=10).grid(row=4,column=1,sticky=E)

city=['Ahmedabad','Rajkot','Surat','Baroda','Jamnagar']

Label(w,text='City*',font='arial 13 ').grid(row=5,column=0,pady=5)
ttk.Combobox(w,values=city,width=37).grid(row=5,column=1,pady=3,columnspan=2)

Label(w,text='State*',font='arial 13 ').grid(row=6,column=0,pady=5)
ttk.Combobox(w,values=city,width=37).grid(row=6,column=1,pady=3,columnspan=2)

Button(w,text='Register',fg='white',bg='blue',width=20,font='arial 10 bold',relief='raised').grid(row=7,column=1,pady=60,columnspan=1)

w.mainloop()

