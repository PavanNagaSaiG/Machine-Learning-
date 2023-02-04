text = 'The quick Brow Fox'
count1=0 # initial lowercase value
count2=0 # initial uppercase value
for i in text:
    if i.islower(): # islower() is the function which is used to count the value of lowercase letters
        count1= count1+1
    elif i.isupper(): # isupper() is the function which is used to count the value of uppercase letters
        count2= count2+1
print("The lowercase is", count1)
print("the uppercase is", count2)
