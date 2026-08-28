# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------

country = "egypt"

if country == "egypt" : print(f"the weather in {country} is 15")
   
elif country == "ksa" : print(f"the weather in {country} is 30")
  
else : print("country isnot in the list")  

# short if

movierate = 18
age = 18

if age < movierate : 
   
   print("movie is not good for you") # condition if true
   
else :
   
   print("movie is good 4u and happy watching") # condition if false
   
print("movie is not good for you" if age < movierate  else  "movie is good 4u and happy watching") 

# condition if True | if condition | else | condition if False