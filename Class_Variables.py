class Employee:



    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

#you can choose to manually go in and change  the pay amount
    def apply_raise(self):
         self.pay = int(self.pay * 1.04)

emp_1 = Employee('Mary', 'John', 50000)
emp_2 = Employee('Test', 'User', 60000)


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.__dict__)

print(emp_1.__dict__)


