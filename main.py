import os
import matplotlib as plt

text = 'dzien dobry piotruciu nie dawaj sie, dzien dobry piotrusiu badz dzielny'

letters = 'abcdefghijklmnopqrstuvwxyz'

letters_dictionary = {letter: 0 for letter in letters}

#print(letters_dictionary)

for char in text.lower():
    if char in letters:
        letters_dictionary[char] += 1

'''total_num_letter = 0
for letter in letters:
    total_num_letter += letters_dictionary[letter]'''

total_num_letters = sum(letters_dictionary.values())
sorted_pairs = sorted([(value, key) for (key, value) in letters_dictionary.items()], reverse=True)

#print(sorted_pairs)

for value, letter in sorted_pairs:
    percentage = 100*value/total_num_letters
    print(f'{letter}:{value}\t({percentage:.2f}%)')