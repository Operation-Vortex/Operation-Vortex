def process_student_cleanly(name, score):
    if not validater(name, score):
        return
    grade = grader(score)
    result = result_formatter(name, score, grade)
    saver(name, score, grade)
    print(result)

def validater(name, score):
    if not name:
        print("Error: name is empty")
        return False
    if score < 0 or score > 100:
        print("Error: score must be between 0 and 100")
        return False
    return True
    
def grader(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
        
def result_formatter(name, score, grade):
    return f"{name} scored {score} and got grade {grade}"
    

def saver(name, score, grade):
    students.append({"name": name, "score": score, "grade": grade})
    print(f"Saved {name} to student list")


students = []
process_student_cleanly("John", 85)
process_student_cleanly("", 85)
process_student_cleanly("Mary", 105)