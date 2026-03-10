# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

# ipv6 = "25:09:1985:aa:091:4846:374:bb"
# ipv6 = "2001:db8:85a3::8a2e:370:7334"
# ipv6 = "::1"

ipv6 = input()

ipv6_list = list(map(str, ipv6.split(":")))
if (len(ipv6_list) > 8):
    idx = ipv6_list.index('')
    ipv6_list[idx] = '0000'
    idx = ipv6_list.index('')
    
    if ('' in ipv6_list): # "1:2:3:4:5:6:7::" 케이스용
        ipv6_list.remove('')

elif (len(ipv6_list) < 8):
    idx = ipv6_list.index('')
    ipv6_list[idx] = '0000'
    if ('' in ipv6_list): # "::1" 케이스용
        idx = ipv6_list.index('')
        ipv6_list[idx] = '0000'
    n = len(ipv6_list)
    
    for _ in range(8-n):
        ipv6_list.insert(idx, '0000')
        
for i in range(8):
    if (len(ipv6_list[i]) != 4):
        append = '0'*(4-len(ipv6_list[i]))
        ipv6_list[i] = append + ipv6_list[i]

print(f"{ipv6_list[0]}", end='')
for val in range(1, len(ipv6_list)):
    print(':',end='')
    print(ipv6_list[val], end='')
print()