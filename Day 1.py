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










