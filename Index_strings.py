#index strings:
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

#for in strings and len function
s ="abasdfghjklnbvcxzwerty"
print(len(s)) #the number of characters the string has
    #we can iterate over a string and get any character
for character in s:
    print(character, end=" ") #end used to create an space between each character
print() #creates an enter effect

#same print using while instead (backwards):
i = len(s) - 1 #start a counter (positive starts from 0, while negative from -1)
while i >= 0:
    print(s[i], end=" ") #print the input with an end and space between it and the new one
    i = i - 1 #define how the counter increases
print()

#slice examples (it is a fancy index) #third number says the "steps"
s="0123456789"
print(s)
print(s[2:3]) # 2
print(s[4:6]) # 45
print(s[:3]) # 012
print(s[3:]) # 3456789
print(s[1:7:2]) #135
print(s[::-1])
print(s[::-2])


