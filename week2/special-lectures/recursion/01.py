def nsum(n):
    return ((n+1)*n)/2

def recursion_sum(n):
    # base condition 
    if n <= 0:
        return 0
    
    return n+recursion_sum(n-1)

print(int(nsum(10)))
print(int(recursion_sum(10)))

# tail recursion
## 이 케이스는 중간에 멈춰도 확인할 수 있음 (종 모양의 띄지 않는다.)
## 단, 파이썬은 recursion 보다는 iteration(반복)을 사용할 것을 권장함!
def sum_iter(n, total):
    if n == 0:
        return total
    
    else:
        return sum_iter(n-1, total+n)
    
    
def sum(n):
    return sum_iter(n, 0)

# 거듭제곱
## base condition
### b^n = b*b^(n-1)
### b^0 = 1

def exp(b, n):
    if n == 0:
        return 1
    return b*exp(b, n-1)

def exp_iter(b, n, total):
    if n == 0:
        return total
    
    return exp_iter(b, n-1, total*b)

def exponential():
    return exp_iter(3, 2, 1)

print(exponential())

# 복잡한 경우 어쩔 수 없이 재귀를 사용해야 함
## 속도를 최적화하기 위한 방법이 필요
## 예를 들어 거듭제곱에서
# n이 짝수라면: b^n = (b^(n/2))^2
# n이 홀수라면: b^n = b*b^(n-1)

def fast_exp(b, n):
    #### base condition!!!!! 너무 중요!!! #####
    if n == 0:
        return 1
    if(n % 2 == 0):
        return (fast_exp(b, (n/2)))**2
    else:
        return b*fast_exp(b, n-1)
        
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# Counting Change Problem
def count_change_case(result, target, combination_arr, sum):
    if(target == sum):
        result.append(combination_arr)
        sum -= combination_arr.pop()
        return
    
    elif target < sum:
        sum -= combination_arr.pop()
        return
    
    else:
        pass
    
    
def count_changes(amount, coins):
    if amount == 0:
        return 1
    
    if amount < 0 or len(coins) == 0:
        return 0
    
    return count_changes(amount, coins[1:]) + count_changes(amount-coins[0], coins)

##하노이탑 문제 풀어보기!!!!