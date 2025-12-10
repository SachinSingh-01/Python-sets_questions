'''Create two sets such that:
One is a proper subset
One is a proper superset
Verify using methods.'''
a = {2, 3, 4, 5, 6, 8, 9}
b = {2, 3, 4, 8}
print(a.issuperset(b))
print(b.issubset(a))