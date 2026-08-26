name="osama"
age=36
rank=10


print("my name is : {:s} and my age is : {:d} and my rank is : {:.3F} ".format (name,age,rank))

# {:s} => string
# {:d} => numbers
# {:f} => floating points numbers 

n= "osama"
l= "python"
y= 10

print("my name is {} iam {} developer with {:d} years exp".format (n, l, y))

mynumber= 10
print("my number is:{:d}".format (mynumber))
print("my number is: {:f}".format (mynumber))
print("my number is: {:.2f}".format (mynumber))

# truncate strings

mylongstring="hello peoples from elzero web school i love you all"
print("message is {}".format( mylongstring))
print("message is {:.13s}".format(mylongstring))

# format money

mymoney = 500612348544

print("my money in bank is : {}".format(mymoney))
print("my money in bank is : {:_d}".format(mymoney))
print("my money in bank is : {:,d}".format(mymoney))

# rearrange 

a, b, c, = "one", "two", "three"

print("hello {} {} {}".format(a,b,c)) # hello one two three
print("hello {1} {2} {0}".format(a,b,c)) # hello two three one
print("hello {2} {0} {1}".format(a,b,c)) # hello three one two 

x, y, z =10, 20, 30 
print("hello {1} {2} {0}".format(x,y,z))
print("hello {2} {0} {1}".format(x,y,z))
print("hello {1:d} {2:d} {0:d}".format(x ,y ,z ))
print("hello {1:f} {2:f} {0:f}".format(x,y,z))
print("hello {1:.2f} {2:.3f} {0:.4f}".format(x,y,z))

# format in version 3.6+

myname= "osama"
myage= 36

#print("my name is : {myname} and my age is : {myage}")
print(f"my name is : {myname} and my age is : {myage}")


#:<		Left aligns the result (within the available space)
#:>		Right aligns the result (within the available space)
#:^		Center aligns the result (within the available space)
#:=		Places the sign to the left most position
#:+		Use a plus sign to indicate if the result is positive or negative
#:-		Use a minus sign for negative values only
#: 		Use a space to insert an extra space before positive numbers (and a minus sign befor negative numbers)
#:,		Use a comma as a thousand separator
#:_		Use a underscore as a thousand separator
#:b		Binary format
#:c		Converts the value into the corresponding unicode character
#:d		Decimal format
#:e		Scientific format, with a lower case e
#:E		Scientific format, with an upper case E
#:f		Fix point number format
#:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
#:g		General format
#:G		General format (using a upper case E for scientific notations)
#:o		Octal format
#:x		Hex format, lower case
#:X		Hex format, upper case
#:n		Number format
#:%		Percentage format