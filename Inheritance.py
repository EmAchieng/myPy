#we can override or add a new functionality without affecting the parent class

#reusing the code

class Employee:
    raise_amt = 1.04

    def __int__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay


    def fullname(self):
        return '{} {}'. format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    pass

dev_1 = Developer('Mary', 'John', 50000)
dev_2 = Developer ('Test', 'User', 60000)

print(dev_1.email)
print(dev_2.email)