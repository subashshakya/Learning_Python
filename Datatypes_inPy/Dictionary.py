# Dictionary datatype
# has a key and value

my_dictionary = {'key': 'value', 'subash': 'shakya'}
container = my_dictionary.get('key')
container_1 = my_dictionary.get('subash')
print(container)
print(container_1)
print(my_dictionary)

# putting lists inside a dictionary

List_dict = {'list1': [1, 2, 3, 4], 'list2': ["subash", "shakya"]}
value_in_key1 = List_dict.get('list1')
print(value_in_key1)
value_in_key2 = List_dict.get('list2')
print(value_in_key2)

# showing the values in the dictionary

long_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for x in long_dict:
    print(x)    # this gives us key
    print(x, long_dict[x])   # gives key and value


# merging dictionaries
dict_1 = {'name': "subash", 'surname': "shakya", 'address': "Lalitpur"}
dict_2 = {'name': "starbucks", 'what_is_it': "coffee"}

merged_dict = {**dict_1, **dict_2}
print(merged_dict)
# output: {'name': 'starbucks', 'surname': 'shakya', 'address': 'Lalitpur', 'what_is_it': 'coffee'}
# if the keys are the same then the value of the second or the last similar key will replace the values of all the similar keys

# accessing the values or keys of the dictionary

dict_4 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

x = dict_4.get('a')
print(x)