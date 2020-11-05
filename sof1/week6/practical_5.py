semple_text = (
    " As Python s creator, I'd like to say a few words about its " +
    "origins adding a bit of personal philosophy. " +
    "Over six years ago in December I was looking for a " +
    "hobby programming project that would keep me occupied " +
    "during the week around Christmas. My office, " +
    "a government run research lab in Amsterdam would be closed " +
    "but I had a home computer and not much else on my hands " +
    " I decided to write an interpreter for the new scripting " +
    "language  I had been thinking about lately a descendant of ABC " +
    "that would appeal to UnixC hackers I chose Python as a " +
    "working title for   the project being in a slightly irreverent " +
    "mood and a big fan of Monty Python s Flying Circus.  ")

######################### EXERCISE 1 ##########################################


def split_text(text, separators):
    tokens = []
    start = 0
    for i, letter in enumerate(text):
        if letter in separators:
            if text[start:i] != '':
                tokens.append(text[start:i])
                start = i + 1
            else:
                start = i + 1

    if start != len(text):
        tokens.append(text[start:])
    return tokens


import string


def get_words_frequencies(text):
    text = text.lower()
    words = {}
    splitters = string.punctuation + ' '
    splitters = splitters.replace("'", '')
    tokens = split_text(text, splitters)
    for word in tokens:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words


def flatten(list_2D):
    l = []
    for arr in list_2D:
        for el in arr:
            l.append(el)
    print(l)
    return l


def rasterise(list_1D, width):
    list_2D = []
    if len(list_1D) % width != 0:
        return None
    for i in range(len(list_1D) % width):
        temp = []
        for j in range(i, i + width):
            temp.append(list_1D[j])
        list_2D.append(temp[:])
    print(list_2D)
    return list_2D


rasterise([1, 2, 3, 4, 5, 6, 7, 8], 4)
