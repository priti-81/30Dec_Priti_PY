class Faculty:
    name='priti'
    def __init__(self,qualification):
        self.c=qualification

    def facultyinfo(self):
        print('faculty qualification is:',self.c)
        print('faculty name is:',Faculty.name)

    def teaching(self,subject):
        print('faculty is teaching:',subject)

    def guiding(self,course):
        self.a=course
        print('faculty is  guiding about:',self.a)

class Course(Faculty):
    def coursename(self,name):
        print('course name is:',name)
        
        

c=Course('MBA')
c.coursename('python')
c.facultyinfo()