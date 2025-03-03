# 5. Check Whether a String is Symmetrical/Palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
test_string = input("Enter a string: ")
if is_palindrome(test_string):
    print(f"'{test_string}' is a palindrome.")
else:
    print(f"'{test_string}' is not a palindrome.")
