# Create a set comprehension that filters only even numbers from 1 to 20.
even_number=set()
for i in range(1,21):
    if i%2==0:
        even_number.add(i)
print(even_number)