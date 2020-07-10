'''
@Author: Mayur Fartade

Problem Link: https://www.codechef.com/JULY20B/problems/CRDGAME
'''

# cook your dish here

try:
    for _ in range(int(input())):
        N = int(input())
        chef_points = 0
        morty_points = 0
        
        for x in range(N):
            A,B = input().strip().split()
            A = list(map(int, A))
            B = list(map(int, B))
            
            sum_A = sum(A)
            sum_B = sum(B)
            
            if sum_A > sum_B:
                chef_points += 1
            elif sum_B > sum_A:
                morty_points += 1
            else:
                chef_points += 1
                morty_points += 1
            
        if chef_points > morty_points:
            print(0, chef_points)
        elif morty_points > chef_points:
            print(1, morty_points)
        else:
            print(2, chef_points)

except:
    pass
