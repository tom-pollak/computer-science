import random
from typing import Tuple

try:
    from .lfsr_machine import LsfrMachine
except ImportError:
    from lfsr_machine import LsfrMachine


def decrypt_key(lsfr_machine: LsfrMachine, message: int) -> int:
    ciphertext = lsfr_machine(message)
    key = message ^ ciphertext
    return key


def test_decrypt():
    cipher_length = 15
    random_message = lambda: random.randint(0, 2**cipher_length - 1)

    secret_key = random_message()
    print(f"Secret key: {secret_key}")

    lsfr_machine = LsfrMachine(secret_key, cipher_length)
    reconstructed_key = decrypt_key(
        lsfr_machine, random_message()
    )

    print(f"Found key:  {reconstructed_key}")
    assert secret_key == reconstructed_key


def test_question_7():
    message = 0b00000000001111111111
    ciphertext = 0b01111011011001001010
