from tkinter import *
from math import *
w = Tk()
w.geometry('350x600')
w.title('Calculator')
w.iconbitmap('D:/icon-1.ico')

scvalue=StringVar()
input_v=''

# function for key events

def key_press(event):   
    try:
        scvalue.set(eval(scvalue.get()))
    except:
        scvalue.set('Error')
   
        
# function for Button event
def click(event):
    global input_v
    text=event.widget.cget('text')

    
    if text=='=':
        try:
            value=str(eval(input_v))
            scvalue.set(value)
        except:
            value='Error'
            scvalue.set(value)
            input_v=''

    elif text=='AC':
        input_v=''
        scvalue.set('')

    elif text=='x':
        c=input_v[:-1]
        scvalue.set(c)
        input_v=c

    elif text=='√': 
        try:
            rst=sqrt(int(input_v))
            scvalue.set(rst)
            input_v=str(rst)
        except:
            value='Error'
            scvalue.set(value)
            input_v=''

    
    elif text=='÷' :
            text='/'
            input_v+=str(text)
            scvalue.set(input_v)
            
            
    elif text=='X':
            text='*'
            input_v+=str(text)
            scvalue.set(input_v)

    else:
            input_v+=str(text)
            scvalue.set(input_v)


btn=[('AC','x','%','÷'),(7,8,9,'X'),(4,5,6,'-'),(1,2,3,'+'),('√',0,'.','=')]
f=Frame(w,bg='gray')
screen=Entry(f,textvariable=scvalue,font='serif 30 bold',relief=RAISED,highlightthickness=10)
screen.pack(fill=X,padx=8,pady=10,ipady=10)

#screen.focus()

screen.bind('<Return>',key_press)
f.pack(fill='both',expand=True)


for i1 in btn:
    f=Frame(w,bg='gray',relief=RAISED)
    for i in i1:
        if i=='AC':
            b=Button(f,text=i,width=4,height=2,font='serif 20 bold',relief=RAISED,bg='Red',fg='white')
            b.pack(side=LEFT,padx=5,pady=5,fill=BOTH,expand=True)
            b.bind('<Button-1>',click)
            f.pack(fill=BOTH,expand=True)
        
        elif i in  ['x' ,'%' , 'X' ,'÷', '-' , '+' , '√' , '.' , '=',]:
            b=Button(f,text=i,width=4,height=2,font='serif 20 bold',relief=RAISED,bg='Blue',fg='white')
            b.pack(side=LEFT,padx=5,pady=5,fill=BOTH,expand=True)
            b.bind('<Button-1>',click)
            f.pack(fill=BOTH,expand=True)

        else:
            b=Button(f,text=i,width=4,height=2,font='serif 20 bold',relief=RAISED,bg='Black',fg='white')
            b.pack(side=LEFT,padx=5,pady=5,fill=BOTH,expand=True)
            b.bind('<Button-1>',click)
            f.pack(fill=BOTH,expand=True)


w.mainloop()
