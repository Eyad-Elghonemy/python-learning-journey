my_nums = [15, 81, 5, 17, 20, 21, 13]

my_nums.sort(reverse=True)

sum = 0

for number in my_nums :
    
    if number %5 == 0 :
        
        sum += 1 
        
        print(f"{sum} => {number}")
        
    else : 
    
        continue
    
else :
        
    print("All Numbers Printed")    