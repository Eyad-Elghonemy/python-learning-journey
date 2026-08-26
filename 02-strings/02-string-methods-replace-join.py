# ------------------------------
# -- strings methods --
# ------------------------------

# replace(old value, new value, count)

a= "hello one two three one one"
print(a.replace("one","1"))
print(a.replace("one","1",1))
print(a.replace("one","1",2))

# join(iterable)

mylist=["osama", "mohamed","elsayed"]
print("-".join(mylist))
print(",".join(mylist))
print(" ".join(mylist))

