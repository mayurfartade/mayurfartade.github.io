'''
A string which is a mixture of letters ,numbers and special characters from which produce
the largest even number from the available digit after removing the duplicates digits.
If an even number did not produce then return -1.
Ex : 
infosys@337
O/p : -1
-----------------------
Hello#81@21349
O/p :984312
'''

st = input()

no = []
for i in st:
    if i.isdigit():
        no.append(int(i))

no = list(set(no))
no.sort(reverse=True)

#print(no)

if no[len(no)-1] % 2 == 1:
    for i in range(len(no)-1, 0, -1):
        if no[i]%2 == 0:
            
            no.append(no[i])
            no.remove(no[i])
            break
    else:
        print(-1)
    if no[len(no)-1]%2 == 0:
        print(no)
else:
    print(no)

