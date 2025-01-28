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
print()

#same print using while instead (backwards):
i = -1 #start a counter
while i < len(s):
    print(s[i], end=" ") #print the input with an end and space between it and the new one
    i -= 1 #define how the counter increases

