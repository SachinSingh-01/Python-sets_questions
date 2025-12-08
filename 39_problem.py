# Given two lists, find which elements are present in both using sets.
lst1=[3,5,6,7,7,3,9,8,2]
lst2=[7,8,9,3,2,5,1,7]
set1=set(lst1)
set1=set(lst1)
set2=set(lst2)
element_present_in_both=set1.intersection(set2)
print(element_present_in_both)