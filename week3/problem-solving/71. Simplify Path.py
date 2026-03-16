path = input().split("/")
path.reverse()

result = list()

while path:
    folder = path.pop()
    if(folder == '.'):
        continue
    elif(folder == '..'):
        if result:
            result.pop()
        continue
    elif(folder == ''):
        pass
    else:
        result.append(f'/{folder}')

if not result:
    result.append('/')

str = "".join(result)
print(str)