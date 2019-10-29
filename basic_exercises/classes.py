# class Test:
#     def something(self):
#         return "Hello!!"

# var = Test()

# print(type(var))

# Each metho needs a paramater in this case is self

class User:

    def __init__(self, username = "", mail = "", name = ""):
        self.username = username
        self.mail = mail
        self.name = name

    def greet(self):
        return "Hi "+ self.name
    
    def show_username(self):
        print(self.username)
    
    def show_name(self): # Show name
        print(self.name)

    # def create_name(self, name): # Create name
    #     self.name = name

    

user1 = User("Jeison De Jesús Anillo Pérez", "Jason") 
#user1.username = "Jason"
# user1.mail = "jeison@testing.com.co"

user2 = User("Rodmy Jeraldin Jerez Numpaque", "Rodmy")
#user2.username = "Rodmy"
# user2.mail = "rodmy@testing.com.co"

# user1.show()
# user2.show()

# user1.create_name("De Jesús")
# user1.show_name()

variable = user1.greet()
print(variable)

var = user2.greet()
print(var)