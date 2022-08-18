from string import ascii_lowercase, ascii_uppercase


def cesar_cipher(text, key):
    if text == text.upper():
        alphabet = ascii_uppercase
    else:
        alphabet = ascii_lowercase

    cipher_text = ''

    for char in text:
        if char in alphabet:
            cipher_text += alphabet[(alphabet.index(char) + key) % len(alphabet)]
        else:
            cipher_text += char
    return cipher_text


def main():
    while True:
        key = int(input('Enter key: '))
        text = input('Enter text: ')
        print(cesar_cipher(text, key))


if __name__ == '__main__':
    main()
