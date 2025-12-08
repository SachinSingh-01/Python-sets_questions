# Generate a set of squares of numbers from 1 to 10 using set comprehension.
square=set()
for i in range(1,11):
    square.add(i*i)
print(square)
