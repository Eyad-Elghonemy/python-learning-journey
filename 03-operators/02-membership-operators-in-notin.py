# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------

# string

name = "osama"
print("s" in name)
print("a" in name)
print("A" in name)

print("#"*50)

# list

friends = ["ahmed", "sayed", "mahmoud"]
print("Osama" in friends)
print("sayed" in friends)
print("mahmoud" not in friends)

print("#"*50)

# using in and not in with condition 

countriesone = ["egypt", "ksa", "kuwait", "bahrain"]
countriesonediscount = 80

countriestwo = ["italy", "usa"]
countriestwodiscount = 50

mycountry = input("where U from ??")

if mycountry in countriesone :
    
    print(f"hello you have a discount equal to ${countriesonediscount}")

elif mycountry in countriestwo :
    
    print(f"hello you have a discount equal to ${countriestwodiscount}")

else :
    
    print("you have no discount")    