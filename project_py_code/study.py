
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

  def greet(self, greeting, year):
    self.greet = greeting
    print(f"Hello {self.greet} {self.firstname}  {self.lastname} welcome to {year}")

class Student(Person):
     def __init__(self, firstname, lastname):
         super().__init__(self, lastname)
