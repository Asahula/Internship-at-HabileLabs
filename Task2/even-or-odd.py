def EvenOrOdd(i):
    if i%2==0:
        return("Even")
    else:
        return("Odd")
try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Enter an integer")
else:
    print(EvenOrOdd(n))