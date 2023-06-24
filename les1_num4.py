word = str(input())
word_inversion = word[::-1]
if word == word_inversion:
  print("Это слово является палиндромом")
else:
  print("Это слово не является палиндромом")