'''
Input : Given a List of numbers separated with comma.
The numbers 5 and 8 are present in the list.
Assume that 8 always comes after 5.
Case 1: num1 -> Add all numbers which do not lie between 5 and 8 in the Input List.
Case 2: num2 -> Numbers formed by concatenating all numbers from 5 to 8 in the list.
Output: Sum of num1 and num2
Example: 
3,2,6,5,1,4,8,9
Num1: 3+2+6+9 =20
Num2: 5148
O/p=5148+20 = 5168
'''

st = input().split(',')

num1 = 0
num2 = ''
temp = 0

index5 = st.index('5')
index8 = st.index('8')

num2 = ''.join(st[index5:index8+1])

num1 = int(sum(map(int,st[0:index5] + st[index8+1:len(st)])))

print(num1,int(num2)+num1)