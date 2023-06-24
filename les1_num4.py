def is_palindrome(word):
    return word == word[::-1]

word = input()
if is_palindrome(word):
    print("Палиндром")
else:
    print("Не палиндром")