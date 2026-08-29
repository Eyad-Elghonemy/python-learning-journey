# -----------------
# -- Loop => For --
# -----------------
# For item in iterable_object :
#   Do Something With Item 
# -----------------------------
# item is a variable you create and call whenever you want 
# item refer to current position and will run and visit all items to the end
# iterable_object => sequence [ list, tuples, set, dict, string or characters, etc ... ]
# --------------------------------------------------------------------------------------

mynums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in mynums :
    
  #  print(mynums)
  
  if number % 2 == 0 : #Even
      
      print(f"the number {number} is even")
      
  else :
      
      print(f"the number {number} is odd")
      
else :
    
    print("loop is finished")
    
myname = "osama"

for letter in myname :
    
    print (f" [ {letter.upper()} ] ")