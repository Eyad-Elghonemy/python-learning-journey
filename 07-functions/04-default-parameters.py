# ---------------------------------
# -- Function Default Parameters --
# ---------------------------------

def say_hello(name = 'Unknown', age = 'Unknown', country = 'Unknown') : 
    
    print(f"Hello {name} Your Age Is {age} And Your Country IS {country}")
    
say_hello("osama", 36, "EGy")
say_hello("Ali", 28, "KSA")
say_hello("sameh", 38)
say_hello("Ramy")
say_hello()