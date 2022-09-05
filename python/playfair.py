import numpy as np

message=input()
cipher_K=input()

cipher_list=[]
for i in range(len(cipher_K)):
    if cipher_K[i] not in cipher_list:
        cipher_list.append(cipher_K[i])
    else:
        continue

for j in range(26):
    if chr(65+j) not in cipher_list and chr(65+j)!='J':
        cipher_list.append(chr(65+j))
    else:
        continue

cipherList=np.reshape(cipher_list, (5,5))


# message를 2개씩 쪼개서 암호화하는거 구현!
def makeCipherStr(a,b):
    return 0

for i in range(len(message)/2):
    a=1
