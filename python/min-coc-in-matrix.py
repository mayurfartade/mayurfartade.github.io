
r,c = map(int,input().split())

list_dig = []

matrix = []
for i in range(r):
    matrix.append(list(map(int,input().split())))

for i in range(r):
    for j in range(c):
        #row wise
        if j <= c-4:
            if matrix[i][j] == matrix[i][j+1] == matrix[i][j+2] == matrix[i][j+3]:
                list_dig.append(matrix[i][j])

        #column wise
        if i <= r-4:
            if matrix[i][j] == matrix[i+1][j] == matrix[i+2][j] == matrix[i+3][j]:
                list_dig.append(matrix[i][j])
        
        #diagonally /
        if i > 2 and j > 2:
            if matrix[i][j] == matrix[i-1][j-1] == matrix[i-2][j-2] == matrix[i-3][j-3]:
                list_dig.append(matrix[i][j]) 

        #diagonally \
        if i >= 3 and j <= c-4:
            if matrix[i][j] == matrix[i-1][j+1] == matrix[i-2][j+2] == matrix[i-3][j+3]:
                list_dig.append(matrix[i][j]) 

print(list_dig)
print(min(list_dig))