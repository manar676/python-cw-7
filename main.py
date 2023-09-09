class person :
    # name="manar"
    # age=17 
    def is_adult(self):
       if self.age > 18 :
          print("You have too much responsibilities")
       else:
          print("lucky")
          
first_person=person()
print(first_person.name)
print(first_person.age)
first_person.is_adult()
class person :
    def __init__(self,name,age):
       self.name= name
       self.age=age 

    def is_adult(self):
       if self.age > 18 :
          print("You have too much responsibilities")
       else:
          print("lucky")
    def __str__(self):
          return f"my name is{self.name} and I am {self.age}years old)"
    


first_person=person("manar",17)
print(first_person.name)
print(first_person.age)
first_person.is_adult()
print(first_person)