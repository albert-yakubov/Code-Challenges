import random
import time


my_range = 100000
my_size = 10
# 
my_random = random.sample(range(my_range), my_size)

print(my_random)

def print_number(n):
    print(my_random[4])

print_number(4)


def print_array(arr):
    for i in range(len(arr)):
        print (arr[i])

print (my_random)

# def my_for_loop(n):
#   print(n)

# my_for_loop(1)


animals = ["cats", "dogs", "parrot","tiger"]
def print_animals(animal_list):
    my_n = 0
    for i in range(len(animal_list)):
        print(animal_list[i])
        for _ in range(10):
            my_n += 1

print_animals(animals)


def print_animal_pairs():
    for animal1 in animals:
        for animal2 in animals:
            print(f"{animal1}, {animal2}")
print_animal_pairs()

def print_animal_triplets():
    for animal1 in animals:
        for animal2 in animals:
            for animal3 in animals: 
                print(f"{animal1}, {animal2}, {animal3}")
# 53 through 66 returns huuuuge list of animals
def get_animal_combos(l):
    list_length = len(l)
    if list_length == 0:
        return [ [] ]
    else:
        animal_combos = []
        previous_combos = get_animal_combos( l[1:] )
        for combo in previous_combos:
            animal_combos.append( combo )
            animal_combos.append( combo + [l[0]] )
        return animal_combos
        
print(get_animal_combos(animals))


# linear search

searching_for = 7
def find_in_number():
    for i in range(len(my_random)):
        if my_random[i] == searching_for:
            return True
    return False
start = time.time()

# sort it


print(find_in_number())  
end = time.time()
print(f"runtime: {end-start} ")      

# log n --- slows down the n to power increases
# binary has to be lenth 2+ and sorted 
# Binary search is for more expensive searches
value = 7
def find_val_binary(arr):
    if len(arr) <= 0:
        # TODO handle edge
        pass
    first = 0
    last = (len(arr) -1)

    found = False

    while first <= last and not found:
        # find middle using int division
        middle = (first + last) // 2

        if arr[middle] == value:
            found = True
        else:
            if value < arr[middle]:
                # search lower half (or backwords)
                last = middle - 1
            else:
                first = middle + 1
    return found 
print("Binary!")
start = time.time()

# sort it
my_random.sort()


print(find_in_number())  
end = time.time()
print(f"runtime: {end-start} ")


# insertion sort:

my_list = [8 , 2 , 4 , 5 , 4 , 3]

# make a function to sort the array

def insertion_sort(list_to_sort):
    # separate first elemement think of it as sorted 

    # all the other once, starting at 1
    for i in range(1, len(list_to_sort)):
    # put current number in temp variable
        temp = list_to_sort[i]
    # look left, and shift items to right as we look through(iterate)
        # we start at i 
        j = i 
        # start at number 
        while j > 0 and temp < list_to_sort[j -1]:
        # when left is maller than temp or we re at 0, put it at that spot:
            list_to_sort[j] = list_to_sort[j -1]
            #counter for j
            j -= 1
        
        list_to_sort[j] = temp
    return list_to_sort

print (insertion_sort(my_list))
