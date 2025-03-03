# 5.	Remove Duplicates from a List
def remove_duplicates(lst):
    return list(set(lst))

lst = [1, 2, 3, 2, 4, 1]
print(remove_duplicates(lst))
