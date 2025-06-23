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
try:
    n = int(input("Enter a number: "))
    if n<0:
        print("Enter a positive integer number in numerical form")
    else:
        print(fibseq(n))
except ValueError:
    print("Please enter a positive integer number in numerical form")
