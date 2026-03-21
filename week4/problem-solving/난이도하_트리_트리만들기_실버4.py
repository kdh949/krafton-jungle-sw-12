# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244
# 1. 인접 행렬 생성 (Boolean)
# 2. 리프(연결 1개인 노드)만 먼저 한 개 True로, 나머지 False
# 3. 행별로 True일때만 i, j (행, 열 인덱스) 출력
## 3-1. 출력할 때 대각행렬 윗 부분만!! (어차피 무방향)


n, m = map(int, input().split())

i = 0
for j in range(1, n):
    print(i, j)
    if i < n-m:
        i += 1
