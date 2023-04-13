import errno

try:
    f = open('/opt/tmp/myfile.txt')
except IOError as e:
    if e.errno == errno.ENOENT:
        print('File not found')
    elif e.errno == errno.EACCES:
        print('Permission denied')
    else:
        print (e)
# When their is error or not finally block will always execute....
finally:
    print('file not opened')