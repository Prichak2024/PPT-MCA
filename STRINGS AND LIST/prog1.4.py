# 4.	Remove Multiple Elements from a List
def remove_multiple(lst, elements):
    return [item for item in lst if item not in elements]

lst = [1, 2, 3, 4, 5]
elements_to_remove = [2, 4]
print(remove_multiple(lst, elements_to_remove))  
