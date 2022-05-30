a, b = map(int, input().strip().split(' '))

star=[]
for i in range(a):
    star.append('*')
str_star="".join(star)

for j in range(b):
    print(str_star)