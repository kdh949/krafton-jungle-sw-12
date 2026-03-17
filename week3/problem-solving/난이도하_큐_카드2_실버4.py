# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

# 수식 버전
import math

n = int(input())

if n == 1:
    print(1)
    
else:
    last_max = 2**int(math.log2(n))
    result = (n-last_max)*2
    if result == 0 :
        print(n)
    else:
        print(result)

# 덱 버전

from collections import deque

n = int(input())
queue = deque(range(1, n + 1)) # 1부터 N까지의 카드를 큐에 넣음

while len(queue) > 1:
    queue.popleft()            # 제일 위에 있는 카드를 버림
    queue.append(queue.popleft()) # 그 다음 카드를 뽑아서 제일 아래로 옮김

print(queue[0])