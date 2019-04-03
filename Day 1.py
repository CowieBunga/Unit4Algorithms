# Sample Algorithm - baking a cake
'''
1. purchase ingredients
2. preheat oven to 350 fahrenheit
3. Gather ingredients
4. measure out appropriate quantities
5. combine wet ingredients
6. combine dry ingredients
7. mix wet and dry ingredients together
8. pour batter into cake pan
9. put in oven
10. set timer for 30 minutes
11. remove cake from oven
12. remove cake from pan and let cool
13. once cool, put icing on the cake
14. cut the cake into even pieces.
15. serve the cake
'''

'''
#Day 1
#1.
def fact(n):
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product


print(fact(5))
# Linear - 5*O(n) --> O(n)

#2.


def constant_algo(items):
    result = items[0] * items[0]
    print(result)


constant_algo([4, 5, 6, 8])
# Constant - O(1)

#3.


def linear_algo(items):
    for item in items:
        print(item)

    for item in items:
        print(item)


linear_algo([4, 5, 6, 8])
# Linear - 2 * O(n) --> O(n)

#4.

def quadratic_algo(items):
    for item in items:
        for item2 in items:
            print(item, ' ', item)


quadratic_algo([4, 5, 6, 8])
# Quadratic - O(n^2)

'''

# Day 2:

# Using pseudocode design an algorithm that sums all the numbers from 1 to 100
'''
x equals 0
for number in the range 1 to 100:
    x plus equals number
'''
'''
x = 0
for number in range(0,101):
    x += number
print(x)
'''
'''
def recursionExample(tracker):
    if tracker > 4:
        return True
    else:
        return recursionExample(tracker+1)

tracker = 0
print(recursionExample(-992))
'''
'''
searchdata = 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def linearSearch(numbers):
    for number in numbers:
        if searchdata == number:
            return True
print(linearSearch(numbers))
'''
import math
def binarySearch(a, value, left, right):
    if right > left:
        return "not found"
    mid = math.floor((len(a)-1)/2)
    if a[mid] == value:
        print("true")
        return mid
    if value < a[mid]:
        print("left")
        a = a[0:mid+1]
        return binarySearch(a, value, left, mid - 1)
    else:
        print("right")
        a = a[mid+1:6]
        return binarySearch(a, value, mid + 1, right)
print(binarySearch([1,2,3,4,5,6],4,6,1))

'''
def findFactorial(num):
    for i in range(0, num-1):
        print(i)
        num += num * i
    return num
print(findFactorial(5))
'''

