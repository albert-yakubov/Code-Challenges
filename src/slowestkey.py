#slowest keypress challenge

# The function is expected to return a CHARACTER.
# The function accepts 2D_INTEGER_ARRAY keyTimes as parameter.
#
import os 
import sys


def slowestKey(keyTimes):
    # Write your code here
    worst_time = [0] * 26
    previous_time = 0
    for event in keyTimes:
        current_key = event[0]
        current_time = event[1]
        time_diff = current_time - previous_time
        if time_diff > worst_time[current_key]:
            worst_time[current_key] = time_diff
        previous_time = current_time

    slowest_key_number = worst_time.index(max(worst_time))
    slowest_key = str(chr(slowest_key_number + 97))

    return slowest_key

if __name__ == '__main__':
    fptr = sys.stdout 

    keyTimes_rows = int(input().strip())
    keyTimes_columns = int(input().strip())

    keyTimes = []

    for _ in range(keyTimes_rows):
        keyTimes.append(list(map(float, input().rstrip().split())))

    result = slowestKey(keyTimes)

    fptr.write(str(result) + '\n')

    fptr.close()
