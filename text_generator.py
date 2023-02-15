import random

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

def generate_random_word():
    """Generates a random word with 3-10 letters"""
    length = random.randint(3, 10)
    word = ""
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(consonants)
        else:
            word += random.choice(vowels)
    return word

def generate_random_sentence(num_words):
    """Generates a random sentence with a specified number of words"""
    sentence = ""
    for i in range(num_words):
        sentence += generate_random_word()
        sentence += " "
    sentence = sentence.capitalize()
    sentence = sentence[:-1] + "."
    return sentence

# Generate a random sentence with 5 words
random_sentence = generate_random_sentence(5)
print(random_sentence)
