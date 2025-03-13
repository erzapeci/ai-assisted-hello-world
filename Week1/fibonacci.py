#Functions to calculate the Fibonacci sequence
# The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
# The sequence starts 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.
# Parameters: n - the number of elements in the sequence to calculate
# Returns: a list of Fibonacci numbers

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence
print(fibonacci(10))
#code before refactoring

#def f(l, t): r = [] for i in range(len(l)): if l[i]["t"] == t: r.append(l[i]) return r
#code after refactoring
def filter_list(l, t):
    """Filter a list of dictionaries by a specific key."""

    result = []
    for i in range(len(l)):
        if l[i]["t"] == t:
            result.append(l[i])

    return result

#test the function
list_of_dicts = [{"t": 1, "x": 2}, {"t": 2, "x": 3}, {"t": 1, "x": 4}]
print(filter_list(list_of_dicts, 1))  # [{'t': 1, 'x': 2}, {'t': 1, 'x': 4}]
