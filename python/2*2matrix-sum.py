row = int(input())
column = int(input())
matrix = []
for i in range(row):
    matrix.append(input().split())

def isDivisible(no):
    if int(no)%sum(list(map(int,no))) == 0:
        return True
    return False
    
for i in range (row):
    for j in range (column):
        if i+1 < row and j+1 < column:
           if isDivisible(matrix[i][j]) and isDivisible(matrix[i][j+1]) and isDivisible(matrix[i+1][j]) and isDivisible(matrix[i+1][j+1]):
               print()
               print(matrix[i][j],matrix[i][j+1])
               print(matrix[i+1][j],matrix[i+1][j+1])

            