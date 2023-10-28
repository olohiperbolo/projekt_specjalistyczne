import matplotlib.pyplot as plt
import tkinter as ttk

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
def menu_window():
    global root
    root = ttk.Tk()
    root.geometry('400x200')
    frame1 = ttk.Frame(root, width=400, height=100)
    frame2 = ttk.Frame(root, width=400, height=100)
    from_text_button = ttk.Button(width= 15,text='Z Podanego tekstu', command=lambda:[frame2.forget, place_entry()])
    from_text_button.place(x=25,y=110)
    change_file = ttk.Button(width= 16,text='przetworz plik tekstowy',  command=lambda:[frame1.forget, place_entry1()])
    change_file.place(x=207,y=110)
    root.mainloop()

def place_entry():
    global frame1,frame2, from_text_entry
    frame1 = ttk.Frame(root, width=400, height=100)
    frame2 = ttk.Frame(root, width=400, height=100)
    frame1.place(x=0,y=0)
    from_text_entry = ttk.Entry(frame1, width=20, background='white',foreground='black')
    from_text_entry.place(x=103,y=60)
    from_file_label = ttk.Label(frame1, text='Podaj tekst')
    from_file_label.place(x=160, y=25)
    button = ttk.Button(root, text='Dalej', command=lambda:[from_text()])
    button.place(x=170, y = 150)
def place_entry1():
    global frame1,frame2, from_file_entry
    frame1 = ttk.Frame(root, width=400, height=100)
    frame2 = ttk.Frame(root, width=400, height=100)
    frame1.place(x=0,y=0)
    from_file_entry = ttk.Entry(frame1, width=20, background='white', foreground='black')
    from_file_entry.place(x=103, y=60)
    from_file_label = ttk.Label(frame1, text='Podaj sciezke pliku')
    from_file_label.place(x=140, y=25)
    button = ttk.Button(root, text='Dalej', command=lambda:[from_file()])
    button.place(x=170, y = 150)

def from_text():
    text = from_text_entry.get()
    letter_counts = count_letters(text)
    draw_histogram(letter_counts)

def from_file():
    running = True
    try:
        file_path = from_file_entry.get()
        with open(file_path, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print("Błędna ścieżka, bądź plik nie istnieje")
    else:
        letter_counts = count_letters(text)
        draw_histogram(letter_counts)


menu_window()