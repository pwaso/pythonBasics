"""
Print following pattern
*
* *
* * *
* * * *
* * * * *
* * * * * *
"""

print('Patterns 1 - enter number of rows you want to print')
rows = int(input())

for i in range(rows+1):
    for j in range(i):
        print('* ', end='')
    print()

"""
Print following pattern
* * * * * 
* * * * 
* * * 
* * 
* 
"""

print('Pattern 2 - enter number of rows you want to print')
rows = int(input())

for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print('* ', end='')
    print()

"""
Print following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
"""
print('Pattern 3 - Enter number of rows you want to print')
rows = int(input())

for i in range(rows+1):
    for j in range(i):
        print(i, end=' ')
    print()

"""
Print following pattern
        1 
      1 3 5 
    1 3 5 7 9 
  1 3 5 7 9 11 13 
1 3 5 7 9 11 13 15 17 
"""
print('Pattern 4 - enter number of rows you want to print')
rows = int(input())

for i in range(rows+1):
    k=-1
    for j in range(0,rows-i):
        print(" ", end=' ')
    for j in range(0,((i*2)-1)):
        k+=2
        print(k, end=' ')
    print()