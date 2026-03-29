# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904
import sys

input = sys.stdin.readline

n = int(input().strip())

curr_tile = 1
result = 0

for _ in range(n+1):
    curr_tile, result = result, (curr_tile+result)%15746

print(result)