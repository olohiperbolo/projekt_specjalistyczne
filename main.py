import os
import matplotlib as plt

quantity = []

#zliczanie liter
def count_letters(text):
    quantity = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in quantity:
                quantity[char] += 1
            else:
                quantity[char] = 1
    return quantity

#tworzenie wykresu
def draw_char(quantity):
    letters = list(quantity.keys())
    occurences = list(quantity.values())

    plt.bar(letters, occurences)
    plt.xlabel('litery')
    plt.ylabel('il. wystapien')
    plt.title("HISTOGRAM")
    plt.show()

#funkcja do wpisywania lokalizacji pliku
def load_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
        return text
if __name__ == "__main__":
    file_path = input("Podaj ścieżkę: ")

    try:
        text = load_file(file_path)
        letter_quantity = count_letters(text)
        draw_char(letter_quantity)
    except FileNotFoundError:
        print("Plik nie został znaleziony.")