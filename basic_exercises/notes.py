message = "Hi there, type your qualification, please: "
print(message)
qualification = input() # Or get note through input()
color = None

# if int(qualification) >= 7:
#     color = "Green" 
# else:
#     color = "Red"
# print("Your qualification is: ", qualification, color)

color = "Green" if int(qualification) >= 7 else "Red"
print("Your qualification is: ", qualification, color)
