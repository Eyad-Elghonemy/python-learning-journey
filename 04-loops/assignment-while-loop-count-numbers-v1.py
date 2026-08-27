num = int(input("write number : " ))

count = num - 2

if num < 0 or num == 0 : 
    
    print(f"Number {num} Is Not Larger Than 0 ")
    
else :
    
    pass

while num > 1 :
  
    num -=1
    
    if num == 6 :
        
        continue
    
    print(num)
    
print(f"{count} Numbers Are Printed Successfully")

