# # List Comprehension

# new_numbers = [n*2 for n in range(1,50) if n % 2 == 0]

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# new_names = [name.upper() for name in names if len(name) > 5]

# file1 = open("day26/file1.txt") 
# file2 = open("day26/file2.txt")

# result1 = [int(num.strip('\\n')) for num in file1.readlines()]
# result2 = [int(num.strip('\\n')) for num in file2.readlines()] 

# result = [num for num in result1 if num in result2]


# Dict Comprehension

import random
student_scores = {student:random.randint(1,100) for student in names}


passed_students = {key:value for (key,value) in student_scores.items() if value >= 60}


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {name:lenght for (name, lenght) in sentence.strip(" ")}

print(result)