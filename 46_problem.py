'''Write a program to find common characters between two strings ignoring case.
Example:
"Python", "typhoon"'''
string1=input("Enter the string1:")
string2=input("Enter the string2:")
set1=set(string1)
set2=set(string2)
common=set1.intersection(set2)
print(common)