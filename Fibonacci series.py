# FIBONACCI SERIES
# The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
# The sequence commonly starts 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.
# F(n) = F(n-1) + F(n-2)
# where F(0) = 0 and F(1) = 1.

N = 10  # Number of terms in the Fibonacci series
a = 0
b = 1
next = b
count = 1

while count <= N:
    print(next, end=" ")
    next = a + b
    a = b
    b = next
    count += 1
print()

