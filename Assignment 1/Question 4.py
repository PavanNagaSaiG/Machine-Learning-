it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("the length of the it companies string is", len(it_companies))  # len is the function used for length of string
it_companies.add('twitter')  # add is the function to add a value into sets
print("the updated list is", len(it_companies))
it_companies.update(['Verizon', 'AT&T', 'Tesla'])  # to add multiple values into sets update function is used
print("the updated list is", len(it_companies))
it_companies.remove('Tesla')  # remove is the function used to remove a value in set
print("the length of the it companies string is", len(it_companies))
it_companies.discard('Verizon')
# discard is used to remove value from list but it wil not raise an error if an item does not exist
print("the length of the it companies string is", len(it_companies))
print("the updated list is ", it_companies)
C = A.intersection(B)  # intersection is the function which is used to return the common values in 2 given lists
print("The intersection is ", C)
K = A.union(B)
# union is the function which is used to get all the values in 2 or more lists but multiple values in the list will
# not be repeated
print("the union result is", K)
print("the give sets are ", A.isdisjoint(B))
#  if the value is TRUE then there are no common or intersecting elements in two sets
# if the value is FALSE then there are common or intersecting elements in two sets
D = A.union(B)
E = B.union(A)
print(D , E) # here the values of A and B will be repeated
F = A.symmetric_difference(B) # symmetric difference is the function which prints only common values in the list
print("the symmetric difference is " , F)
del A
del B
# del is the keyword which is used to delete the sets
print(A, B) # error will be generated when we run the programme
ages = set(age) # set is the keyword which is used to convert list into set
print("the ages after turing from list to set is", ages) 
