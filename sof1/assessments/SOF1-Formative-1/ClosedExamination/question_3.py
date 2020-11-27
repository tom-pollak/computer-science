def sum_integers(start, end):
    if end < start or start < 0 or end < 0:
        return -1
    count = 0
    for i in range(start, end + 1):
        count += i
    return count
