def my_recursion(n):
    print(n)
    #line 4 is the base case
    if n == 5:
        return
    else:
        my_recursion(n+1)

my_recursion(1)


# Fibonacci numbers -->
# always start with 0 and 1
# which is base for recursive move towards it

# 0 1 1 2 3 5 8 13 21 34 55 89 

def fibonacci(n):
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        n_minus_1 = fibonacci(n-1)
        #this print statement shows the steps that are happening in fibonacci
        print(n_minus_1)
        n_minus_2 = fibonacci(n-2)
        print(n_minus_2)
        return n_minus_1 + n_minus_2 
# tenth number in fibonacci numbers
print(fibonacci(5))

# quick sort 
# [ 5 9 3 7 2 8 1 6]
# pick the number
# base --> if array len 0 or 1 return an array
# pick pivot \put smaller to left
# pivot is kinda like the base case
# put higher to right
# quick sort left
# quick sort right
# return quick sort (left) + quick sort (right)
