def max_sub_list(arr):
    max_sum = 0
    cur_sum = 0
    for number in arr:
        if cur_sum + number > 0:
            cur_sum += number
            if cur_sum > max_sum:
                max_sum = cur_sum
        else:
            cur_sum = 0
    return max_sum


# def get_sum(matrix, top, bot):
#     mat_sum = 0
#     for i in range(top[0], bot[0] + 1):
#         for j in range(top[1], bot[1] + 1):
#             mat_sum += matrix[i][j]
#     return mat_sum


def get_rec(matrix, max_sum, i, j):
    subgraphs = [0 for z in matrix[i]]
    for k in range(i, len(matrix)):
        mat_sum = 0
        for l in range(j, len(matrix[i])):
            mat_sum += matrix[k][l]
            if mat_sum + subgraphs[l] > max_sum:
                max_sum = mat_sum + subgraphs[l]
            subgraphs[l] += mat_sum
            # optimisation: if a subgraph has a negative total then the program
            # does not create anymore subgraphs which incorporate that subgraph
            # elif mat_sum < 0:
            #     bp = l
            #     break
    return max_sum


def max_sub_matrix(matrix):
    max_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            max_sum = get_rec(matrix, max_sum, i, j)
    return max_sum


matrix = [
    [6, -5, -7, 4, -4],
    [-9, 3, -6, 5, 2],
    [-10, 4, 7, -6, 3],
    [-8, 9, -3, 3, -7],
]
max_sum = max_sub_matrix(matrix)
print(max_sum)

# max_sum = max_sub_list([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# print(max_sum)
