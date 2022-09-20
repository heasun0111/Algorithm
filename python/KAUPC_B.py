
N=int(input())
dic={}

for _ in range(N-1):
    A, B=input().split()
    if B not in dic:
        dic[B]=[A]
    else:
        tmp_list=[]
        for i in dic.get(B):
            tmp_list.append(i)
        tmp_list.append(A)
        dic[B]=tmp_list


ans1, ans2 = input().split()

def findC(parent, child):
    if parent not in dic.keys():
        return False
    else:
        if child in dic[parent]:
            return True
        else:
            for tmp in dic[parent]:
                findC(tmp, child)

def findP(parent):
    for key in dic:
        if parent in dic[key]:
            return True
        else:
            return False

if findC(ans1, ans2)==True or findP(ans1)==True:
    print('1')
else:
    print('0')




