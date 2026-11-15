n = 7
for i in range(n):

    for j in range(n-i-1):
        print(" ",end=' ')

    for j in range(1, i*2+2, 2):
        print(j, end =" ")

    for j in range(i*2-1, 0, -2):
        print(j, end=" ")
    print()

def reverse(s):
    if len(s) <= 1:
        return s
    return s[1:] + s[0]