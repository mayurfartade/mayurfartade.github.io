
no = int(input())

for _ in range(no):
    st = input().split('.')
    st.reverse()
    print('.'.join(st))