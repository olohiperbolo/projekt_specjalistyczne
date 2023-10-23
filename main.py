import os
import matplotlib as plt

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
def draw_histogram(quantity):
    letters = list(quantity.keys())
    occurrences = list(quantity.values())

    plt.bar(letters, occurrences)
    plt.xlabel('litery')
    plt.ylabel('il. wystapien')
    plt.title("HISTOGRAM")
    plt.show()

#funkcja do wpisywania lokalizacji pliku
def load_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            text = file.read()
            return text
    else:
        return None

#szukanie wpisanej sciezki
if __name__ == "__main__":
    file_path = "C:\\Users\\aleks\Desktop\\tekst1.txt"

    text = load_file(file_path)

    if text is not None:
        letter_quantity = count_letters(text)
        draw_histogram(letter_quantity)
    else:
        print("Plik nie został znaleziony.")