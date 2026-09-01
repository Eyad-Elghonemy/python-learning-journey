# ---------------------------------------
# -- Function Parameters And Arguments --
# ---------------------------------------

a, b, c = "osama", "ahmed", "sayed"

#print(f"hello {a}")
#print(f"hello {b}")
#print(f"hello {c}")


# def                    => Function Keyword [Define]
# say_hello()            => Function Name
# name                   => Parameter
# print(f"Hello {name}") => Tsak
# say_hello("Osama")     => Osama Is The Arguement


def say_hello(name):
    
    print(f"Hello {name}")
    
say_hello(a)
say_hello(b)
say_hello(c)



def addition(n1 , n2) :
    
    if type(n1) != int or type(n2) != int :
        
        print("only integrs allowed")
    
    else:
        
        print(n1 + n2)
    
    
addition(100,500)

def full_name(first, middle, last) :
    
    print(f"Hello {str(first).strip().capitalize()} {str(middle).upper():.1s} {str(last).capitalize()}")
    
full_name('  osama  ', 'ahmed', 'sayed')