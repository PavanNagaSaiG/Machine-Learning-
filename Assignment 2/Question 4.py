def unique_list(lst):
    # here we have defined a unique list  for the following lst
    return list(set(lst))


# set function is used to remove duplicates from the list
lst = [1, 2, 3, 3, 3, 3, 4, 5]
print(unique_list(lst))
