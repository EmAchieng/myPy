import pickle


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


person = Person('Mary', 15)
print(person.getName())
print(person.getAge())

with open('mary', 'wb') as f:
    pickle.dump(person, f)

with open('mary', 'rb') as f2:
    mary = pickle.load(f2)

print(mary.getName())
print(mary.getAge())