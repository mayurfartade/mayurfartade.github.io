

def BFS(matrix):
    temp = []
    for _ in range(4):
        temp.append([False]*4)

    q = [(0,0)]
    while len(q):
        
        vis = q.pop(0)
        r = vis[0]
        c = vis[1]
        

        if r < 0 or c < 0 or r >= 4 or c >= 4 or  temp[r][c]:
            continue

        print(matrix[r][c], end=" ")
        temp[r][c] = True

        q.append((r-1,c))
        q.append((r+1, c))
        q.append((r, c-1))
        q.append((r, c+1))
        
            


matrix = []

for i in range(4):
    matrix.append(list(map(int, input().split())))

BFS(matrix)
print()