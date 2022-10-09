import random
from typing import Tuple

try:
    from .lfsr_machine import LsfrMachine
except ImportError:
    from lfsr_machine import LsfrMachine


def decrypt_key(lsfr_machine: LsfrMachine, message: list[int]) -> list[int]:
    ciphertext = lsfr_machine(message)
    key = list(map(lambda x: x[0] ^ x[1], zip(message, ciphertext)))
    return key


def test_decrypt():
    secret_key = [random.randint(0, 1) for i in range(15)]
    print(f"Initial key: {secret_key}")
    lsfr_machine = LsfrMachine(secret_key)
    reconstructed_key = decrypt_key(lsfr_machine, [random.randint(0, 1) for i in range(15)])
    print(f"found key:   {reconstructed_key}")
    assert secret_key == reconstructed_key
