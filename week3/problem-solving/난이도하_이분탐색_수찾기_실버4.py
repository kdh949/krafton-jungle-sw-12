# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

## 이분탐색 버전
def bin_search(num_list, find_num):
    start = 0
    end = len(num_list) - 1
    
    while(start <= end):
        mid = (start + end) // 2
              
        if num_list[mid] == find_num:
            return 1
        
        if find_num < num_list[mid]:
            end = mid - 1
        else:
            start = mid + 1
            
    return 0
            
    
n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))

for find in b:
    print(bin_search(a, find))