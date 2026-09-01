# ------------------------
# -- Function => lambde --
# ------------------------
# [1] Is Has No Name
# [2] You Can Call It Inline Without Defining It 
# [3] You Can Use It In Return Data Feom Another Function
# [4] Lambde Used For Simple Functions And Def Handle The Large Tasks
# [5] Lambde Is One Single Expression Not Block Of Code 
# [6] Lambde Type Is Function
# -----------------------------------------------------------------

def say_hello(name, age) : return f"Hello {name} Your Age Is : {age}"

hello = lambda name, age : f"Hello {name} Your Age Is : {age}"

print(say_hello("Ahmed", 36))
print(hello("Ahmed", 36))


print(say_hello.__name__)
print(hello.__name__)
   
   
file = open("D:\Users\eyad0\Documents\python\osama.txt")