# Create a frozenset of numbers and try to add an item. Observe what happens.
a=frozenset({3,5,6,7,2,9})
print(a)
b=a.add(5)
print(b) # this will show an error because frozenset are immutable
