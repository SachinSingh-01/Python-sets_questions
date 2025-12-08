# Write a program to find unique vowels present in a word.
word=input("Enter the words:").lower()
vowels=('a','e','i','o','u')
unique_vowel=set()
for w in word:
    if w in vowels:
        unique_vowel.add(w)
print(unique_vowel)