# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

def isprime(n): #True: 소수
    if n == 1:
        return False
    
    if (n % 2 != 0):
        for i in range(3, round(n**0.5)+1):
            if(n%i == 0):
                return False
            
    else:
        for i in range(2, round(n**0.5)+1):
            if(n%i == 0):
                return False
    
    return True

input()
nums = list(map(int, input().split()))
cnt = 0
for n in nums:
    if isprime(n):
        cnt += 1
        
print(cnt)