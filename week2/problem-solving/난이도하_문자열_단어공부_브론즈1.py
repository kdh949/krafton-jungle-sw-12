# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

str = input().upper()
cnt = [0]*26d

for c in str:
    cnt[ord(c)-65] += 1

max_idx = 0
max_val = 0
nxt_idx = 0
nxt_val = 0


for i in range(26):
    if (max_val < cnt[i]):
        max_idx = i
        max_val = cnt[i]
    elif (nxt_val < cnt[i]):
        nxt_idx = i
        nxt_val = cnt[i]
        
if (max_val == nxt_val):
    print("?")
else:
    print(chr(max_idx+65))