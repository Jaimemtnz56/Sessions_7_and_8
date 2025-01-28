s1 = "hello world!"
print(s1)
print(s1[0], s1[1], s1[2]) #print characters
print(s1[4], s1[7]) # print both os
print(s1[11], s1[-1]) #print the last character
print(s1[-2]) #count from the end of the string
#You cannot print for example 15 or 1.2 as it is not an option for the string provided
print(s1[14//2]) #needed the double // to provide an integer number

#Operations with strings
s1= "Hello"
s2= "world"

print(s1+ " " + s2 + "!") #space and exclamation are also strings

#if operations:
if "bob":
    print("bob is")
else:
    print("bob isn't") #code unreachable

if "":
    print("Empty string is true") #code unreachable
else:
    print("Empty string is false")

