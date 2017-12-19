#creating an instanciated simple classes

#classes allow us to logically group our data and functions making it easy to reuse

class Employee:
    #means you just want to skip it

    pass
#each of these will be their own unique instances of the employee class

emp_1 = Employee()
emp_2 = Employee()

#both of these are unique objects that occupy some kind of memory

print(emp_1)
print(emp_2)

#instance variables contains data that is unique to each instance
#we can go ahead and create instance variables

emp_1.first = 'Mary'
emp_2.last = 'John'

emp_1.email = 'marya@gmail.com'
emp_1.pay = 50000


emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test@gmail.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)