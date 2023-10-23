import codecs
import os
import matplotlib.pyplot as plt

def count_letters(text):
    letters = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'
    letters_dictionary = {letter: 0 for letter in letters}

    for char in text.lower():
        if char in letters:
            letters_dictionary[char] += 1

    return letters_dictionary

def draw_histogram(letters_dict):
    letters = list(letters_dict.keys())
    occurrences = list(letters_dict.values())

    plt.bar(letters, occurrences)
    plt.xlabel('litery')
    plt.ylabel('il. wystapien')
    plt.title("HISTOGRAM")
    plt.show()

with codecs.open('tekst1.txt', 'r', encoding='utf-8') as f:
    text = f.read()

letter_counts = count_letters(text)
draw_histogram(letter_counts)


'''total_num_letters = sum(letters_dictionary.values())
sorted_pairs = sorted([(value, key) for (key, value) in letters_dictionary.items()], reverse=True)

for value, letter in sorted_pairs:
    percentage = 100*value/total_num_letters
    print(f'{letter}:{value}({percentage:.2f}%)')'''
