'''
https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/balanced-brackets-3-4fc590c6/
'''

n  =int(input())

for _ in range(n):
    s = input()

    stk = []

    opening_brackets = ['[','(','{']
    closing_brackets = [']',')','}']

    for char in s:
        if char in opening_brackets:
            stk.append(char)
        else:
            try:
                if (stk[-1] == '[' and char == ']') or (stk[-1] == '(' and char == ')') or (stk[-1] == '{' and char == '}'):
                    stk.pop()
                else:
                    print("NO")
                    break
            except:
                print("NO")
                break
    
    else:
        if len(stk):
            print("NO")
        else:
            print("YES")