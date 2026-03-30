# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

def combination_coins(n, m, coins):
    dp = [0]*(m+1)
    dp[0] = 1 # 아무것도 사용하지 않는 케이스도 경우의 수
    
    for coin in coins:
        for j in range(coin, m+1):
            dp[j] = dp[j] + dp[j-coin]

    return dp[m]

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    
    print(combination_coins(n, m, coins))