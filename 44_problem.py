'''Predict output without running:
x = {1, 2, 3}
y = x
x.add(4)
print(y)
Now solve it correctly so y does not change.'''
x = {1, 2, 3}
y = x
x.add(4) 
print(y)
# output:-4 will be add on x and y=x so output = {1,2,3,4}