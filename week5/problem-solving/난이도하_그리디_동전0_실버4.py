# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())

coins = [0]*n

for i in range(n):
    coins[i] = int(input())

result = 0
left_coins = k

for j in range(n-1, -1, -1):
    result += left_coins // coins[j]
    left_coins %= coins[j]
    
    if left_coins == 0:
        break

print(result)