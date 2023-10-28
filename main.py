import os
import matplotlib.pyplot as plt
import cv2 as cv

choice = input('do czego chcesz histogram: (1) - plik.txt, (2) - zdjecie.jpg: ')

file_path = input("Podaj ścieżkę do pliku: ")

if(choice == '1'):
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

    try:
        with open(file_path, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print("Błędna ścieżką, bądź plik nie istnieje")
    else:
        letter_counts = count_letters(text)
        draw_histogram(letter_counts)
elif choice == '2':
    img = cv.imread(file_path, 0)
    hist = cv.calcHist([img], [0], None, [256], [0, 256])
else:
    print('niepoprawna wartość')

