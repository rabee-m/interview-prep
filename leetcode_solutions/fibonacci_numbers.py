#AlgoExpert Easy Problem: Nth Fibonacci Number

#Bad Recursive Solution
#Time: O(2^n)
#Space: O(n) due to call stacking from recursion
#e.g.) stack: fib(6) -> fib(5) -> fib(4) -> fib(3) -> fib (2), then we start returing
#as we hit base case (this is not showing fib(n-2) calls yet
def getNthFib1(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)
    pass

#Good Recursive Solution
#Time: O(n), as we have to atleast memomize each fib number once, but after
#that they are stored in our memo hash table which has O(1) lookup
#Space: O(n), as we are creating hash-table and also we have call-stack 

#Utilize memoization which is a good strategy for optimizing exponential
#time recursive algorithms
#refer to pg 53-54 of CTCI
def getNthFib2(n, memo={1:0, 2:1}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = getNthFib(n-1, memo) + getNthFib(n-2, memo)
        return memo[n]

#Iterative Solution (Best) 
#Time: O(n), as we have to calculate all previous fibonacci numbers
#Space: O(1), not taking any additional space
def getNthFib3(n):
    lastTwo = [0, 1]
    counter = 3
    while n >= counter:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    if n == 1:
        return 0
    else:
        return lastTwo[1]