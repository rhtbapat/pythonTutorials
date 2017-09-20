'''
Python Module
'''
import sys

#Fibonacci Series
def fibonacci(num):
    a, b = 0, 1
    for i in range(0,num):
        a, b = b, a + b
        print(str(a))
 
fibonacci(5)


