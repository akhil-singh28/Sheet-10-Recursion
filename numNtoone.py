n=int(input())
def num(n):
    if n==1:
        print(1)
    else:
        print(n)
        num(n-1)
num(n)