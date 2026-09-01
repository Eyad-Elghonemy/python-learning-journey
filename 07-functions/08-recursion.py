# ------------------------
# -- Function Recursion --
# ------------------------
# ------------------------------------------------------------------
# -- To Understand Recursion, You Need To First Understand Recursion
# ------------------------------------------------------------------

# Test Word [ WWWooooorrrldd ]
# x = "WWWooooorrrldd"
# print(x[1:])

def clean_word(word) :
    
    if len(word) == 1 :
        
        return word 
    
    print(f"Print Start Function {word}")
    
    if word[0] == word[1] :  # WWWooooorrrldd
        
        print(f"Print From Condition {word}")
        
        return clean_word(word[1:])
    
    print(f"Print Before Return {word}")   
    
    return word[0] + clean_word(word[1:]) 

    # Stach [ World ]

print(clean_word('WWWooooorrrldd'))