from typing import List, Optional


def sum_all(n):
    if n < 0:
        return -1
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def mul_table(n):
    if n < 0:
        return -1
    for i in range(1, 11):
        print(f'{i} x {n} = {i*n}')


def factorial(n):
    if n < 0:
        return -1
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum


# sum = sum_all(10)
# print('sum_all: %s' % sum)
# mul_table(10)
# fac = factorial(10)
# print('factorial: %s' % fac)


def king_wise_man():
    SINGLE_RICE_WEIGHT = 30 * 10**-9
    NO_OF_SQUARES = 8 * 8
    no_rice = 0
    factor = 1
    for i in range(NO_OF_SQUARES):
        no_rice += factor
        factor *= 2
    rice_weight = SINGLE_RICE_WEIGHT * no_rice
    print('Weight of rice: %skg' % rice_weight)


# king_wise_man()


def scalar_product(scalar: float, vector: List[float]) -> List[float]:
    for i, dimension in enumerate(vector):
        vector[i] = dimension * scalar
    return vector


def vector_addition(vector1: List[float],
                    vector2: List[float]) -> Optional[List[float]]:
    if len(vector1) != len(vector2):
        return None

    result_vector = []
    for dimension1, dimension2 in zip(vector1, vector2):
        result_vector.append(dimension1 + dimension2)
    return result_vector


# vector = scalar_product(6.0, [1.0, 3.0, 4.0, 5.0])
# print(vector)
# vector = vector_addition([1.0, 3.0, 4.0, 5.0], [1.0, 3.0, 4.0, 5.0])
# print(vector)

sample_text = (
    " As Python s creator I d like to say a few words about its " +
    "origins adding a bit of personal philosophy " +
    "Over six years ago in December I was looking for a " +
    "hobby programming project that would keep me occupied " +
    "during the week around Christmas My office " +
    "a government run research lab in Amsterdam would be closed " +
    "but I had a home computer and not much else on my hands " +
    " I decided to write an interpreter for the new scripting " +
    "language  I had been thinking about lately a descendant of ABC " +
    "that would appeal to UnixC hackers I chose Python as a " +
    "working title for   the project being in a slightly irreverent " +
    "mood and a big fan of Monty Python s Flying Circus")


def get_words_starting_with(text, letter):
    words = sample_text.split(' ')
    found_words = set()
    for word in words:
        if word != '':
            if word[0].lower() == letter.lower():
                found_words.add(word)
    print(found_words)


get_words_starting_with(sample_text, 'a')
