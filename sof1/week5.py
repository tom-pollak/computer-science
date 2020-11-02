# def find_sum(numbers, target):
#     pairs = []
#     for i in range(len(numbers)):
#         target_val = target - numbers[i]
#         if binary_search(numbers, 0, len(numbers) - 1, target_val):
#             # pair = set([numbers[i], target_val])
#
#             pair = [numbers[i], target_val]
#             if not any(j in pairs for j in [pair, pair[::-1]]):
#                 pairs.append(pair)
#     return pairs
#
#
# def binary_search(array, head, tail, target_val):
#     if tail >= head:
#         mid = head + (tail - head) // 2
#         if array[mid] == target_val:
#             return True
#         elif array[mid] > target_val:
#             return binary_search(array, head, mid - 1, target_val)
#         else:
#             return binary_search(array, mid + 1, tail, target_val)
#     else:
#         return False
#
#
# pairs = find_sum([-1, 1, 2, 4, 8], 7)
# print(pairs)
################################################################################


def display_dico(dico):
    for key, value in dico.items():
        print(f'{key} --> {value}')


def concat_dico(dico1, dico2):
    dic = {}
    overlap_keys = dico1.keys() & dico2.keys()
    for key in overlap_keys:
        dic[key] = [dico1[key], dico2[key]]
    for key in dico1.keys() - overlap_keys:
        dic[key] = dico1[key]
    for key in dico2.keys() - overlap_keys:
        dic[key] = dico2[key]
    return dic


def map_list(x, y):
    if len(x) != len(set(x)):
        print('ERROR: key array has duplicate values')
        return None
    return {i: j for i, j in zip(x, y)}


def reverse_dictionary(dico):
    if len(dico.values()) != len(set(dico.values())):
        print('ERROR: duplicate dictionary values')
        return None
    return {j: i for i, j in dico.items()}


def save_string(val):
    f = open('exo1.txt', 'wt')
    f.write(val)
    f.close()


def save_list2file(sentences, filename):
    f = open(filename, 'at')
    for sentence in sentences:
        f.write(sentence)
    f.close()


def save_to_log(entry, logfile):
    f = open(logfile, 'at')
    f.write(entry)
    f.close()


def to_upper_case(input_file, output_file):
    r = open(input_file, 'r')
    w = open(output_file, 'a')
    for line in r.readlines():
        w.write(line.upper())
    r.close()
    w.close()


import re


def sum_numbers(text):
    """Sums integers given in a string seperated by spaces"""
    try:
        return sum(map(lambda x: int(x), text.split()))
    except TypeError:
        print('ERROR: File contains non integers')
        return None


def sum_from_file(filename):
    """Sums integers seperated by a space from a file"""
    f = open(filename, 'r')
    text = f.read()
    return sum_numbers(text.replace('\n', ' '))


s = sum_from_file('test.txt')
print(s)
# display_dico({'un': 1, 'deux': 2, 'trois': 3})
# dic = concat_dico({'one': 1}, {'two': 2, 'one': 4})
# l = map_list(['un', 'un'], [1, 2])
# r = reverse_dictionary({'one': 1, 'two': 1})
# print(r)
#
# print(l)
