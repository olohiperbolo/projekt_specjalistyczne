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
    plt.ylabel('il. wystąpien')
    plt.title("HISTOGRAM")
    plt.show()

running = True

while running:
    print("Wybierz opcję:")
    print("1. Podaj tekst")
    print("2. Przetwórz plik tekstowy")
    print("3. Wyjdź")

    choice = input("Twój wybór: ")

    if choice == '1':
        text = input("Wprowadź tekst: ")
        letter_counts = count_letters(text)
        draw_histogram(letter_counts)

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

    elif choice == '3':
        running = False
else:
    print('Niepoprawna wartość. Podaj 1, 2 lub 3:')
