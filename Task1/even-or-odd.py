def EvenOrOdd(i):
    if i%2==0:
        return("Even")
    else:
        return("Odd")
n = int(input("Enter a number: "))
print(EvenOrOdd(n))