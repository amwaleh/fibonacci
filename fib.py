"""
This function returns the number in the nth position within the fibonacci's sequence
using list comprehension 
"""


def fib(position):
    list_fib = [0, 1, 1]
    [list_fib.append(sum(list_fib[-2:])) for i in range(position - 3) if position >= 3]
    return list_fib[position-1]

print(fib(2))
print(fib(100))