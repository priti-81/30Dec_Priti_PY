""" import sys
print(sys.path)
sys.path.insert(0,"d:\\python assignment\\python assignment")
print(sys.path)
from Module_4.myfile import Geometry 
g=Geometry()
g.Area_circle(15)

 """
from Module_4.myfile import Geometry
g=Geometry()
g.Area_rectangle(5,5)
