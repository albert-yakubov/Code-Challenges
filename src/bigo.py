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
# def get_animal_combos(list):
#    list_len = len(list)
#    if list_len == 0:
#        return [[]]

#   else:
#        animal_combos = []
#        previous_combos = get_animal_combos([list [1:]])
#        for combo in previous_combos:
#            animal_combos.append(combo)
#            animal_combos.append(combo + [list[:0]])
#        return animal_combos

#print(get_animal_combos(animals))


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

# log n --- slows down the n to pwer increases
# binary has to be lenth 2+ and sorted 
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