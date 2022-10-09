import random
from typing import Callable, List, Tuple


class LsfrMachine:
    """
    Creates a new lfsr machine that only encrypts messages through encrypt_message
    Secure provided you don't mess with the internal state (don't touch oracle!)
    """
    def __init__(self, key: list[int]):
        self.__oracle = LsfrMachine.create_lfsr_machine(key)

    @staticmethod
    def create_lfsr_machine(key: list[int]) -> Callable[[list[int]], list[int]]:
        """
        Returns an encryption oracle function (like the pseudocode)
        Win condition: Guess what value comes out next from the oracle returned
        Returns: Enc_K(M) -> C
        """

        def xor_shift_state(check_bit: int) -> int:
            end_bit = key.pop()  # NOTE: Uses the global state
            new_bit = check_bit ^ end_bit
            key.insert(0, new_bit)
            return new_bit

        def encrypt_ciphertext(m: list[int]) -> list[int]:
            return list(map(xor_shift_state, m))

        return encrypt_ciphertext

    def encrypt_message(self, m: list[int]) -> list[int]:
        return self.__oracle(m)


lsfr = LsfrMachine([random.randint(0, 1) for i in range(15)])


def calc_s(m: list[int], initial_state: list[int]) -> Tuple[list[int], int]:
    n = get_count_flush_s(initial_state, m)
    state, num_steps = calc_s_bit(m[:n], m[n:])
    assert (
        n == num_steps
    ), f"""n and num_steps should equal
    - I think num_steps should be the same as n since they both require a full pass through the data"""
    return state, n + num_steps

"""
Mental model of lfsr:
>  ^ X_2 <-----
|             |
XXXXXXXXXXXXXXX -> X (random)

Giving *known* random input into the system
---------------
|             |
RRRRRRRRRRRRRXX -> X (Random)

Still unknowable:
Boom! now we can simulate :)
-------0-------
|             |
RRRRRRRRRRRR111 -> R ^ R_{n-15}


WRONG!
Actuall its more like
c_i <- m_i ^ s_i

for message s_i in s:
match m_i {
    0 => {
        match c_i {
            0 => {
                // s_i = 0
            },
            1 => {
                // s_i = 1
            }
        }
    },
    1 => {
        match c_i {
            1 => {
                // s_i = 1
            },
            0 => {
                // s_i = 0
            }
        }
    }
}


"""


def calc_s_bit(m: list[int], initial_state: list[int]) -> Tuple[list[int], int]:
    """
    secret bit shifts forward left everytime
    """
    raise NotImplemented


def flush_key(oracle, message_queue: list[list[int]]) -> Tuple[list[int], list[list[int]]]:
    """
    This should be the length of random_state I think
    """
    
    for i in range(key_length):
        oracle()

