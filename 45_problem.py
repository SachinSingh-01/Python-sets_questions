'''Write a program where:
One set remains unchanged
Another set keeps updating
Use appropriate set methods.'''
A={5,4,3,2,567,6}
B={8,9,54,3,12,0,7}
result = A.union(B)
print("A remains unchanged:", A)
print("Result of union:", result)
C = {1, 2, 3, 4}
D = {3, 4, 5, 6}
C.intersection_update(D)
print("C keeps updating:", C)