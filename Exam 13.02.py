# Task 1

def card_num_hide(card):
    return '*' * len(card[:-4]) + card[-4:]

card = '1234 1234 1234 1234'
print(card_num_hide(card))

# Task 2

def palindrome(word):
    word = word.replace(' ','').lower()
    return 'Палиндром' if word == word[::-1] else 'Не палиндром'

word = 'Заказ'
print(palindrome(word))

# Task 3





