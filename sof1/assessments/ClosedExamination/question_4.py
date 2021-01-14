def check_level(level):
    if len(level) == 0 or level[0] == 0:
        return False
    if len(level) == 1:
        return True

    for i in range(1, level[0] + 1):
        valid = check_level(level[i:])
        if valid:
            return True
    return False
