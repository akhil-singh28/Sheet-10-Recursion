s=input()
def rev(s):
    if len(s)==0:
        return ""
    else:
        return rev(s[1:])+s[0]
print(rev(s))