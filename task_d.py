def is_palindrome(word):
    return word.lower() == word[::-1].lower()
test_word = input("Enter a word to check if it's a palindrome: ")
if is_palindrome(test_word):
    print(f"'{test_word}' is a palindrome.")
else:
    print(f"'{test_word}' is not a palindrome.")