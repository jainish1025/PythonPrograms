a= "4534"
a= int(a) # it will turn string into integer but only.

# a= float(a) integer to float convert
# a= str(a) float to string convert
# a= int(a) string to integer convert

print(type(a))
print(a+5)

# example 2
var1 = "54"
var2 =  4
var3 = 36.7
var4 = "32"
print(var1 + var4) #this is wrong it will not add

print(int(var1) + int(var4))  # this is correct

print(10 * str (int(var1) + int(var4)) )  # type casting

print(10 * "hellow world\n")
print("hellow world\n")
