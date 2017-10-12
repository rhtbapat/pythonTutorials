import sys

def factorialOfNum(num):
    temp = 1
    for i in range(0,num):
        temp = temp*(i+1)
    
    return temp