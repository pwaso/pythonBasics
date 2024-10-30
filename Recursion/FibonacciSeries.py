#Fibonaci Series using recursion
def fibonaciSeries(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaciSeries(n-1) + fibonaciSeries(n-2)
try:
    num = int(input('Enter number of terms in series'))
    for i in range (num):
        print(fibonaciSeries(i), end= ' ')
except ValueError:
        print('Please enter valid input')