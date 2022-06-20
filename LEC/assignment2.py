#assignment 2:

import math

accounts = [
    {"account_number": '1', 'title': 'First Year'},
    {"account_number": '1.1', 'title': 'Biswash', "fees_paid": 20000},
    {"account_number": '1.2', 'title': 'Nikita', "fees_paid": 48000},
    {"account_number": '2', 'title': 'Second Year'},
    {"account_number": '2.1', 'title': 'Yashmini', "fees_paid": 35000},
    {"account_number": '2.2', 'title': 'Anshul', "fees_paid": 27000},
    {"account_number": '3', 'title': 'Third Year'},
    {"account_number": '3.1', 'title': 'Arun', "fees_paid": 92000},
    {"account_number": '3.2', 'title': 'Jeshika', "fees_paid": 56000},
    {"account_number": '4', 'title': 'Fourth Year'},
    {"account_number": '4.1', 'title': 'Seeru', "fees_paid": 23000},
    {"account_number": '4.2', 'title': 'Kushal', "fees_paid": 87000},
]

def is_int(accounts):
    check = accounts["account_number"].find('.')
    if check == 1:
        return True
    else:
        return False

student_list = list(filter(is_int, accounts))


def int_list(accounts):
    check = accounts["account_number"].find('.')
    if check == -1:
        return True
    else:
        return False

accounts = list(filter(int_list, accounts))

total_fee = 0
std = []
for account in accounts:
    for student in student_list:
        if int(account["account_number"]) == int(float(student["account_number"])):
            if math.floor(float(account["account_number"])) == math.floor(float(student["account_number"])):
                std.append(student)
                total_fee += student["fees_paid"]
        else:
            pass
    account["total_fees"] = total_fee
    account["students"] = std



print(accounts)







