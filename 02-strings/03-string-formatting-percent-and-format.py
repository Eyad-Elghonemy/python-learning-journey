# -----------------------------
# -- Strings Formatting --
# -----------------------------

name ="osama"
age= 36
rank= 10

print("my name is : " + name)
# print("my name is : " + name + " " + "and my age is: " + age) # type error

print("my name is :%s and my age is :%d and my rank is :%f"% (name,age,rank))
print("my name is : {:s} and my age is : {:d} and my rank is : {:F} ".format (name,age,rank))

# %s => for string 
# %d => for numbers
# %f => for floating points numbers

n= "osama"
l= "python"
y= 10

print("my name is %s iam %s developer with %d years exp"% (n, l, y))

# control floating point number 

mynumber= 10
print("my number is: %d"% mynumber)
print("my number is: %.1f"% mynumber)

# truncate string 

mylongstring="hello peoples from elzero web school i love you all"
print("message is %.5s"% mylongstring)
print("message is %s"% mylongstring)
