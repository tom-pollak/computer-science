from typing import Callable


class LsfrMachine:
    """
    Returns an encryption oracle function (like the pseudocode)
    Win condition: Guess what value comes out next from the oracle returned

    Creates a new lfsr machine that only encrypts messages through encrypt_message
    Secure provided you don't mess with the internal state
    """

    def __init__(self, initial_key: int, key_length: int):
        self.__key: int = initial_key
        self.max_val: int = 2**key_length - 1

    def xor_shift_bit(self, comp_bit: int) -> int:
        assert comp_bit in [0, 1], f"comp bit: {comp_bit} must be 0 or 1"
        key_list = [c for c in self.num2binstr(self.__key)]

        end_bit = int(key_list.pop())
        new_bit = comp_bit ^ end_bit
        key_list.insert(0, str(new_bit))

        self.__key = int("".join(key_list), 2)
        assert self.__key <= self.max_val
        return new_bit

    def encrypt_message(self, message: int) -> int:
        """
        Enc_K(M) -> C
        """
        assert message <= self.max_val, f"Message must be less than {self.max_val}"
        ciphertext = message ^ self.__key

        # It should only shift the bit *once* per message
        self.xor_shift_bit(int(self.num2binstr(message)[-1]))
        return ciphertext

    @staticmethod
    def num2binstr(n: int) -> str:
        return "{0:b}".format(n)

    def __call__(self, m: int) -> int:
        return self.encrypt_message(m)


def test_lfsr_machine():
    import random

    cipher_length = 15
    max_val = 2**cipher_length - 1
    lsfr_machine = LsfrMachine(random.randint(0, max_val), cipher_length)
    cipher_random_message = lambda: lsfr_machine(random.randint(0, max_val))
    prev_cipher = cipher_random_message()
    for i in range(100):
        cipher = cipher_random_message()
        assert cipher <= max_val
        assert prev_cipher != cipher, "Ciphers should be different (not guarateed!)"
        prev_cipher = cipher


def test_lfsr_zero():
    cipher_length = 15
    lsfr_machine = LsfrMachine(0, cipher_length)
    for _ in range(10):
        c = lsfr_machine(0)
        assert c == 0


def test_simulate_input():
    cipher_length = 15
    # write out by hand
