# ---------------------------------------------
# -- Calculate Age Advanced Version Training --
# ---------------------------------------------

# write a very beautiful note

print("#"*80)
print(" you can write the first letter or full name of the time unit ".center(80, "#"))
print("#"*80)

# Collect Age Data

age = int(input("Please write your age").strip())

# collect time unit data

unit = input("please choose time unit: Months, weeks, days, hours, mins, secs").strip().lower()

# get time units

months = age*12
weeks = months*4
days = age*365
hours = days*24
mins = hours*60
secs = mins*60

if unit == "months" or unit == "m" : 
    print("you choose the unit months")
    print(f"you lived for {months:,} months.")
    
elif unit== "weeks" or unit == "w" :
    print("you choose the unit weeks")
    print(f"you lived for {weeks:,} weeks.")
    
elif unit== "days" or unit == "d" :
    print("you choose the unit days")
    print(f"you lived for {days:,} days.")
    
elif unit == "hours" or unit == "h" : 
    print("you choose the unit hours")
    print(f"you lived for {hours:,} hours.")
    
elif unit== "mins" or unit == "m" :
    print("you choose the unit mins")
    print(f"you lived for {mins:,} mins.")
    
elif unit == "secs" or unit == "s":
    print("you choose the unit secs")
    print(f"you lived for {secs:,} secs.")
 