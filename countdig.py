def count(n):
    if n==0:
        return 0
    return 1+count(n//10)
num=int(input())
if num==0:
    print(1)
else:
    print(count(num))
