matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
matrix[0][1]=20
print(matrix[0][1])

for i in matrix:
    for j in i:
        print(j)