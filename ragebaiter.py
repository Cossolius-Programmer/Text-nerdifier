import random

def nerdify(text: str, strength: float) -> str:
    if 0 >= strength >= 1:
        raise ValueError('Strength must be between 0 and 1')
    new_text = ''
    for char in text:
        if char not in '0123456789':
            new_text += char.upper() if random.random() < strength else char
        else:
            new_text += char
    return new_text

while True:
    message = input('Enter a message: ')
    if message == '':
        print()
        print("Ok we done.")
        break
    print(nerdify(message, 0.52))
