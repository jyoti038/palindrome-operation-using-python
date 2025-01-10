def is_palindrome(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]

# Test the function
word = input("Enter a string to check for palindrome: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
