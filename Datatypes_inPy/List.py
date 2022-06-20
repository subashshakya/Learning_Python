# List is a better array

List_Num1 = ["this", "is", "a", "string", "list"]

print(List_Num1[3])
# prints 'string'
print("****************")
for x in List_Num1:
    print(x)
# prints the elements of List_Num1

print("*****************")

print(List_Num1)
# this prints ['this', 'is', 'a', 'string', 'list'] i.e prints the list as it is

length = len(List_Num1)
print(length)
# prints the length of the list

# lists can also store the values of objects in it

class For_example:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    



def say_hello():
    print("hello!")


say_hello()

# storing constructors in a list
Obj_list = [For_example("subash", "shakya"), For_example("starbucks", "coffee")]
# displaying the list elements
for i in Obj_list:
    print(i.name + " " + i.surname)
# output: subash shakya
#         starbucks coffee


# changing the types inside a list

alist = ["1", "2", "3", "4"]
alist = [int(item) for item in alist]

print(type(alist[0]))

# list comprehension

list_a = [1, 2, 3, 4]
list_b = [4, 3, 2, 1]

list_sum = [x + y for x in list_a for y in list_b]
# adds element of the given index to all the element of the other list
# output: [5, 4, 3, 2, 6, 5, 4, 3, 7, 6, 5, 4, 8, 7, 6, 5]
print(list_sum)


list_sum1 = [[x + y for x in list_a] for y in list_b]
# adds the element of the second list of the specific index to all the elements in the other list(list_a here)
# output: [[5, 6, 7, 8], [4, 5, 6, 7], [3, 4, 5, 6], [2, 3, 4, 5]]
print(list_sum1)

# adding in the opposite order

list_sum2 = [[x + y for x in list_b] for y in list_a]
print(list_sum2)
# output: [[5, 4, 3, 2], [6, 5, 4, 3], [7, 6, 5, 4], [8, 7, 6, 5]]
