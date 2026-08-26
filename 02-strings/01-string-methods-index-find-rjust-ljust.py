# ---------------------------
# -- strings methods --
# ---------------------------

# index(substring, start, end)

a= "i love python"
print(a.index("p")) #index 7
print(a.index("p",0,10)) #index num 7
#print(a.index("p",0,5)) #error

#find(substring, start, end)

b = "i love python"
print(b.find("p"))  #index 7
print(b.find("p",0,10))  #index num 7
print(b.find("p",0,5))  # -1

# rjust(width, fill character) ijust(width, fill characte)

c= "osama"
print(c.rjust(10, "%"))
print(c.ljust(10, "%"))

# splitlines()

e= """first line
second line
third line"""

print((e.splitlines()))

f= "first line\nsecond line\nthird line"
print(f.splitlines())

# expandtabs 

g= "hello\tworld\ti\tlove\tpython"
print(g.expandtabs(2))

# is

one= "I Love Python And 3G"
two= "i love python and 3g"
print(one.istitle())
print(two.istitle())

THREE=""
four=" "
print(THREE.isspace())
print(four.isspace())

five= "ilove python"
six= 'I Love Python'
print(five.islower())
print(six.islower())

seven= "osama_elzero"  #48aal 
eight='osamaelzero100'
nine='osama--elzero100'

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x="aaaaabbbbb"
y="aaaaabbbbb1111"
print(x.isalpha())
print(y.isalpha())

u="aaaaabbbbb"
z="aaaaabbbbb1111"
print(u.isalnum())
print(z.isalnum())