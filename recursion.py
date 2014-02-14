# Multiply all the elements in a list
def multiply_list(l):
    if len(l) == 1:
        return l[0]
    else:
        popped = l.pop()
        return popped * multiply_list(l)
       

# Return the factorial of n
def factorial(n):
    if n ==1:
        return 1
    else:
        return factorial(n-1) * n
    

# Count the number of elements in the list l
def count_list(l):
    # if l == []:
    #     return 0
    # else:
    #     popped = l.pop()
    #     return popped + count_list(l)
    #return l
    if l == []:
        return 0
    else:
        return count_list(l[1:])+1

# Sum all of the elements in a list
def sum_list(l):
    if len(l) == 1:
        return l[0]
    else:
        popped = l.pop()
        return popped + sum_list(l)


# Reverse a list without slicing or loops
def reverse(l):
    if len(l) == 1:
        return l
    else:
        popped = l.pop()
        return [popped] + reverse(l)

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    return None

# Determines if a string is a palindrome
def palindrome(some_string):
    return False

# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    return (0, 0)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    return



# Test functions
l = [2, 3, 4,]

#print factorial(5)
#print multiply_list(l)
# print sum_list(l)
# print count_list(l)
print fibonacci(10)