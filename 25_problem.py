# Take two sets and find which elements exist only in the first set.
set1={"sachin","kakali","anurag","priya","adarsh","sahmir","karishma","saloni","krishna"}
set2={2,5,6,7,5,5,8,9,1,4,7}
user=input("Enter the value of set1 to check it is present or not:")
if user in set1:
    print("yes present")
else:
     print("no not present")


# method-2
set1 = {"sachin","kakali","anurag","priya","adarsh","sahmir","karishma","saloni","krishna"}
set2 = {2,5,6,7,8,9,1,4}

result = set1.difference(set2)
print(result)
