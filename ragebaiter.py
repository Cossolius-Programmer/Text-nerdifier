from random import random

def nerdify(text: str, strength: float) -> str:
    if 0.0 >= strength >= 1.0:
        raise ValueError('Strength must be between 0 and 1')
    new_text: str = ''
    for char in text:
        if char not in '0123456789':
            new_text += char.upper() if random() < strength else char
        else:
            new_text += char
    return new_text

while True:
    message: str = input('Enter a message: ')
    if message == '': # need to stop program
        print()
        print("Ok we done.")
        break # self close
    print(nerdify(message, 0.52)) # copy paste this to make the other person think you're mocking them
