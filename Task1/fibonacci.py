def fibonacci(n):
    sum=0
    if n==0:
        return(0)
    elif n==1:
        return(1)
    else:
        sum = sum + fibonacci(n-1) + fibonacci(n-2)
    return(sum)
def fibseq(n):
    l=[]
    for i in range(n+1):
        l.append(fibonacci(i))
    return(l)
n = int(input("Enter a number: "))
print(fibseq(n))
