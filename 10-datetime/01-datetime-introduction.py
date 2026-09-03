# -----------------------------------
# -- Date And Time => Introduction --
# -----------------------------------

import datetime

# Print(dir(datetime))

# Print(dir(datetime.datetime))

# Print The Current Date And Time 

print(datetime.datetime.now())

print('#'*50)

# Print The Current Year

print(datetime.datetime.now().year)

print('#'*50)

# Print The Current Month

print(datetime.datetime.now().month)

print('#'*50)

# Print The Current Day

print(datetime.datetime.now().day)

print('#'*50)

# Print Start And End Of Date

print(datetime.datetime.min)
print(datetime.datetime.max)

print('#'*50)

# print(dir(datetime.datetime.now()))

# Print The Current Time

print(datetime.datetime.now().time())

print('#'*50)

# Print The Current Time Hour

print(datetime.datetime.now().time().hour)

print('#'*50)

# Print The Current Time Minute

print(datetime.datetime.now().time().minute)

print('#'*50)

# Print The Current Time second

print(datetime.datetime.now().time().second)

print('#'*50)

# Print Start And End Of Time

print(datetime.time.min)
print(datetime.time.max)

print('#'*50)

# Print Specific Date

print(datetime.datetime(2005,3,22))
print(datetime.datetime(2005,3,22,10,45,55,150364))

mybirthday = datetime.datetime(2005,3,22)
datenow = datetime.datetime.now()

print(f"My Birthday Is {mybirthday} And", end =" ")
print(f"Date Now Is {datenow}")

print(f"I Lived For {datenow - mybirthday}")
print(f"I Lived For {(datenow - mybirthday).days}")

print(f"I Lived For {datenow - mybirthday}")