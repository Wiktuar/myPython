digit = int(input())

def dividers(digit):
    a = 2;
    while True:
        if digit % a == 0: 
            digit = digit / a;
            print(a);
            a = 1;
            
        if digit == 1:
            break;
        a += 1

dividers(digit)
