# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable
# [1] Object contains Data That Can Be Iterated Upon
# [2] Examples (Strings, List, Set, Tuple, Dictionary)
# --------------------------------------------
# Iterator
# [1] Object Used To Iterator Over Iterable Using next() Method Return 1 Element At A Time
# [2] You can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method On The Iterable Behind The Scene
# [4] Gives "Stopiteration" If There No Next Element
# ---------------------------------------------------------

mystring = "Osama"

mylist = [1, 2, 3, 4, 5]

# for letter in mystring :
    
#     print(letter, end = " ")
    
# for num in mylist :
    
#     print(num, end = " ")
    
myiterator = iter(mystring)    

# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))

for letter in iter("Elzero") :
    
    print(letter, end = " ")