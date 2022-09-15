def get_grade(score):
    if 90 < score < 101:
        return "A"
    elif 80 < score < 91:
        return "B"
    elif 70 < score < 81:
        return "C"
    elif score <= 70:
        return "F"
        
score = int(input())
grade = get_grade(score)
print(grade)
