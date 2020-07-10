
ip = input()
def validate(ip):
    st = []

    counter = 0
    for i in ip:
        if i == '[' or i == '(' or i == '{':
            st.append(i)
            counter += 1
            continue
        if len(st) == 0:
            return counter + 1
        
        top = st.pop()
        if top == '[' and i == ']':
            counter += 1
        elif top == '(' and i == ')':
            counter += 1
        elif top == '{' and i == '}':
            counter += 1
        else:
            return counter+1
    if len(st) == 0:
        return 0
    else:
        return counter+1

print(validate(ip))