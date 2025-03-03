# 2. Reverse Words in a Given String
def reverse_words(s):
    return " ".join(s.split()[::-1])

s = "Hello World Python"
print(reverse_words(s))
