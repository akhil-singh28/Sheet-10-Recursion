N=int(input())
def num(N):
    if N==1:
        print(1)
    else:
        num(N-1)
        print(N)
num(N)