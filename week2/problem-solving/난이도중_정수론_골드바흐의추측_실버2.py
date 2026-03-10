# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

isprime = [True] * 10001
isprime[0] = isprime[1] = False

for i in range (10001):
    if not isprime[i]:
        continue
    
    for j in range(2, 10000//i + 1):
        isprime[i*j] = False
        
def find_pairs(num):
    if (num % 2 == 0):
        a = b = num//2
    else:
        a = b = num//2
        b += 1
    
    while(True):
        if(isprime[a] == True) and (isprime[b] == True):
            break
        else:
            a -= 1
            b += 1
    if (a < b):
        return a, b
    else:
        return b, a
    
    
for _ in range(int(input())):
    a, b = find_pairs(int(input()))
    print(f"{a} {b}")