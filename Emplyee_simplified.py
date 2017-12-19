#to avoid writing to many codes that are prone to mistakes, you can use the init method
#think of it as a constructor
#when we create methods within a class , they receive the instance as the first argument automatically
#self
#self is the instance
#first, last, pay are arguments


class Employee:
    def __int__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'


#pass on the values specified in our init method
#pass on the information manually insde the brackets

emp_1 = Employee('Mary', 'John', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.first)
print(emp_2.first)

#prints Mary.John@gmail.com
#prints Test.User@gmail.com



#if we want, we can run it from the class name, we need to inform it of the instance we are trying to pass by a parameter

#print Emlpoyee.fullname(emp_1)