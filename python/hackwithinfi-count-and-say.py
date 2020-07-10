
def countAndsay(n,no):
    if n==0:
        return
    i = 0
    l = len(no)
    print(no)
    new = ""
    start = i
    count = 1
    while i<l-1:
        if no[i] == no[i+1]:
           count+=1
        else:
            new += str(count)+no[start]
            count = 1
            start = i+1
        i += 1
    new += str(count)+no[start]
    countAndsay(n-1,new)

no = str(1)
n = int(input())

countAndsay(n,no)
    