
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
new_matrix = []

size = len(matrix)
for i in range(size):
    row = []
    for j in range(size):
        row.append(matrix[j][i])
    new_matrix.append(row)

for i in range(size):
    new_matrix[i].reverse()

print(new_matrix)
