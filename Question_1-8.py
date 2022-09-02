
# Online Python - IDE, Editor, Compiler, Interpreter
#----------------Question 1-------------------
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sorting the list
ages.sort()
print(ages)
l=len(ages)
 # minimum age as the list is sorted
min=ages[0]
# maximum age as the list is sorted
max=ages[l-1]
print("Minimum age:" ,min, "and Maximum age:",  max)
# appending minimum age
ages.append(ages[0])
#appending maximum age
ages.append(ages[l-1])
print(ages)
#Finding the median :
#calculating the index
l=(len(ages)-1)//2
#checking whether the no. of elements count is even or odd
if((len(ages))%2!=0):
    median=ages[l]
    print("The median is :",median)
else:
    median=(ages[l]+ages[l+1])/2
    print("The median is :",median)
#Finding average(sum of all elements):
sum=0
#summing up all the values in the list
for i in ages:
    sum=sum+i
print("The avaerage is :",sum//len(ages))
#Range of ages [max minus min]
ages.sort()
range=ages[len(ages)-1]-ages[0]
print("The range is:", range)
#----------------------Question 2------------------------------
#creating empty dictionary
dog = dict ()
#inserting data to dictionary
dog["name"] = "Bruno",
dog["color"] = "white",
dog["breed"] = "Shih zui",
dog["legs"] = "4",
dog["age"] = "3",
#creating student dictionary
student = {
    "first_name" : "Tejaswi Reddy",
    "last_name" : "Anapalli",
    "gender" : "female",
    "age" : "22",
    "marital status": "Married",
    "skills" : ["dancing","reading"],
    "country": "India",
    "city" : "Nellore",
    "address" : "Lakes at lions gate",
}
print(len(student))#calculated the length of student dictionary
v = student.get("skills")
print(v)
#printing the data type of the skills
print(type(v))
student['skills']+=['Skating']
print(student)
#printing the keys and values in a dictionary
print(list(student.keys()))
print(list(student.values()))

#-------------------------Question 3-----------------------------
#creating sisters and brothers
Sisters=("sony",'sanjana','snehitha')
Brothers=('Akhil','sunil','waseem')
#joining sisters and brothers tuple
Siblings=Sisters+Brothers
print(Siblings)
#calculating the length of tuples
print("I have",len(Siblings),"Siblings")
#converting tuple to list to make modifications
fml=list(Siblings)
#appending father and mother name
fml.append('Sumalatha')
fml.append('Srinivasulu')
#converting to tuple
family_members=tuple(fml)
print(family_members)

#----------------------Question 4---------------------------------
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#calculating the length
print("The length of set it_companies is:",len(it_companies))
#inserting one element
it_companies.add('Twitter')
print(it_companies)
#inserting multiple elements
it_companies.update(['Infosys','Deloitte','TCS','CTS','Wipro'])
print(it_companies)
#removing elements
it_companies.remove('TCS')
print(it_companies)
#joining A and B
C=A.union(B)
print(C)
#finding intersection between A and B
print(A.intersection(B))
#checking whether A is subset of B
print("Is A subset of B",A.issubset(B))
#checking whether A and B are disjoint set
print("Are A and B disjoint sets",A.isdisjoint(B))
#joining A and B, B and A
A|=B
B|=A
print(A,B)
#finding the symmetric difference between A and B
print("The symmetric difference between A and B is:",A.symmetric_difference(B))
#Deleting A and B
del A
del B
#converting age list to set to compare the length
s=set(age)
print("The lenght of list ages is:",len(age),"and the length of set ages is:",len(s))

#-------------------------Question 5--------------------------------
radius=30
#Calculating the area
_area_of_circle_= 3.14 *(radius**2)
print("The area of the circle is",_area_of_circle_)
#Calculating the circumference
_circum_of_circle_= 2 * 3.14 * radius
print("The circumference of the circle is:",_circum_of_circle_)
#Reading user input
print("Enter the radius value:")
r=int(input())
#calculating the area
area=3.14 * (r**2)
print("The area of the circle is:",area)

#---------------------------Question 6----------------------------------

text="I am a teacher and I love to inspire and teach people"
#Splitting the text
text=text.split()
#Converting splitted list to set
set_text=set(text)
#finding the length of set to get the count of unique elements
print("The unique words count is:",len(set_text))


#----------------------Question 7-----------------------------------------
#Using the escape separators to print the table
print("Name\t\tAge\t\tCountry\t\tCity\nAsabeneh\t250\t\tFinland\t\tHelsinki")

#-----------------------Question 8-------------------------------------------
#using the string formatting operators
radius = 10
area = int(3.14 * radius ** 2)
print("The area of a circle with radius %d is %d meters square."%(radius,area))

#------------------------------------------------------------------

    
    

