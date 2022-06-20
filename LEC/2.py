# immutables and mutables

#LIST
#list is a mutable data type 
my_list = ['subash', 1, 2, 3, [4,5,6,7]]

another_list = my_list[4];

print(another_list)
# output:  [4, 5, 6, 7]

another_list.append(8)


print(my_list)

print(another_list)

# #output:
# ['subash', 1, 2, 3, [4, 5, 6, 7, 8]]
# [4, 5, 6, 7, 8]


another_list.pop(2) #pop ko bhitra kei index vayena ki default mai last item pop garxa
print(another_list)
#output: [4, 5, 7, 8]


my_list.clear()
print(my_list)
#output: []

#for inserting in a specific index
#insert(index, value)
my_list.insert(0, "shakya")
print(my_list)
#output: ['shakya']


#as the list is mutable its individual index is refrenced as addresses and when we put my_list[4] in another_list so the address is referenced in both the lists


#DICTONARY 
#same as JS ko object
#key hunxa ani tesko value hunxa
# Dictonary ma item haru refrenced hudaina
#CRUD
my_dict = {"name": "Subash",
            "roll_no": 34,
            "dob": {"year": 2057,
                     "month": "nov"
            }
}


print(type(my_dict))
#output: <class 'dict'>

print(my_dict["name"])
#output: Subash

my_dict["age"] = 21

print(my_dict)
#output: {'name': 'Subash', 'roll_no': 34, 'dob': {'year': 2057, 'month': 'nov'}, 'age': 21}
#age vanne key add hunxa 

print(my_dict.items())
#output: dict_items([('name', 'Subash'), ('roll_no', 34), ('dob', {'year': 2057, 'month': 'nov'}), ('age', 21)])

print(my_dict.keys())
#output: dict_keys(['name', 'roll_no', 'dob', 'age'])

print(my_dict.values())
#output: dict_values(['Subash', 34, {'year': 2057, 'month': 'nov'}, 21])



print(my_dict["dob"]["year"])
#output: 2057

#deletion in dictonary:
my_dict.pop("age")
print(my_list)
#output: ['subash', 1, 2, 3, [4, 5, 6, 7, 8]]

del my_dict #del le dictionary nai delete gardinxa
# print(my_dict)
#output: NameError: name 'my_dict' is not defined

# TUPLES
# this datatype is immutable and has similar working mech of list

my_tuple = (1, 2, 3, "subash")
# my_tuple[3] = 3
print(my_tuple)
# output: my_tuple[3] = 3
# TypeError: 'tuple' object does not support item assignment


#SORTING

numbers = [90, 7,8,0, 89,79,69]

print(numbers)
#output: [90, 7, 8, 0, 89, 79, 69]

print(sorted(numbers))
#output:[0, 7, 8, 69, 79, 89, 90]

print(numbers)
#output: [90, 7, 8, 0, 89, 79, 69] 

numbers.sort()
print(numbers)
#output: [0, 7, 8, 69, 79, 89, 90] the sort function will change the original list

numbers.sort(reverse=True)
print(numbers)
#output: [90, 89, 79, 69, 8, 7, 0]


#STRING SLICING

name="Subash Shakya"
#this is index ranging
print(name[0:7])
#output: Subash

print(name[0:7:2])
#this is index stepping 
#third parameter takes the step value
#output: Sbs

print(name[::-1])
#output: aykahS hsabuS
#this is reversing the string with step as 1

my_name = ["subash", "raj", "shakya"]
print(" ".join(my_name) )
#output: subash raj shakya

some_name = "momo"

print(some_name.split())
#output:['momo']

print(list(some_name))
#output: ['m', 'o', 'm', 'o']

