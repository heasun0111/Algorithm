str=input()
str_tmp=''

braket=False
num=False

for i in range(len(str)):
    if str[i]=='-' and braket==False:
        num = False
        braket=True
        str_tmp=str_tmp+'-'
        str_tmp = str_tmp+'('
        
    elif str[i]=='-' and braket==True:
        num = False
        str_tmp = str_tmp+')'
        str_tmp=str_tmp+'-'
        str_tmp = str_tmp+'('

    elif str[i]=='+':
        num = False
        str_tmp=str_tmp+'+'

    elif str[i]=='0' and num==False:
        continue

    else:
        num = True
        str_tmp = str_tmp+str[i]

if braket==True:
    str_tmp = str_tmp+')'

answer=eval(str_tmp)
print(answer)

