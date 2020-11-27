def sum_all(numbers):
    if isinstance(numbers, int):
        return numbers
    if not numbers:
        return 0
    return sum_all(numbers.pop(0)) + sum_all(numbers)


def wildcard(pattern, prev_pattern=''):
    if len(pattern) == 0:
        return prev_pattern
    char = pattern[0]
    if len(pattern) == 1:
        pattern = ''
    else:
        pattern = pattern[1:]
    if char == '?':
        next_pattern = wildcard(pattern)
        return add_to_arr(prev_pattern, next_pattern)
    else:
        prev_pattern += char
        return wildcard(pattern, prev_pattern)


def add_to_arr(prev_pattern, next_pattern):
    pattern_arr = []
    prev_patterns = [prev_pattern + '0', prev_pattern + '1']
    for prev in prev_patterns:
        if isinstance(next_pattern, list):
            for n_pat in next_pattern:
                pattern_arr.append(prev + n_pat)
        else:
            pattern_arr.append(prev + next_pattern)
    return pattern_arr


length_prices = {}


def rod_cutting(prices, length):
    if length == 0:
        return 0
    for cut in prices:
        if length - cut[0] >= 0:
            rec_price = rod_cutting(prices, length - cut[0])
            price = cut[1] + rec_price
        else: # only if lengths are sorted
            break
    if not str(length) in length_prices.keys() or length_prices[str(
            length)] > price:
        length_prices[str(length)] = price
        # print(length_prices)
    return length_prices[str(length)]


# pattern_arr = wildcard('1?11?00?1?')
# print(pattern_arr)
# total = sum_all([1, [2, [3, [4, [5]]]]])
# print(total)

price = rod_cutting([[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8]], 15)
# price = rod_cutting([[1, 1], [3, 2]], 5)
print(price)
