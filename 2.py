digit = int(input())

def minDivider(n):
    a = 2
    while True:
        if(n % a == 0 ):
            print(a)
            return
        a += 1

minDivider(digit)