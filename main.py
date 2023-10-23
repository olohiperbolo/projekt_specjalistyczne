import os
import matplotlib as plt

quantity = []

def count_letters(text):
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in quantity:
                quantity[char] += 1
            else:
                quantity[char] = 1
    return quantity

