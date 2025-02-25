def change(a,b):
    return [int(a[i]!=b[i]) for i in range(len(a))]
def bian(l,i):
    l[i] = 1 - l[i]
    if i > 0:
        l[i-1] = 1 - l[i-1]
    if i < len(l) - 1:
        l[i+1] = 1 - l[i+1]
    return l
def solve(l):
    count = 0
    temp = l.copy()
    for i in range(len(temp) - 1):
        if temp[i] == 1:
            temp = bian(temp,i+1)
            count += 1
    return count if temp[-1] == 0 else float('inf')
a = input()
b = input()
l = change(a,b)
result1 = solve(l)
l = bian(l, 0)
result2 = solve(l) + 1

min_result = min(result1, result2)

if min_result == float('inf'):
    print('impossible')
else:
    print(min_result)