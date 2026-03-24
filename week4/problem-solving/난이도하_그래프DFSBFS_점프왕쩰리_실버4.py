# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

# 가정 1 -> DFS
## 가능한 모든 경로 탐색 필요

n = int(input())
game_map = []
for _ in range(n):
    game_map.append(list(map(int, input().split())))
   
stack = [(0, 0)]
visited_set = set((0, 0))
while stack:
    i, j = stack.pop()
    diff = game_map[i][j]
    
    if diff == -1:
        print("HaruHaru")
        exit()
    
    nx = i + diff
    ny = j + diff
    
    if nx < n and ((nx, j)) not in visited_set:
        stack.append((nx, j))
        visited_set.add((nx, j))
    if ny < n and ((i, ny)) not in visited_set:
        stack.append((i, ny))
        visited_set.add((i, ny))

print("Hing")