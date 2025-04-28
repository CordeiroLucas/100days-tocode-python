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
result = {name:len(name) for name in sentence.split(" ")}


# convert Celsius to Fahrenheit
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)