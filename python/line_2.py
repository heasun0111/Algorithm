from itertools import permutations

arr=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

print(list(permutations(arr,15)))




# 조합은 DFS이용해서 풀 수 있다
# DFS, BFS 등 그래프 탐색도 공부!!