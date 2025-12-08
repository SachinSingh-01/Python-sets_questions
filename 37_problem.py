# Write a program that checks if two strings have any common letter using sets.
str1=set(input("Enter the first string:"))
str2=set(input("Enter the second string:"))
common_letter=str1.intersection(str2)
if common_letter:
    print("common letter:",common_letter)
else:
    print("common letter:",common_letter)

