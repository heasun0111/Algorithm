import sys

bracket=sys.stdin.readline()
bracket=bracket.replace("()","x")

stick=0
ans=0

for i in range(len(bracket)):
    if bracket[i] == '(':
        stick = stick + 1
                      
    elif bracket[i] == ')':
        stick = stick - 1
        ans = ans + 1

    elif bracket[i] == 'x':
        ans = ans + stick


print(ans)
