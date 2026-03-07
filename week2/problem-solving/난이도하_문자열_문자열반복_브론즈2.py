# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

test_case = int(input())

for _ in range(test_case):
    n, str = input().split(" ")
    n = int(n)
    
    result = ""
    for c in str:
        for _ in range(n):
            result+=c
    
    
    print(result)