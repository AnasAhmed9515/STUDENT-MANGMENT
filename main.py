import student
import result

while True:
    print("======================================")
    print("        STUDENT RESULT MANAGMENT     ")
    print("======================================")
    print("1.ADD STUDENT")
    print("2.VIEW STUDENT")
    print("3.SEARCH STUDENT")
    print("4.CALCULATE TOTAL MARKS")
    print("5.DISPLAY TOP STUDENT")
    print("6.EXIT")
    x = int(input("Select option 1 to 6 :  "))
    if x == 1:
        student.add_student()
    elif x == 2:
        student.view_student()
    elif x == 3:
        student.search_student()
    elif x == 4:
        result.cal_marks()
    elif x == 5:
        result.top_student()
    elif x == 6:
        print("Exiting...")
        break
    else:
        print("Invalid option. Please select a valid option.")
