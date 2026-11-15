

call_count={}

def fib(n):
    call_count[n] = call_count.get(n, 0) + 1
    if n == 0:
        return 0
    if n == 1 :
        return 1
    return fib(n-1) + fib(n-2)
n = 10
print(fib(n))

for i in range(n):
    print(f"{i}번 발생 {call_count[i]}")