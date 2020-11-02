import string


def even_numbers():
    numbers = input('Enter a series of numbers: ')
    numbers = numbers.split(' ')
    even = set()
    for number in numbers:
        if int(number) % 2 == 0:
            even.add(number)

    print(f'There are {len(even)} distinct even numbers:', end='')
    for number in even:
        print(f' {number}', end='')
    print()


def draw_sudoku():
    numbers = []
    for i in range(4):
        row = input('enter 4 digits (0..4) seperated by a space: ')
        numbers.append(row.split(' '))

    for row in numbers:
        print('+-+-+-+-+')
        for number in row:
            if number == '0':
                number = ' '
            print('|%s' % number, end='')
        print('|')
    print('+-+-+-+-+')


def convert_bin():
    number = int(input('Enter a number: '))
    binary = ''
    while number != 0:
        binary += str(number % 2)
        number = number // 2
    print(binary)


def palindrome():
    sentence = input('Enter a sentence: ').lower()
    for punctuation in string.punctuation:
        sentence = sentence.replace(punctuation, '')
    sentence = sentence.replace(' ', '')
    print(sentence)

    pal = ''
    for i in range(len(sentence) // 2):
        if sentence[i] != sentence[i * -1 - 1]:
            pal = 'not '

    print('%s is %sa palindrome' % (sentence, pal))


def camel_case():
    sentence = input('Enter a sentence: ')
    words = sentence.split(' ')
    camel_case = ''
    for word in words:
        camel_case += (word[0].upper() + word[1:])

    # camel_case = camel_case[0].lower() + camel_case[1:]
    print(camel_case)


def un_camel_case():
    camel_case = input('Enter a sentence in CamelCase: ')
    index = 0
    word_list = []
    for i in range(len(camel_case)):
        if camel_case[i] in string.ascii_uppercase:
            word = camel_case[index:i]
            word_list.append(word)
            index = i

    word = camel_case[index:i + 1]
    word_list.append(word)
    del word_list[0]
    print(word_list)


def caesar_cipher():
    alphabet = string.ascii_lowercase
    plain_text = input('Enter a message: ')
    shift = int(input('Enter shift: '))
    cipher_text = ''
    for letter in plain_text:
        letter_index = (alphabet.index(letter) + shift) % 26
        cipher_text += alphabet[letter_index]
    print(cipher_text)


def un_caesar_cipher():
    alphabet = string.ascii_lowercase
    cipher_text = input('Enter a caesar cipher: ')
    shift = int(input('Enter shift: '))
    plain_text = ''
    for letter in cipher_text:
        letter_index = (alphabet.index(letter) - shift) % 26
        plain_text += alphabet[letter_index]
    print(plain_text)


# even_numbers()
# draw_sudoku()
# convert_bin()
# palindrome()
# camel_case()
# un_camel_case()
# caesar_cipher()
# un_caesar_cipher()
