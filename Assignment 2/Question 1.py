rows = 5
for i in range(0, rows):  # range is used to return the sequence of the numbers.
    for j in range(0, i + 1):  # here i value increments until 5
        print('*', end=' ')
    print()  # the * will be printed in sequence order
for i in range(rows - 1, -1, -1):  # here the i value decrements from 5 to 1
    for j in range(0, i):
        print('*', end=' ')
    print()  # the * prints accordingly
