list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in list:  # let us declare one of value in i
    if (i % 2 == 0):
        # comparing i if i=even then remove from list, if i= odd hold in list
        list.remove(i)
        # remove is function which is used to remove values in the list
print(list)
