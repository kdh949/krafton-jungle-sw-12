# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

blue_cnt = 0
white_cnt = 0

def slicing(i_start, i_end, j_start,j_end):#i = row, j =column
    exist_blue = False
    exist_white = False
    
    if (i_start > i_end) or (j_start > j_end):
        return
    
    for i in range(i_start, i_end+1):
        for j in range(j_start, j_end+1):
            if paper[i][j] == 1:
                exist_blue = True
            else:
                exist_white = True
            
            if exist_blue and exist_white: #두 색이 동시에 존재한다면 더 쪼개야 하므로 멈춤
                break
            
        if exist_blue and exist_white:#두 색이 동시에 존재한다면 더 쪼개야 하므로 멈춤
            break
    
    if exist_blue and exist_white:
        i_mid = (i_start + i_end) // 2
        j_mid = (j_start + j_end) // 2
        
        slicing(i_start, i_mid, j_start, j_mid)
        slicing(i_start, i_mid, j_mid + 1, j_end)
        slicing(i_mid + 1, i_end, j_start, j_mid)
        slicing(i_mid + 1, i_end, j_mid + 1, j_end)
        
    if exist_blue and not exist_white:
        global blue_cnt 
        blue_cnt += 1
    elif exist_white and not exist_blue:
        global white_cnt 
        white_cnt += 1
    
    
n = int(input())
paper = list()


for i in range(n):
    paper.append(list(map(int, input().split())))

slicing(0, n-1, 0, n-1)
print(white_cnt)
print(blue_cnt)