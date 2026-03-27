# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

n = int(input())

if n <= 2:
    print(n)
    exit()

fib = [-1] * (n+1)

fib[0] = 0
fib[1] = 1

for i in range(2, n+1):
    fib[i] = fib[i-1]+fib[i-2]
    
print(fib[n])