digit = int(input("Введите число: "))

def factorial(n):
    a = 1
    for i in range(2, n+1) :
        a*=i
    print(a)

factorial(digit)