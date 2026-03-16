# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

n = int(input())
pass_set = set()

for i in range(n):
    password = input()
    pass_set.add(password)

    if password[::-1] in pass_set:
        pass_len = len(password)
        print(pass_len, end=' ')
        print(password[pass_len//2])
        break