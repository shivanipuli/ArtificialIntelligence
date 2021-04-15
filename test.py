def mystery(num, y):
    if y==0:
        return 1
    return num*mystery(num,y-1)

def recur(n):
    if n<=10:
        return n*2
    return recur(recur(n//3))

print(recur(27))