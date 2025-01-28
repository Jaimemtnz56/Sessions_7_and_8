#Print the list of methods
from idlelib.multicall import MC_ENTER
from itertools import count
from string import punctuation
from traceback import print_tb

methods = dir("Hi")
#Print without the double underscores
useful_methods = []
for method in methods:
    if "__" in method:
        continue
    useful_methods.append(methods)
print(useful_methods) # continue function to get rid of __ methods, not useful

print(help("hi".capitalize)) #get help for whatever method you used
print("cat".capitalize()) #Makes the first letter capital letter when it is not already
#See the use of an specific method for strings in this case
print(help("".casefold))
print("Hello". center(30, "*")) #Create spaces and locate a word
print("bananananananananananananananana". count("ana")) # Counts the number of times inside string
print("Ana ana ana banana". find("ana")) #4 because first ana lowercase is in position 4
print("Ana ana ana banana". find("ana", 5)) #find first from specified position

print("abcdefg".index("b")) # 1, prints position where b is inside the string
print("abcdefg".index("b", 0)) #starting from a certain position, no result

words = ["i", "like", "to", "sing"] #list of words
print(" ".join(words)) #it joins the words in the list with an space

s="I like to go hiking"
print(s.replace(" ", "! !")) #replaces a certain element inside a string
s= "I like to go hiking."
print(s.split()) #Splits the string by default spacing
#useful way to replace
print(s.replace(".", "!").split()) #Adds exclamation mark to the end
print(s.upper()) # Prints string in capital letters

#How to take out punctuation from sentences, or certain objects
punctuation="!.?./,"
sentence = "How, are, you? I don't like this"
for p in punctuation:
    sentence= sentence.replace(p, "")
print(sentence)

print("I like to play hockey".title()) #Puts it as title