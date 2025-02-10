# For Loops

student_scores = [21,24,54,11,1,2,45,74,88,11,44,55,54, 199, 158, 123, 54, 22, 65]

highest = 0

for score in student_scores:
    if score > highest:
        highest = score

print(highest)