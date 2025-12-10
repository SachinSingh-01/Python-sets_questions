'''Create a set of numbers from 1:50 that are:
divisible by 3
not divisible by 5'''
store=set()
for i in range(1,51):
    if i%3==0 and i%5!=0:
        store.add(i) 
print(store)
   