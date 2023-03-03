π=3.141592653589793

def cylinder(radius,height):
    return (π*radius*radius*height)

print('cylinder surface volume :',cylinder(15,10))

def CSA(r,h):
    return 2*π*r*h
print('cylinder curved surface area :',CSA(15,10))

def TSA(r,h):
    return 2*π*r*(r+h)
print('cylinder Total surface area :',TSA(15,10))


