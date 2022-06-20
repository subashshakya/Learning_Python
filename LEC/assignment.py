# #ASSIGNMENT: 
# Create a function that takes "staffs" as input and returns the output as expected below:

# Guide:
# 1. Evaluate the maximum value from the "scores" key of every dictionary.
# 2. Remove the "scores" from each dictionary and add the "max_score" key in the dictionary. 
#     "max_score" represents the maximum value among the "scores" list of respective dictionary.
# 3. Print the final output after receiving from the solution function

staff=[]

def find_max(value):
    max = value[0]
    for val in value:
        if(max<int(val)):
            max = val
    return max

for i in range(2):
    roll = input("Enter you roll number")
    name = input("Enter your name")
    scores = input("enter your scores")
    score_list = scores.split(',')
    s = []
    for scr in score_list:
        s.append(int(scr))
    item = {"roll": int(roll), 
            "name": name,
            "scores": s
    }
    staff.append(item)
    print(item["scores"])
    

for item in staff:
    score = item["scores"]
    max = find_max(score)
    print(max)
    item["scores"] = max

print(staff)