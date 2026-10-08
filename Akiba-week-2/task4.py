
word = input("Enter a word: ")

word = word.lower()

if word == word[::-1]:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")