# Question: Rotate an NxN matrix 90 degrees clockwise in place.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

size = len(matrix)

for i in range(size):
    for j in range(i,size):
        matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

for i in range(size):
    matrix[i].reverse()

print(matrix)
