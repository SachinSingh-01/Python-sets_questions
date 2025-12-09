# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7}
# Print elements that are only in A.
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
print(A-B)

# Print elements that are only in B.
print(B-A)

# Print elements common in both.
x=A.intersection(B)
print(x)

# Print all unique elements without modifying A or B.
y=A.union(B)
print(y)
