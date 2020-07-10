
ip = input().split(',')

for i in ip:
    no = i.split(':')
    sum_no = sum(list(map(int,no[1])))
    st = no[0]
    l = len(st)
    if sum_no % 2 == 0:
        #print( ( no[0] )[len(no[0])-2:len(no[0])]+(no[0])[0:len(no)-2] ,end=' ')
        s = st[l-2:l] + st[0:l-2]
        print(s,end=' ')
    else:
        s = st[1:l] + st[0]
        print(s,end=' ')


'''
abcd:1234,bcdgfhf:127836,sdjks:1245
'''