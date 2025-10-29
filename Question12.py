class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("Hello", self.name,"your avg score is:",sum/3)    

s1 = Student("Parth", [98,99,98])  
s1.get_avg()      
