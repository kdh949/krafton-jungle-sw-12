# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

max_val = 0
max_idx = 0

for i in range(9):
    num = int(input())
    if(max_val < num):
        max_val = num
        max_idx = i + 1
    
print(max_val)
print(max_idx)