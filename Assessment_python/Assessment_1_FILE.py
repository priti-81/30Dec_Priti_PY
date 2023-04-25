def prent():
    print('Welcome to  Python E - Note\n')
    print('Press 1 for generate Note')
    print('Press 2 for view Note')
    print('Press 4 for exit\n')

import re,string,datetime
e=datetime.datetime.now()
a,b,c='','',''


def generate_note():
            global a,b,c
            for b in range(5):
                a=input('Enter python E-note generator name: ').lower()
                sto=any(a1 in a for a1 in string.punctuation)
                sto1=re.findall('\d',a)
            
                if sto==True:   
                    print('Error:Invalid input "punctuation not allowed"')
                elif bool(sto1)==False:
                    break
                else:
                    print('Error:Invalid input "digits not allowed"')

            b=input('Enter Python E-note title: ')

            c=input('Enter E-note content:')

            if input('Do you want to make more notes ?(y/n)')=='y':
                generate_note()
            else:
                print('\nYour note generated successfully...')

            with open('log1.txt','a')  as   f: 
                f.write('--------------------------------------------------------------------------\n')
                f.write(e.strftime("%d-%m-%Y %I:%M:%S %p \n"))
                f.write(f'Enter python E-note generator name:{a}\n')  
                f.write(f'Enter Python E-note title:{b}\n')
                f.write(f'\t\tEnter E-note content:{c}\n')


def view_note(a,b,c):
        print(f'Enter python E-note generator name:{a}')
        print(f'Enter python E-note title:{b}')
        print(f'Enter python E-note content:{c}')
            
        
def choice():
    for i in range(6):
        x=int(input('Enter your choice: '))    
        if x==1:
            generate_note()
        elif x==2:
            if a=='':
                print('Please Generate note first..')
            else:
                view_note(a,b,c)
        elif x==4:
            exit()
                    
prent()
choice()