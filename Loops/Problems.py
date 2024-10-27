"""
1. Hacker Rank Problem
    Link : https://www.hackerrank.com/challenges/python-loops/problem
"""


def hackerrankProblem():
    number = int(input("Enter a number: "))
    for i in range(0, number):
        print(i * i)


"""
2. Print numbers from 1 to 10 using a for loop
"""


def printNumbersInBetween():
    for i in range(1, 11):
        print(i)


"""
3. Calculate the sum of numbers from 1 to 10 using a for loop
"""


def sumNumbersFromTo():
    sum = 0
    for i in range(1, 11):
        sum += i
    print(sum)


"""
4. Print the elements of a list using a for loop
"""


def printElementFromList():
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in List:
        print(i)


"""
5. Calculate the product of elements in a list using a for loop
"""


def productOfNumbersFromList():
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    product = 0
    for i in List:
        product *= i
    print('Product of numbers in list is: ', product)


"""
6. Print even numbers from 1 to 10 using a for loop
"""


def evenNumbersFromList():
    for i in range(1, 11):
        if i % 2 == 0:
            print(i)


"""
7. Print numbers in reverse from 10 to 1 using a for loop
"""


def reverseNumbers():
    for i in range(10, 0, -1):
        print(i)


"""
8. Print characters of a string using a for loop
"""


def printCharactersFromString():
    str = 'This is a string'
    for i in str:
        if i == ' ':
            continue
        print(i)


"""
9. Find the largest number in a list using a for loop
"""


def largestNumbersFromList():
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    max = List[0]
    for i in List:
        num = i
        if num >= max:
            max = num
    print('Largest number from list is ', max)


"""
10. Find the average of numbers in a list using a for loop
"""


def avgOfNumbersFromList():
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sum = 0
    for i in List:
        sum += i
    avg = sum / len(List)
    print('Average of numbers from list is ', avg)


"""
11. Print all uppercase letters in a string using a for loop
"""


def printAllUppercase():
    str = 'This iS A strInG'
    for i in str:
        if i.isupper():
            print(i)
        # if i >= 'A' and i <= 'Z':
        #     print(i)


"""
12. Count the number of vowels in a string using a for loop
"""


def countVowels():
    str = 'This is a strIng'
    count = 0
    for i in str:
        if i.lower() in 'aeiou':
            count += 1
    print('Number of vowels in string is: ', count)


"""
13. Calculate factorial of a number using a while loop
"""


def factorial():
    n = 10
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    print('The factorial of number is: ', fact)


"""
14. Find the first occurrence of a number in a list using a while loop
"""


def firstOccurrenceOfNumber():
    list = [4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    flag = 0
    number =3
    while flag < len(list):
        if list[flag] == number:
            print(f'First occurrence of {number} is on position: ', flag)
            break
        flag += 1



"""
15. Calculate the sum of numbers from 1 to 100 using a while loop
"""
def sumOfNumbersUsingWhile():
    sum = 0
    num =100
    while num>0:
        sum += num
        num -= 1
    print('The sum of numbers from 1 to 100 is ', sum)
    print(int(50 ** 0.5))


optionActions = {
    1: hackerrankProblem,
    2: printNumbersInBetween,
    3: sumNumbersFromTo,
    4: printElementFromList,
    5: productOfNumbersFromList,
    6: evenNumbersFromList,
    7: reverseNumbers,
    8: printCharactersFromString,
    9: largestNumbersFromList,
    10: avgOfNumbersFromList,
    11: printAllUppercase,
    12: countVowels,
    13: factorial,
    14: firstOccurrenceOfNumber,
    15: sumOfNumbersUsingWhile,

}

while True:
    option = int(input("Enter an option: "))
    print(optionActions.get(option))
    function = optionActions.get(option)
    if function:
        function()
    else:
        print("Invalid option")
