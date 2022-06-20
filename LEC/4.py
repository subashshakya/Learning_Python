#lambda functions

numbers = [1,2,3,4,5,6]
even_list = []
def is_even(num):
    return num % 2 == 0


#filter is an in-built function
#first parameter is function and second parameter is an iterable

print(filter(is_even, numbers))
#output: <filter object at 0x000001CE3396ECD0>


even_list = list(filter(is_even, numbers))
print(even_list)
#output: [2, 4, 6]

print(type(is_even))
#output: <class 'function'>

#yo process lai simplify garna LAMBDA function use hunxa
#on simplifying the is_even function:
lambda num: num % 2 == 0
#num is parameter  num % 2 == 0 this is return value

names = ['Kushal', 'subash', 'monikaaaaa', 'seeru', 'tulasi', 'buddhaa']

#here first parameter is callback function
odd_name = list(filter(lambda nam:len(nam) % 2 != 0, names))
print(odd_name)
#output: ['seeru', 'buddhaa']


#MAP function:
numbers = [1,2,3,4,5,6,7,8]
#here first parameter is callback function
print(list(map(lambda num:num **2, numbers)))
#output: [1, 4, 9, 16, 25, 36, 49, 64]

namess = ['subash', 'totle', 'malisha', 'mama']
#here first parameter is callback function
print(list(map(lambda nam:len(nam) % 2 !=0, namess)))
#output: [False, True, True, False]

print(list(map(lambda nam:"odd" if len(nam)%2 !=0 else "even",namess)))
#output: ['even', 'odd', 'odd', 'even']


#reversing the individual string and adding dash
print(list(map(lambda nam: '-'.join(nam[::-1]),namess)))
#output: ['h-s-a-b-u-s', 'e-l-t-o-t', 'a-h-s-i-l-a-m', 'a-m-a-m']