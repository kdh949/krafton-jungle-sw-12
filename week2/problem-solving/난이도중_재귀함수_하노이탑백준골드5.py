# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

cnt = 0
move_list = []

def hanoi(n, start, aux, end):
    global cnt
    # cnt += 1
    
    # if(n == 1):
    #     return
    
    # hanoi(n-1, start, end, aux)
    # hanoi(n-1, aux, start, end)
    
    for i in range(n):
        cnt += 2**i
    
def hanoi_under(n, start, aux, end):
    global cnt
    cnt += 1
    
    if(n == 1):
        # start -> end
        move_list.append([start, end])
        return
    
    hanoi_under(n-1, start, end, aux)
    move_list.append([start, end])
    hanoi_under(n-1, aux, start, end)

    
n = int(input())

if (n > 20):  
    hanoi(n, 1, 2, 3)
    print(cnt)
else:
    hanoi_under(n, 1, 2, 3)
    print(cnt)
    for arr in move_list:
        print(f"{arr[0]} {arr[1]}")