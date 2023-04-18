from tkinter import *
from math import *
w = Tk()
w.geometry('314x415')
w.title('Calculator')
w.iconbitmap('icon.ico')

input_value=""
d_text=StringVar()

def click_btn(item):
    global input_value
    input_value+=str(item)
    d_text.set(input_value)

def clear_btn():
    global input_value
    input_value=""
    d_text.set(input_value)

def equal_btn():
    global input_value
    rlt=str(eval(input_value))
    d_text.set(rlt)
    input_value=rlt

def sqt():
    global input_value
    rst=sqrt(int(input_value))
    d_text.set(rst)
    input_value=str(rst)

def c_one(item):
    global input_value
    c=item[:-1]
    d_text.set(c)
    input_value=c

txt=Entry(w,font=' lucida 15 bold',textvariable=d_text)
txt.grid(row=0,column=0,sticky='n',columnspan=4,padx=5,pady=5,ipady=30,ipadx=38)


bton=Button(w,text='AC',fg='orange',font=' lucida 10 bold',command=clear_btn)
bton.grid(column=0,row=1,sticky='w',ipadx=15,ipady=15,padx=3)

bton=Button(w,text= 'x',fg='orange',font=' lucida 10 bold',command=lambda:c_one(input_value))
bton.grid(column=1,row=1,sticky='w',ipadx=20,ipady=15,padx=3)

bton=Button(w,text='%',fg='orange',font=' lucida 10 bold',command=lambda:click_btn('%'))
bton.grid(column=2,row=1,sticky='w',ipadx=20,ipady=15,padx=3)

bton=Button(w,text='÷',font=' lucida 10 bold',fg='orange',command=lambda:click_btn('÷'))
bton.grid(column=3,row=1,sticky='w',ipadx=22,ipady=15,padx=3)

bton=Button(w,text='7',font=' lucida 10 bold',command=lambda:click_btn(7))
bton.grid(column=0,row=2,sticky='w',ipadx=20,ipady=15,padx=3,pady=3)

bton=Button(w,text='8',font=' lucida 10 bold',command=lambda:click_btn(8))
bton.grid(column=1,row=2,sticky='w',ipadx=20,ipady=15,padx=3,pady=3)

bton=Button(w,text='9',font=' lucida 10 bold',command=lambda:click_btn(9))
bton.grid(column=2,row=2,sticky='w',ipadx=20,ipady=15,padx=3,pady=3)

bton=Button(w,text='X',font=' lucida 10 bold',command=lambda:click_btn('X'))
bton.grid(column=3,row=2,sticky='w',ipadx=20,ipady=15,padx=3,pady=3)

bton=Button(w,text='4',font=' lucida 10 bold',command=lambda:click_btn(4))
bton.grid(column=0,row=3,sticky='w',ipadx=20,ipady=15,padx=3,pady=3)

bton=Button(w,text='5',font=' lucida 10 bold',command=lambda:click_btn(5))
bton.grid(column=1,row=3,sticky='w',ipadx=20,ipady=15,padx=3,pady=3)

bton=Button(w,text='6',font=' lucida 10 bold',command=lambda:click_btn(6))
bton.grid(column=2,row=3,sticky='w',ipadx=20,ipady=15,padx=3,pady=3)

bton=Button(w,text='-',font=' lucida 10 bold',fg='orange',command=lambda:click_btn('-'))
bton.grid(column=3,row=3,sticky='w',ipadx=22,ipady=15,padx=3,pady=3)

bton=Button(w,text='1',font=' lucida 10 bold',command=lambda:click_btn(1))
bton.grid(column=0,row=4,sticky='w',ipadx=20,ipady=15,padx=3,pady=3)

bton=Button(w,text='2',font=' lucida 10 bold',command=lambda:click_btn(2))
bton.grid(column=1,row=4,sticky='w',ipadx=20,ipady=15,padx=3,pady=3)

bton=Button(w,text='3',font=' lucida 10 bold',command=lambda:click_btn(3))
bton.grid(column=2,row=4,sticky='w',ipadx=20,ipady=15,padx=3,pady=3)

bton=Button(w,text='+',font=' lucida 10 bold',fg='orange',command=lambda:click_btn('+'))
bton.grid(column=3,row=4,sticky='w',ipadx=20,ipady=15,padx=3,pady=3)

bton=Button(w,text='√ ',font=' lucida 10 bold',fg='orange',command=sqt)
bton.grid(column=0,row=5,sticky='w',ipadx=20,ipady=15,padx=3,pady=3)

bton=Button(w,text='0',font=' lucida 10 bold',command=lambda:click_btn(0))
bton.grid(column=1,row=5,sticky='w',ipadx=20,ipady=15,padx=3,pady=3)

bton=Button(w,text='.',font=' lucida 10 bold',command=lambda:click_btn('.'))
bton.grid(column=2,row=5,sticky='w',ipadx=20,ipady=15,padx=3,pady=3)

bton=Button(w,text='=',font=' lucida 10 bold',fg='orange',command=equal_btn)
bton.grid(column=3,row=5,sticky='w',ipadx=20,ipady=15,padx=3,pady=3)





w.mainloop()