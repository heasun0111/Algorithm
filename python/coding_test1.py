from queue import Queue
date=[]
cost=[]

queueD=Queue()
queueC=Queue()

def solution(purchase):
    for i in purchase:
        tmp1, tmp2 = i.split()
        date.append(tmp1)
        cost.append(int(tmp2))

    for j in range(len(date)):
        queueD.put(date[j])

    for k in range(len(date)):
        Date=queueD.get()
        year, month, day=Date.split("/")

        if (month==1) or (month==3) or (month==5) or (month==7) or (month==8) or (month==10) or (month==12):


["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"]
# [315, 9, 11, 20, 10]

["2019/01/30 5000", "2019/04/05 10000", "2019/06/10 20000", "2019/08/15 50000", "2019/12/01 100000"]
# [245, 30, 30, 30, 30]




    answer = []
    return answer