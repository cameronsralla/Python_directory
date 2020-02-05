def add(x, y):
    total = x+y
    return total

def subtract(x, y):
    total = x-y
    return total

def multiply(x, y):
    total = x * y
    return total

def divide(x, y):
    total = x / y
    return total

def even_or_odd(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

def power(x, y):
    total = x ** y
    return total

def count(num):
    for digit in range(int(num)):
        print(digit)

def list_sum(lst):
    total = 0
    for num in lst:
        total = total + num
    return total

def average(lst):
    summation = 0
    lst_len = len(lst)
    for num in lst:
        summation += num
    result = summation/lst_len
    return result