# ---------------------
# -- Type Conversion --
# ---------------------

# str()

a=10
print(type(a))
print(type(str(a)))

print("="*50)

# tuple()

c = "osama" # string
d = [1,2,3,4] # list
e = {"a","b","c"} # set
f={"a" : 1, "b" : 2} # dictionary

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))

print("="*50)

# list()

c = "osama" # string
d = (1,2,3,4) # tuple
e = {"a","b","c"} # set
f={"a" : 1, "b" : 2} # dictionary

print(list(c))
print(list(d))
print(list(e))
print(list(f))

print("="*50)

# set()

c = "osama" # string
d = (1,2,3,4) # tuple
e = ["a","b","c"] # list
f={"a" : 1, "b" : 2} # dictionary

print(set(c))
print(set(d))
print(set(e))
print(set(f))

print("="*50)

# dict()

# c = "osama" # string
d = (("a",1),("b",2),("c",3)) # tuple
e = [["one",1],["two",2],["three",3]] # list
# f = {{"a",1},{"b",2}} # set

# print(dict(c)) # error
print(dict(d))
print(dict(e))
# print(dict(f))