#!/usr/bin/env python3

def print_fibonacci(length):
    a,b = 0,1
    fib = []
    for i in range(length):
        fib.append(a)
        a,b = b,a+b
    print(fib)

print_fibonacci(10)