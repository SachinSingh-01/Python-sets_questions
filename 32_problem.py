# Use frozenset with set operations like union or intersection.
fs=frozenset({3,5,3,32,27,85})
s=set({4,6,3,2,32,27,54})
print(fs)
print(s)
result_union=fs.union(s)
print(result_union)
result_intersection=fs.intersection(s)
print(result_intersection)
