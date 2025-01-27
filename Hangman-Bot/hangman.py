import random, codecs
import os

def get_word(topic, language):
    try:
        # Check for file path based on language
        if language == 'gb':  # English
            file_path = f"{topic}_EN.txt"
        elif language == 'ua':  # Ukrainian
            file_path = f"{topic}_UA.txt"
        else:
            print(f"Error: Unsupported language '{language}'")
            return None

        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"Error: {file_path} not found!")
            return None  # Return a default word if desired

        # Open the file based on language
        if language == 'gb':
            with open(file_path, "r") as file:
                words = file.readlines()
        elif language == 'ua':
            with codecs.open(file_path, "r", encoding='utf-8') as file:
                words = file.readlines()

        # Pick a random word from the file
        if not words:
            print(f"Error: {file_path} is empty!")
            return None
        return random.choice(words).strip().lower()  # Strip any leading/trailing spaces

    except Exception as e:
        print(f"Error while getting word: {e}")
        return None  # Return None if any other error occurs

def get_daily_word():
    try:
        topic = random.choice(['Fauna', 'Flora', 'Science', 'Sports', 'Countries'])
        
        # Choose file for English words
        file_path = f"{topic}_EN.txt"
        
        if not os.path.exists(file_path):  # Check if file exists
            print(f"Error: {file_path} not found!")
            return None  # Or return a default word if desired
        
        # Read the file
        with codecs.open(file_path, "r", encoding='utf-8') as file:
            words = file.readlines()
        
        # Pick a random word from the file
        if not words:
            print(f"Error: {file_path} is empty!")
            return None
        return random.choice(words).strip().lower()  # Strip any leading/trailing spaces

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