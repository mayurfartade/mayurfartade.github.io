
ip = input()

special = []
st = []

for i in ip:
    if i.isalnum():
        st.append(i)
    else:
        special.append(i)

st.reverse()
for i in special:
    st.insert(ip.index(i),i)
print(''.join(st))

'''
import re
st = re.findall("[a-zA-Z]",ip)
st.reverse()


'''