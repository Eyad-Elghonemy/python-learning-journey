# ---------------------------
# -- Break, Continue, Pass --
# ---------------------------

mynumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

# continue

for number in mynumbers :
    
    if number == 13 :
       
        continue
    
    print(number)
    
print('#'*50)
    
# Break

for number in mynumbers :
    
    print(number)
    
    if number == 13 :
        
        break
    
    
print('#'*50)

# Pass

for number in mynumbers :
    
    pass
    
    
print('#'*50)
    
# Pass

for number in mynumbers :
    
    if number == 13 :
        
        pass
    
    print(number)
    
    