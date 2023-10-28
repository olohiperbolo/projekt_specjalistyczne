import os
import matplotlib.pyplot as plt
import tkinter as ttk

def cOUnT_LeTTeRS(text):
    letters = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'
    letters_dictionary = {letter: 0 for letter in letters}

    for char in text.lower():
        if char in letters:
            letters_dictionary[char] += 1

    return letters_dictionary

def dRAw_HIsTOgRAm(letters_dict):
    letters = list(letters_dict.keys())
    occurrences = list(letters_dict.values())

    plt.bar(letters, occurrences)
    plt.xlabel('litery')
    plt.ylabel('il. wystąpien')
    plt.title("HISTOGRAM")
    plt.show()

running = True
def mENUwINdOW():
    global rOOt
    rOOt = ttk.Tk()
    rOOt.geometry('400x200')
    frame1 = ttk.Frame(rOOt, width=400, height=100)
    frame2 = ttk.Frame(rOOt, width=400, height=100)
    from_text_button = ttk.Button(width= 15,text='Z Podanego tekstu', command=lambda:[frame2.forget, pLAcE_EnTRy()])
    from_text_button.place(x=25,y=110)
    change_file = ttk.Button(width= 16,text='przetworz plik tekstowy',  command=lambda:[frame1.forget, pLAcE_EnTRy1()])
    change_file.place(x=207,y=110)
    rOOt.mainloop()

def pLAcE_EnTRy():
    global from_text_entry
    frame1 = ttk.Frame(rOOt, width=400, height=100)
    frame2 = ttk.Frame(rOOt, width=400, height=100)
    frame1.place(x=0,y=0)
    from_text_entry = ttk.Entry(frame1, width=20, background='white',foreground='black')
    from_text_entry.place(x=103,y=60)
    from_file_label = ttk.Label(frame1, text='Podaj tekst')
    from_file_label.place(x=160, y=25)
    button = ttk.Button(rOOt, text='Narysuj', command=lambda:[fROm_TExT()])
    button.place(x=160, y=150)
def pLAcE_EnTRy1():
    global from_file_entry
    frame1 = ttk.Frame(rOOt, width=400, height=100)
    frame2 = ttk.Frame(rOOt, width=400, height=100)
    frame1.place(x=0,y=0)
    from_file_entry = ttk.Entry(frame1, width=20, background='white', foreground='black')
    from_file_entry.place(x=103, y=60)
    from_file_label = ttk.Label(frame1, text='Podaj sciezke pliku')
    from_file_label.place(x=140, y=25)
    button = ttk.Button(rOOt, text='Narysuj', command=lambda:[fROm_FIlE()])
    button.place(x=160, y=150)

def fROm_TExT():
    text = from_text_entry.get()
    letter_counts = cOUnT_LeTTeRS(text)
    dRAw_HIsTOgRAm(letter_counts)

def fROm_FIlE():
    try:
        file_path = from_file_entry.get()
        with open(file_path, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print("Błędna ścieżka, bądź plik nie istnieje")
    else:
        letter_counts = cOUnT_LeTTeRS(text)
        dRAw_HIsTOgRAm(letter_counts)


mENUwINdOW()