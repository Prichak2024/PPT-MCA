# 4. Remove ith Character from the String
def remove_ith_character(s, i):
    return s[:i] + s[i+1:]
s = "Python"
i = 2
print(remove_ith_character(s, i))  
