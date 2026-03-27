def process_student(name, score):
    # validate
    if not name:
        print("Error: name is empty")
        return
    if score < 0 or score > 100:
        print("Error: score must be between 0 and 100")
        return
    
    # classify grade
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    # format result
    result = f"{name} scored {score} and got grade {grade}"
    print(result)
    
    # save to list
    students.append({"name": name, "score": score, "grade": grade})
    print(f"Saved {name} to student list")

students = []
process_student("John", 85)
process_student("", 85)
process_student("Mary", 105)



