# ----------------------------
# -- Loop => While Training --
#-----------------------------
# While condition _is_true
#  Code Will Run Untill Condition Become False 
# ----------------------------

myf = ["os", "ah", "ga", "al", "ra", "sa", "ta", "ma", "mo", "wa" ]

print(len(myf))  # List Length

a = 0

while a < len(myf) :    # a < 10

    print(F"#{str (a + 1).zfill(3)} {myf[a]} ")
    
    a += 1  # a = a + 1 
    
else :     
    
    print("All Friends Printed To Screen")

# print(f"#1 {myf[0]}")
# print(myf[0])
# print(myf[1])
# print(myf[2])
# print(myf[3])
# print(myf[4])
# print(myf[5])
# print(myf[6])
# print(myf[7])
# print(myf[8])
# print(myf[9])

