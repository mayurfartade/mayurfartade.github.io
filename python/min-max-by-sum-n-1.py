
n = int(input())
nos = list(map(int,input().split()))

nos.sort()
minSum = sum(nos[0:n-1])
maxSum = sum(nos[1:n])
print(minSum, maxSum)