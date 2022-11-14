text = input("Enter a text: ")

def count_v_c(text):
    vowels = 0
    consonants = 0
    for letter in text:
        if letter.isalpha():
            if letter.lower() in 'aeiouy':
                vowels += 1
            else:
                consonants += 1

    return (vowels, consonants)
print(count_v_c(text))