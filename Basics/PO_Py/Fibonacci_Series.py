# using loops to display the fibonacci series

term1 = 1
term2 = 1

term3 = term1 + term2

print("The required fibonacci series is: ")

print(term1)
print(term2)

i = 0
for i in range(10):
    print(term3)
    term1 = term2
    term2 = term3
    term3 = term1 + term2
