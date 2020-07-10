
ip = input().split(',')
string = ip[0]
specialChar = ip[1]

'''
find combinations
n(n+1)/2
'''

string = string.split(specialChar)
totalSubString = 0
for i in string:
    n = len(i)
    totalSubString += n*(n+1)/2
    
print(int(totalSubString))