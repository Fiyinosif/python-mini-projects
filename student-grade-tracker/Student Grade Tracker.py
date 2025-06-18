print("Student Grade Tracker")
print("""
      Welcome
      Instructions : 
      1. press 1 to add record.
      2. Press 2 for print all student names and grades
      3. Press 3 to fnd a student.
      4. Press 4 to quit program.
      """)



class_grade = {}

while True:
    print()
    response = int(input("Pick an option: "))

    if response == 1 : 
        student_name = input("Student name: ").capitalize()
        student_grade = int(input("Student grade: "))
        class_grade.update({student_name:student_grade})
          

    elif response == 2:
        if not class_grade:
            print("No records yet")
        else:    
            for name,grade in class_grade.items():
                if grade >= 80 :
                    result = "A - Excellent"
                elif 60 <= grade < 80 :
                    result = "B - Good"
                elif 40 <= grade < 60 : 
                    result = "C - Pass"    
                else :
                    result = "F - Failed"     
                print(f"Student name: {name} , Student grade: {grade}, Result: {result} ")
                print()
    
    elif response == 3: 
        target_name = input("Name of student : ").capitalize()
        if target_name in class_grade.keys():
            if class_grade[target_name] >= 80 :
                    result = "A - Excellent"
            elif 60 <= class_grade[target_name] < 80 :
                result = "B - Good"
            elif 40 <= class_grade[target_name] < 60 : 
                result = "C - Pass"    
            else :
                result = "F - Failed" 
            print(f"Record found: Student name: {target_name} , Student grade: {class_grade[target_name]}, Result: {result} ")

        else:
            print(f"No record of {target_name} found.")

    elif response == 4:
        print("Program ended. Goodbye!")
        break   

    else:
        print("Option not valid , pick an option among 1,2,3.")     







 