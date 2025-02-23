def find(dic, value):
    return [key for key,v in dic.items() if v == value]
def xiangdeng(s):
    return 'even' in s
def bian(dic,zimu):
    a,b,c = zimu.split()
    if xiangdeng(c):
        for i in a + b:
            dic[i] = 1
    return dic
def commit(l,m):
    for t in l:
        a,b,c = t.split()
        if c == 'up' and m in a:
            return 'heavy.'
        elif c == 'up' and m in b:
            return 'light.'
        elif c == 'down' and m in a:
            return 'light.'
        elif c == 'down' and m in b:
            return 'heavy.'
n = int(input())
for i in range(n):
    dic = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0}
    a = input()
    b = input()
    c = input()
    l = [a,b,c]
    for i in l:
        dic = bian(dic,i)
    m = find(dic,0)
    m = m[0]
    weight = commit(l,m)
    print(m,"is the counterfeit coin and it is",weight)