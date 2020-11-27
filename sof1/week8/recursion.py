def is_power(a, b):
    if a == b:
        return True
    if b in [0, 1]:
        return False
    if a == 1:
        return True
    if a % b == 0 and is_power(a / b, b):
        return True
    return False


def rec_sum(numbers):
    if not numbers:
        return 0
    return numbers.pop() + rec_sum(numbers)


def sum_digits(number):
    if number == 0:
        return number
    elif number < 0:
        number *= -1
    return number % 10 + sum_digits(number // 10)


def flatten(m_list):
    if isinstance(m_list, int):
        return [m_list]
    m_list = m_list[:]
    if m_list == [[]]: # if [] is last element in list
        return []
    elif not m_list:
        return m_list

    return flatten(m_list.pop(0)) + flatten(m_list)


def merge(sorted_listA, sorted_listB):
    if sorted_listA and sorted_listB:
        if sorted_listA[0] > sorted_listB[0]:
            sorted_listA, sorted_listB = sorted_listB, sorted_listA

        return [sorted_listA[0]] + merge(sorted_listA[1:], sorted_listB)
    return sorted_listA + sorted_listB


def iselfish(word, pattern=['e', 'l', 'f']):
    if pattern == []:
        return True
    if word == '':
        return False
        if word[0] not in 'elf':
            return iselfish(word[1:])
        print(word)
        return word[0] + iselfish(word[1:])
    return word


print(iselfish('whiteleaf'))

# print(merge([1, 5, 7, 8], [2, 3, 4, 5, 9]))
# print(flatten([1, [2, 3, 4], []]))

# print(sum_digits(1234))
# print(rec_sum([1, 2, 3, 4]))
# print(flatten([1, [2, [], [3]]]))
# print(sum_digits(-1))
