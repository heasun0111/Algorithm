import re

def palindrome(str):
    flag=True
    for i in range(len(str)//2):
        if str[i] != str[-1-i]:
            flag=False
            break
    return flag

def solution(s):
    ans=[]
    for str in s:
        alpha= re.sub(r'[^A-Z-a-z]','', str)
        numbers = re.sub(r'[^0-9]','', str)
        special_S= re.sub(r'[^!@#$%^&*]','', str)
        alpha=alpha.upper()

        if palindrome(alpha)==True and palindrome(numbers)==True and palindrome(special_S)==True:
            ans.append(len(str))
        else:
            ans.append(0)
    answer=max(ans)
    return answer

#print(solution(["!@ab12cCbA21@!!!!!", "!@ab12cCbA21@!", "ab12cCbA21"]))
#print(solution(["!@ab12cCbA21@!"]))