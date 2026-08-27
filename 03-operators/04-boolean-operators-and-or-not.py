# -------------------------------
# -- Boolean Operators -- 
# -------------------------------
# and
# or
# not
#

age = 36
country = "egypt"
rank = 10

print(age>16)
print(country=="egypt")

print(age>16 and country=="egypt" and rank >0) # True
print(age>16 and country=="ksa" and rank >0) # False

print(age>40 or country=="egypt") # True
print(age>40 and country=="egypt" or rank > 20)

print(age>16) # True
print(not age>16) # not True = False

