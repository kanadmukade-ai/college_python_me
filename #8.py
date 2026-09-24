marks = []
for i in range(1, 6):
    score = float(input(f"Enter marks for Subject {i}: "))
    marks.append(score)

total_marks = sum(marks)
percentage = (total_marks / 500) * 100

print(f"Total Marks: {total_marks}/500")
print(f"Percentage: {percentage:.2f}%")
