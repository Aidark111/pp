def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

phrase = input("Enter a word or phrase: ")
if is_palindrome(phrase):
    print("Palindrome")
else:
    print("Not a palindrome")
