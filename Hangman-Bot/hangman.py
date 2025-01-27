import random, codecs
import os

def get_word(topic, language):
    try:
        if language == 'gb':
            file_path = f"{topic}_EN.txt"
            if not os.path.exists(file_path):  # Check if file exists
                print(f"Error: {file_path} not found!")
                return None  # Or return a default word if desired
            with open(file_path, "r") as file:
                return random.choice(file.readline().split()).lower()
        elif language == 'ua':
            file_path = f"{topic}_UA.txt"
            if not os.path.exists(file_path):  # Check if file exists
                print(f"Error: {file_path} not found!")
                return None  # Or return a default word if desired
            with codecs.open(file_path, "r", encoding='utf-8') as file:
                return random.choice(file.readline().split()).lower()
    except Exception as e:
        print(f"Error while getting word: {e}")
        return None  # Return None if any other error occurs

def get_daily_word():
    try:
        topic = random.choice(['Fauna', 'Flora', 'Science', 'Sports', 'Countries'])
        file_path = f"{topic}_EN.txt"
        
        if not os.path.exists(file_path):  # Check if file exists
            print(f"Error: {file_path} not found!")
            return None  # Or return a default word if desired
        
        with codecs.open(file_path, "r", encoding='utf-8') as file:
            return random.choice(file.readline().split()).lower()
    except Exception as e:
        print(f"Error while getting daily word: {e}")
        return None  # Return None if any other error occurs

def is_word_guessed(secret, letters_guessed):
    count = 0
    n = len(secret)

    for i in secret:
        for j in letters_guessed:
            if i == j:
                count += 1

    if n == count:
        return 1

    return 0

def get_guessed_word(secret, letters_guessed):
    guessed_word = ""
    for i in range(len(secret)):
        if secret[i] in letters_guessed:
            guessed_word += secret[i] + " "
        else:
            guessed_word += "_ "

    return guessed_word.strip()  # Remove trailing space

def get_available_letters(letters_guessed, language):
    if language == 'gb':
        alphabet = "abcdefghijklmnopqrstuvwxyz"
    else:
        alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'"
    
    available_letters = "".join([letter for letter in alphabet if letter not in letters_guessed])
    return available_letters