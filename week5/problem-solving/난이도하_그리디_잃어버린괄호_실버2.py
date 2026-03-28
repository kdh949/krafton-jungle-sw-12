# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

eq = list(input().split("-"))
add = 0
minus = 0

for val in list(eq[0].split('+')):
    add += int(val)
    
for i in range(1, len(eq)):
    for minus_val in list(eq[i].split("+")):
        minus += int(minus_val)

print(add - minus)