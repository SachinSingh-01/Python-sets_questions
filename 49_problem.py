'''Given a list:
data = ["apple", "Apple", "banana", "BANANA", "orange"]
Create a set of unique lowercase words only using set comprehension.'''
data = ["apple", "Apple", "banana", "BANANA", "orange"]
lower_set = {i.lower() for i in data}
print(lower_set)