# ----------------------------------
# -- Date And Time => Format Date --
# ----------------------------------
# https://strftime.org/
# ---------------------

import datetime

mybirthday = datetime.datetime(2005,3,22)

print(mybirthday)
print(mybirthday.strftime("%a"))
print(mybirthday.strftime("%A"))
print(mybirthday.strftime("%b"))
print(mybirthday.strftime("%B"))

print(mybirthday.strftime("%d, %B, %Y"))
print(mybirthday.strftime("%d/%B/%Y"))
print(mybirthday.strftime("%d - %B - %Y"))