# 3. Print Even-Length Words in a String.
def even_length_words(s):
    return [word for word in s.split() if len(word) % 2 == 0]
s = "This is a test string"
print(even_length_words(s))
