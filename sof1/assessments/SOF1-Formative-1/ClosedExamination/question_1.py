def create_triangle(n):
    if n < 0:
        return None
    triangle = ''
    for i in range(n):
        for j in range(n):
            if i >= j:
                triangle += 'x'
            else:
                triangle += '-'
        triangle += '\n'
    return triangle
