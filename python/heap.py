import heapq

def solution(scoville, K):
    cnt=0
    heapq.heapify(scoville)
    while scoville[0]<=K and len(scoville)>1:
        cnt = cnt+1
        tmp1=heapq.heappop(scoville)
        tmp2=heapq.heappop(scoville)
        tmp3=tmp1+(tmp2*2)
        heapq.heappush(scoville,tmp3)

    if scoville[0]<K:
        return -1

    else:
        return cnt

# heapq.heappop()을 이용하면 원소 제거
# 제거 안하려면 scoville[0]로 확인
# K이상이면 x <= K으로 확인

