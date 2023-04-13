print('Welcome to  Python E - Note\n')
print('Press 1 for generate Note')
print('Press 2 for view Note')
print('Press 4 for exit\n')

import logging,re, Assessment_1_FILE as p

logger=logging.getLogger()

logging.basicConfig(filename='logfile.log',datefmt="%d-%m-%Y %I:%M:%S %p",
               format='%(asctime)s: %(levelname)s: %(message)s',level=logging.INFO)
                  

    
pattern=re.compile(r'[A-Za-z\s]+')

logger.info('-------------------------------------------------------------------')
a,b,c='','',''
def g_note(): 
    global a,b,c 
    for i in range(6):
        a=input('Enter python E-note generator name: ')
        logger.info(f'Enter python E-note generator name :{a}')
    
        user=re.findall(pattern,a)
        if [a]==user:
            break
        else:
            print('only alphabets allow\n')
            
    b=input('Enter Python E-note title: ')
    logger.info(f'Enter Python E-note title:{b}')

    c=input('Enter E-note content:')
    logger.info(f'tEnter E-note content :{c}')
    
    if input('Do you want to make more notes ?(y/n): ')=='y':
        g_note()
    else:
         print('\n Your note generated successfully...')


         
for i in range(6):
    x=int(input('Enter your choice: '))    
    if x==1:
        g_note()
    elif x==2:
        if a=='':
            print('Please Generate note first..')
        else:
            p.view_note(a,b,c)
    elif x==4:
        exit()
            

