# ----------------
# -- Generators --
# ----------------
# [1] Generator Is A Function With "yield" Keyword Instead of "return"
# [2] It Support Iteration And Return Generator Iterator By Calling "yield"
# [3] Generator Function Can Have One Or More "yield"
# [4] By Using next() It Resume From Where It Called "yield" Not From Begining
# [5] When Called, Its Not Start Automatically, Its Only Give You The Control
# -----------------------------------------------------------------

def mygenerator():
    
    yield 1
    yield 2
    yield 3
    yield 4
    
# print(mygenerator())

mygen = mygenerator()

print(next(mygen))

print("Hello From Python")

print(next(mygen))

print("Hello From Python")

print('$'*50)

for number in mygen :
    
    print(number)