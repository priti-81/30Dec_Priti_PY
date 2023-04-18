import os
 
def LastNlines(fname, N):
    bufsize = 8192  
    fsize = os.stat(fname).st_size
    #print(fsize)
    
    with open(fname) as f:
        if bufsize > fsize:
            bufsize = fsize
             
            fetched_lines = []
            while True:
                #print(f.readlines())
                f.seek(0)
                fetched_lines.extend(f.readlines())
                if len(fetched_lines) >=N :
                        return("".join(fetched_lines[-N:]))
                        
          
print(LastNlines('D:/py.txt',2))
 
