from calc import *
from functools import reduce

print(add(1,2))

print(sub(60,45))

#REDUCE 
#syntax: reduce(function, iterable)
#reduce lai 2 ota parameter chaixa here:a,b
print(reduce(lambda a,b: a+b,[1,2,3,4,6,7,8,9,9,9,9,9,100]))
#output: 176

print(reduce(lambda a,b: a if a> b else b, [1,2,3,-9,10]))

