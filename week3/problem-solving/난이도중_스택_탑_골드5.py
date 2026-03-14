# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

n = int(input())
num_list = list(map(int, input().split()))
count_stack = ['']*n

tmp_stack = list()

now = num_list.pop()

for i in range(n-2, -1, -1):
    next = num_list.pop()
    
    if (next >= now):
        top_idx = i
        count_stack[i+1] = top_idx + 1
        
        while(tmp_stack):
            tmp = tmp_stack.pop()
            if (next >= tmp['value']):
                idx = tmp['idx']
                count_stack[idx] = top_idx + 1
                
            else:
                tmp_stack.append({"value": tmp['value'], "idx": tmp['idx']})
                break
    else:
        tmp_stack.append({"value": now, "idx": i+1})
        count_stack[i+1] = 0
        
    now = next

count_stack[0]=0

print(*count_stack, end=' ')
print()