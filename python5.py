class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  @classmethod
  def convertstr (self, string):
    return self(string.split("-")[0], string.split("-")[1])

  def show (self):
    print(f"{self.name} and {self.salary}")

# YOU CAN USE CLASS METHODS TO HANDLE DIFFERENT TYPES OF DATA
e = Employee("Tejas", 1200000)
e.show()

str = "Ananya-12000"
e2 = Employee.convertstr(str)
e2.show()