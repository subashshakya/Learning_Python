# #day 3

# #if else condition

# number = 2

# #determine whether the number is odd or even

# if (number % 2) == 0:
#     print("the number is even")
# else:
#     print("the number is odd")


# number = input("enter any number \n")

# if number == 0:
#     print("the input number is zero")
# elif number > 50:
#     print("the number is greater than 50")
# else:
#     print("the number is less than 50")


# #is vaccinated?

# age = input("enter you age")
# is_vaccinated = True

# if int(age) > 18 and bool(is_vaccinated):
#     print("you are welcomed to the club")
# elif not is_vaccinated:
#     print("go get vaccinated")
# else:
#     print("you are underage!!")


#while loop
#sum of even numbers in range of 100
# i = 0
# sum = 0
# while i<=100:
#     if(i % 2 == 0):
#         sum += i
#     i+=1

# print(sum)
# #output: 2450


# #for loop
# print(list(range(100)))

#range le integer value input linxa
#if one parameter then it shows: range(0, 100)
#if two parameters then it is shows the values from 0 to 100 individually
#if three parameters then last one signifies step
    

# print(range(1, 10))
# #output: 

# print(range(1, 100, 2))



# for i in range(100):
#     print(i)


# iterating in lists
# list = [1, 2, 3, 4, 5]

# for numbers in list:
#     print(numbers)


# students = [ #dictionary ma loop hudaina list ma matra hunxa
#     {
#         "name": "subash",
#         "address":"pulchowk"
#     },
#     {
#         "name": "lambe",
#         "address": "juwagal"
#     }
# ]

# for student in students:
#     print(f"i am {student['name']}")


# list = [2,2,4,4,6,8]
# sum = 0
# item = 0
# for numbers in list:
#     if numbers % 2 != 0:
#         item +=1
    
# if item == 0:
#     print("true")
#     for i in list:
#         sum += i
#     print(sum)
# else:
#     print("the number in list contain a odd")



numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number**2)

print(squares)

#list comprehension:
square = [number**2 for number in numbers if number%2 == 0]
print(square)
#output:[4, 16]


names = ["subash", "shakya", "lambe"]


print(list(enumerate(names)))
#output: [(0, 'subash'), (1, 'shakya'), (2, 'lambe')]


#args 
#args halepaxi tespaxi ko value jasko ma args xa tesko mai janxa
i, *name = (0 ,"subash", "shakya")
print(i , name)
#output: 0 ['subash', 'shakya']


#ternary if else
age = 53
category = 'old' if age > 60 else "young dumb"


#functions:

def details(name, roll, *score):
    print(f"my name is {name}.\n roll number: {roll} \n score: {score}")

details("subash", 34, 69)
#output: my name is subash.
#  roll number: 34
#  score: 69

#use of args in functions:
details("subash", 34, 69,78,99)
#output: my name is subash.
#  roll number: 34
#  score: (69, 78, 99)

#KWARS
def details(name, roll, **score):
    print(f"my name is {name}.\n roll number: {roll} \n score: {score}")

details(name="subash", roll=34, math = 1, science =1, nepali=0)
#output:my name is subash.
#  roll number: 34
#  score: {'math': 1, 'science': 1, 'nepali': 0}


def find_max(*value):
    max = value[0]
    for val in value:
        if(max<val):
            max = val
    return max

print(find_max(1,2,3,4,5,6,7,8))