class Student:
    def  __init__(self,name="none"):
        self.name = name

    def   __str__(self):
        return  f'hello, my  name  is {self.name}'

    def __del__(self):
        print("i'm graduate")
stud = Student('Andriy')
print(stud)





    #print("hi")
    #amount_of_students  =  0
    #def __init__(self, height=0, name="noname",mark=0):
        #self.height = 160
        #self.mark=mark
        #self.name=name
        #self.height = height
       # print("Зріст",self.name,":", self.height)
       # Student.amount_of_students += 1



    #def  growUp(self):
      #def  self.height += 10

    #def growMark(self):
        #self.mark += 10

#maxym = Student(height=160, name = 'maxym')
#kate = Student(height=170, name = 'kate')
#stepan = Student(height=169, name = "stepan")

#maxym.growUp()
#print(maxym.mark)
#print(maxym.mark)


#print(kate.height)
#print(stepan.height)


