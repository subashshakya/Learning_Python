# tuple in python
# A tuple is a collection which is ordered and unchangeable.

Simple_Tuple = 1, 2, 3, 4
# tuples dont require a round bracket to be defined
# but a single parenthesis string is not a tuple i.e ('a') is not a tuple
print(type(Simple_Tuple))
# output: <class 'tuple'>

# len is a built-in function which measures how many elements are present in the array, lists, etc
print(len(Simple_Tuple))

# some useful functions for tuples:
print(min(Simple_Tuple))
# prints 1
print(max(Simple_Tuple))
# prints 4


# concatenating a tuple
tuple_a = (1, 2, 3, 4)
tuple_b = (4, 5, 6, 7)
tuple_c = tuple_a + tuple_b
print(tuple_c)
# output: (1, 2, 3, 4, 4, 5, 6, 7)
# the equal elements are not replaced but repeated instead


# reversing the elements of a tuple
atuple = ("e", "l", "p", "u", "t")
rev = tuple(reversed(atuple))
print(rev)
# output: ('t', 'u', 'p', 'l', 'e')