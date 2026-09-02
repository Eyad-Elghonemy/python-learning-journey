# --------------------------------------------
# -- Doc String & Commenting vs Documenting --
# --------------------------------------------
# [1] Documenting String For Class, Module Or Function
# [2] Can Be Accessed From The Help And Doc Attributes
# [3] Made For Understanding The Functionality Of The Complex Code
# [4] Theres One Line And Multiple Line Doc Strings
# -------------------------------------------------

def elzero_function(name) :
    
    """
    Elzero Function 
      it say Hello From Elzero
    parameter :
      name => Person Name That use function
    Return :
      Return Hello message to the person
    """
    
    print(f"Hello {name} From Elzero")
    
elzero_function("Ali")

# print(dir(elzero_function))

# print(elzero_function.__doc__)

help(elzero_function)