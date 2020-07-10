from itertools import combinations as com

n = int(input())
array = list(map(int, input().split()))

array.sort()

if(len(array)>1):
    co = list(com(array[1:len(array)],2))
    diff = []
    if len(co):
        for j in co:
            diff.append(abs(j[0]-j[1]))
        if array[0] in diff:
            print(0)
        else:
            di = array[1] - array[0]
            if len(array) > 2:
                co = list(com(array[2:len(array)],2))
                if len(co):
                    for j in co:
                        diff.append(abs(j[0]-j[1]))
                    if di in diff:
                        print(0)
                    else:
                        di = array[1] - array[0]
                        x = [x for x in array if x < di]
                        if len(x):
                            print(min(x))
                        else:
                            print(di)
                else:
                    di = array[1] - array[0]
                    x = [x for x in array if x < di]
                    if len(x):
                        print(min(x))
                    else:
                        print(di)
            else:
                x = [x for x in array if x < di]
                if len(x):
                    print(min(x))
                else:
                    print(di)
    else:
        di = array[1] - array[0]
        x = [x for x in array if x < di]
        if len(x):
            print(min(x))
        else:
            print(di)
else:
    print(array[0])

'''
    first_diff = array[0:]
    co = list(com(array[i+1:len(array)],2))
    
    if len(co):
        for j in co:
            diff.append(abs(j[0]-j[1]))
        if first_diff diff:
            print(0)
            break
'''