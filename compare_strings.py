s1= "banana"
s2= "banana"
print(s1 == s2)
s2= "Banana"
print(s1 == s2)
print(s1 > s2) #beacause b is greater than B (lowercase is considered greater)
s1= "banana"
s2= "banany"
print(s1 > s2) #False, because a is not > y (y towards the end of the alphabet)

#in operator can be used for strings
s1 = "I went to see James"
s2 = "went"
print(s2 in s1) #True, it is inside
print("ana" in "banana") #True, it is inside the word
print("ANA" in "banana") #False, it is not inside the word, not capital letters



