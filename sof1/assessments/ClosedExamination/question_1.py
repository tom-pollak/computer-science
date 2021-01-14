def encrypt(message, shifts, alphabet):
    """Returns encrypted message using the caesar cipher algorithm.

    Args:
        message (str): Plaintext message to be encrypted
        shifts (list): List of shift values for each character in message.
        alphabet (list): List of characters avaliable to be used in message 

    Exceptions:
        ValueError: If the size of shifts is not the same as the size of the
            alphabet
        ValueError: A character in message is not in alphabet
        ValueError: shifts contains a negative value
        ValueError: shifts contains value which is greater than the size of
            alphabet
    """
    cipher_message = ''
    if len(message) != len(shifts):
        raise ValueError('Size of shifts is not the same as size of alphabet')

    for index, character in enumerate(message):
        alphabet_index = alphabet.find(character)
        if alphabet_index == -1:
            raise ValueError('Character in message not in alphabet')

        no_shifts = shifts[index]
        if no_shifts >= len(alphabet) or no_shifts < 0:
            raise ValueError(
                'Shifts contains negative value or shift is greater than size of alphabet'
            )

        cipher_index = (alphabet_index + no_shifts) % len(alphabet)
        cipher_message += alphabet[cipher_index]
    return cipher_message
