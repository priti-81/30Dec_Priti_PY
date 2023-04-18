import numpy as np


arr = np.array([[5,3,2,3],[4,8,2,6],[8,2,3,0]])
print(arr)

# Ellipsis literal
print(f"Ellipsis literal output:- {arr[1,...]}.")

# general slice notation
print(f"general slice notation output:- {arr[:,1]}")

# Python Ellipsis 
print(f"Python Ellipsis output:- {arr[... ,1]}")
print(f"Python Ellipsis output:- {arr[Ellipsis,1]}")


