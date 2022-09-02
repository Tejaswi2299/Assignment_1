


lb=[]
kg=[]
print("Enter the number of students weights to be converted:")
#Reading User inputs
count=int((input()))
print("Enter the values")
#appending all the weight values in lbs
for i in range(0,count):
    lb.append((int(input())))
#converting lbs to kgs
for i in range(0,count):
    k=round(lb[i]/2.20462262,2)
    # appending the weight values in kgs
    kg.append(k)
print(kg)