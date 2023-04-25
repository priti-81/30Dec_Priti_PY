""" import sys
print(sys.path)
sys.path.insert(0,"d:\\python assignment\\python assignment")
print(sys.path)
from Module_4.myfile import Geometry 
g=Geometry()
g.Area_circle(15)"""

x = "awesome"
c='wah'
def myfunc():
  global x
  x = input('enter a value: ')

def my1fun ():
  global c
  print(f'python is {x}')
  c='pista'
  print(c)


my1fun()
myfunc()

print("Python is " + x)
