import os
import matplotlib.pyplot as plt

choice = input('do czego chcesz histogram: (1) - podaj tekst: , (2) - zdjecie.jpg: ')

if(choice == '1'):

    text = input("Wprowadz tekst: ")
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

elif choice == '2':
    file_path = input("Podaj ścieżkę do pliku: ")

    try:
        with open(file_path, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print("Błędna ścieżka, bądź plik nie istnieje")
    else:
        letter_counts = count_letters(text)
        draw_histogram(letter_counts)
else:
    print('Niepoprawna wartość')

