students = []
while True:
    print("\n----GRADING SYSTEM----")
    print("1.Add student")
    print("2.Display all")
    print("3.Class summary")
    print("4.Exit")
    choice = input("option: ")
    if choice == "1":
        studentnumber = input("studentnumber: ")
        if not (studentnumber.isdigit() and studentnumber.startswith("20") and len(studentnumber) == 6):
            print("invalid studentnumber.it must start with 20 and contain 6 digits")
            continue
        name = input("Enter name: ")
        score = int(input("score: "))
        if score >= 80:
            grade = "A"
            decision = "excellent"
        elif score >= 70:
            grade = "B"
            decision = "very good"
        elif score >= 60:
            grade = "C"
            decision = "good"
        elif score >= 50:
            grade = "D"  
            decision = "pass"  
        else:
            grade = "F"
            decision = "fail"
        student = {
            "name": name,
            "studentnumber": studentnumber,
            "score": score,
            "grade": grade,
            "decision": decision 
             }
        students.append(student)
        print("student successfully added")
        print(f"grade:{grade}")
        print(f"decision:{decision}")
    elif choice == "2":
        print("\n---student list---")
        print(students)
    elif choice == "3":
        print("\n---class summary---")
        if len(students) == 0:
            print("no student regisgtered")
        else:    
          passes = 0 
          fails = 0
          scores = [s['score'] for s in students]
          total_students = len(students)
          highest = max(scores)
          lowest = min(scores)
          average = sum(scores)/len(scores)
          for student in students:
            if student['score'] >= 50:
                passes += 1
            else:
                fails += 1
                print("fails: ")
        print(f"passes = {passes} ")
        print(f"fails = {fails} ")
        print(f"total: {total_students}")        
        print(f"highest score: {highest}")
        print(f"lowest score: {lowest}")
        print(f"average score: {average}")
    elif choice == "4":
        print("exit")        
    else:
        print("invalid option")        
            