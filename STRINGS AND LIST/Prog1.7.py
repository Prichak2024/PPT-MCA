# 7.	Intersection of Two Lists
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6] 
print(intersection(lst1, lst2)) 
