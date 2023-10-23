import codecs
import os
import matplotlib as plt

with codecs.open('tekst1.txt', 'r', encoding='utf=8') as f:
    text = f.read()

letters = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'

letters_dictionary = {letter: 0 for letter in letters}

for char in text.lower():
    if char in letters:
        letters_dictionary[char] += 1

total_num_letters = sum(letters_dictionary.values())
sorted_pairs = sorted([(value, key) for (key, value) in letters_dictionary.items()], reverse=True)

for value, letter in sorted_pairs:
    percentage = 100*value/total_num_letters
    print(f'{letter}:{value}\t({percentage:.2f}%)')

f.close()