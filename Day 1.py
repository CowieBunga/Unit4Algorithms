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
'''
import math
def binarySearch(a, value, left, right):
    if right > left:
        return "not found"
    mid = math.floor((len(a))/2)
    if a[mid] == value:
        print("true")
        return mid
    if value < a[mid]:
        print("left")
        a = a[0:mid]
        return binarySearch(a, value, left, mid - 1)
    else:
        print("right")
        a = a[mid:len(a)]
        return binarySearch(a, value, mid + 1, right)
print(binarySearch([1,2,3,4,5,6],6,6,1))
'''
'''
def findFactorial(num):
    for i in range(0, num-1):
        print(i)
        num += num * i
    return num
print(findFactorial(5))
'''
'''
# recursion problem warm up
def evenSum(n):
    if n <= 1:
        return 0
    else:
        if n%2 == 1:
            return evenSum(n-1)
        else:
            return n + evenSum(n-1)

print(evenSum(998))
'''
'''
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        holder = self.stack[-1]
        del self.stack[-1]
        return holder

numberStack = Stack()
numberStack.push(2)
numberStack.push(3)
numberStack.push(8011)
print(numberStack.stack)
numberStack.pop()
print(numberStack.stack)
# stacks are LIFO (last in, first out)

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        holder = self.queue[0]
        del self.queue[0]
        return holder

    def peek(self):
        return self.queue[0]

numberStack = Queue()
numberStack.enqueue(2)
numberStack.enqueue(3)
numberStack.enqueue(8011)
numberStack.dequeue()
print(numberStack.queue)
print(numberStack.peek)#?
# queues are FILO (first in, last out)

import random
class RandOut:
    def __init__(self):
        self.list = []

    def add(self, data):
        self.list.append(data)

    def delete(self):
        r = random.randint(0, (len(self.list)-1))
        holder = self.list[r]
        del self.list[r]
        return holder
numberStack = RandOut()
numberStack.add(2)
numberStack.add(3)
numberStack.add(8011)
numberStack.delete()
print(numberStack.list)
'''


# cryptology

def caesar(text, key):
    text = list(text)
    for i in range(len(text)):
        text[i] = chr(int(ord(text[i]))+key)
    print(text)

caesar("Hello", 3)

'''
# ??? not done
def encrypt(text, key):
    alph = [4,5,6]
    ALPH = [8,9,1,0]
    for i in range(len(text)):
        if text[i] == type(int):
            text[i] == int(text[i])+key
        elif text[i] in alph:
            text[i] == chr(int(ord(text[i]))+key*2)
        elif text[i] in ALPH:
            text[i] == chr(int(ord(text[i]))+key+3)
        else:
            text[i] == int((text[i])+key*8)
        print(text)
        return text


nums = []
while True:
    num = int(input("\nInput a number you would like to encrypt "))
    if isinstance(num, int):
        nums.append(num)
        again = input("\nAgain? (y for yes)").lower()
        if again != 'y':
            key = int(input("\nKey: "))
            print(encrypt(nums, key))
            break
    else:
        print("\nNot a number!")

therest = input("\nInput the rest of your message ")
'''
