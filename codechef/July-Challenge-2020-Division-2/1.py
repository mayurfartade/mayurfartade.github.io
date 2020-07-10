
'''
@Author: Mayur Fartade

Problem Link: https://www.codechef.com/JULY20B/problems/CHEFSTR1
'''

# cook your dish here

try:
    for _ in range(int(input())):
        N = int(input())
        S = list(map(int, input().strip().split()))
        
        skip = 0
        for i in range(N-1):
            if S[i] == S[i+1]:
                exit()
            skip += abs(S[i]-S[i+1])-1
        print(skip)

except:
    pass