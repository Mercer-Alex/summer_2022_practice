import string


def valid_palindrom(word):
    word = word.translate(str.maketrans('', '', string.punctuation)).lower().strip()
    print(word)
    flip_word = word[::-1]
    return word == flip_word

word1 = "A man, a plan, a canal: Panama"

print(valid_palindrom(word1))
