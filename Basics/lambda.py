# lambda returns the value that a function will return when it is called
# for a simple function we use lambda rather than creating a function using def


# normal function creation
def add(x, y):
    return x + y

num1 = input("enter any number")
num2 = input("enter any number")

sum_normal = add(num1, num2)
print(sum_normal)

# lambda creates a function
sum_of_num = lambda num1, num2: num1 + num2
print(sum_of_num(num1, num2))
print(type(sum_of_num))
# type(sum_of_num) gives us <class 'function'> which illustrates that lambda creates a function

