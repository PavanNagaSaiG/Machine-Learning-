n=int(input("enter the number of students in the list"))
# input is the function which allows dynamically to enter values
weight_pounds = []
weight_KG = []
for i in range(n):
    pound_weight = float(input("the weight of students {} in pounds are:".format(i+1)))
    weight_pounds.append(pound_weight) #append is the function which is used to add values
    KG_WT = pound_weight * 0.543592
    weight_KG.append(round(KG_WT))
    # round tis the function which rounds up decimal values

print(weight_KG)
