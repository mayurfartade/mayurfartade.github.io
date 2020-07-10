'''
Hands-on Coding Question I:- Pronic Number

Given a string in which random numbers are present and we have to find the product and the number(one is lesser and one is greater) 
who already present in the string. Confusing,  Let’s see the example:

E.g. Given a string contains 1203456. The multiplication of 3 and 4(one is lesser and one is greater) product become 12 and 
it’s present in the string. Like 4 and 5(one is lesser and one is greater) the product is 20 and it’s present in the string and so on. 
In such a way, We have to find all the numbers and in the output just we have to store the only product in the list like[ ’12’, ’20’].

If we haven’t found the product then print -1.
'''

ip = input()

no = list(map(int,ip))
no.sort()

result = []

for i in range(len(no)):
    for j in range(i+1, len(no)):
        if str(no[i]*no[j]) in ip:
            result.append(str(no[i]*no[j]))

print(list(set(result)))