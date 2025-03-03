# 9.	Maximum and Minimum Element’s Position in a List
def max_min_positions(lst):
    max_pos = lst.index(max(lst))
    min_pos = lst.index(min(lst))
    return max_pos, min_pos

lst = [1, 2, 3, 4, 5]
print(max_min_positions(lst))  
