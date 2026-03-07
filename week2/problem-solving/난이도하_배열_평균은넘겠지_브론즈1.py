# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

def calc_percentile():
    score_list = list(map(int, input().split()))
    total_stu = score_list[0]
    
    score_sum = sum(score_list) - total_stu

    avg = score_sum / float(total_stu)
    cnt = 0
    
    for i in range(1, len(score_list)):
        if score_list[i] > avg:
            cnt += 1
    
    return cnt / float(total_stu)

n = int(input())

for _ in range(n):
    result = round(calc_percentile() * 100, 3)
    print(f"{result} %")