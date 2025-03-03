# 6.	Find Second Largest Number in a List
def second_largest(lst):
    unique_lst = list(set(lst))  
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) > 1 else None

lst = [1, 2, 3, 4, 5]
print(second_largest(lst))  
