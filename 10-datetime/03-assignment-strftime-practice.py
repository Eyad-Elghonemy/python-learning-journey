# import random 

# print(f"Random Number Between 10 And 50 => {random.randint(10,50)}")

# print(f"Random Even Number Between 2 And 10 => {random.randrange(2, 11, 2)}")

# print(f"Random Odd Number Between 1 And 9 => {random.randrange(1, 10, 1)}")

# print(dir(random))

import datetime 

today = datetime.datetime(2021, 8, 10)

print(today.strftime("%Y-%m-%d"))

print(today.strftime("%b %d, %Y"))

print(today.strftime("%b - %d - %Y"))

print(today.strftime("%b / %d / %y"))

print(today.strftime("%b / %d / %Y"))

print(today.strftime("%a, %b %d %Y"))
