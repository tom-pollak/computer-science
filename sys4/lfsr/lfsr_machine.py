from typing import Callable


class LsfrMachine:
    """
    Returns an encryption oracle function (like the pseudocode)
    Win condition: Guess what value comes out next from the oracle returned

    Creates a new lfsr machine that only encrypts messages through encrypt_message
    Secure provided you don't mess with the internal state
    """

    def __init__(self, key: list[int]):
        self.__key = key

    def __xor_shift_bit(self, check_bit: int) -> int:
        end_bit = self.__key.pop()
        new_bit = check_bit ^ end_bit
        self.__key.insert(0, new_bit)
        return new_bit

    def encrypt_ciphertext(self, message: list[int]) -> list[int]:
        """
        Enc_K(M) -> C
        """
        assert len(message) == len(
            self.__key
        ), f"Length of message must be {len(self.__key)}"
        ciphertext = list(map(lambda x: x[0] ^ x[1], zip(message, self.__key)))
        # It should only shift the bit *once* per message
        self.__xor_shift_bit(message[-1])
        return ciphertext

    def __call__(self, m: list[int]) -> list[int]:
        return self.encrypt_ciphertext(m)


def test_lfsr_machine():
    import random

    cipher_length = 15
    random_message = lambda: [random.randint(0, 1) for i in range(cipher_length)]
    lsfr_machine = LsfrMachine(random_message())
    cipher_random_message = lambda: lsfr_machine(random_message())
    prev_cipher = cipher_random_message()
    for i in range(100):
        cipher = cipher_random_message()
        assert len(cipher) == cipher_length
        assert prev_cipher != cipher, "Ciphers should be different (not guarateed!)"
        prev_cipher = cipher[:]

def test_lfsr_zero():
    cipher_length = 15
    zero_message = [0 for _ in range(cipher_length)]
    lsfr_machine = LsfrMachine(zero_message)
    for _ in range(10):
        c = lsfr_machine(zero_message)
        assert c == zero_message

def test_simulate_input():
    cipher_length = 15
    # write out by hand
