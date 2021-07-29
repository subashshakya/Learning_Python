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

    def Display():
        print(self.name)
        print(self.surname)


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