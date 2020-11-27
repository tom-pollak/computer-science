import random


def scramble(word):
    if len(word) <= 5:
        return word
    mid = list(word[2:-2])
    random.shuffle(mid)
    return word[:2] + ''.join(mid) + word[-2:]
