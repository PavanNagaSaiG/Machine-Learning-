ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# sorted is the function which is used to sort the values in a list
ages = sorted(ages)
# min and max are the functions to say the values in the list
print("The Min age is", min(ages), "and The Max age is", max(ages))
# append will add the minimum and maximum values to the list
ages.append(min(ages))
ages.append(max(ages))
print("the updated ages are", ages)
ages = sorted(ages)
# here we are sorting to find mean
print("the ages after sorted are", ages)
cou = len(ages)
# len is for length of list ,cou is the variable where we insert the value
print("the count is", cou)
if (cou % 2 != 0):
    # here by modulus if reminder is not equal to zero then we print the middle value of the list ias median
    print("Median is ", ages[cou // 2])
else:
    # if the modulus value is equal to zero then we had to add the two middle items
    print("Median is ", (ages[(cou // 2) - 1] + ages[cou // 2]) / 2)
    # -1 states the previous value of the location of the list + current value of location in the list
a = 0
# declare a here to run the for loop
for i in ages:
    a = a + i
    # this loop executes until the values comes to an end in the list
print("the average value is", a / cou)
print("The range is ", max(ages) - min(ages))
# to find the range of ages the formula is written in list
