import student
def cal_marks():
    rollno = int(input("Enter rollno to calculate total marks:"))
    if rollno in student.student_list:
        print("TOTAL:",((sum(student.student_list[rollno]["MARKS"]))))
        print("AVG:",((sum(student.student_list[rollno]["MARKS"])/len(student.student_list[rollno]["MARKS"]))))
        if (sum(student.student_list[rollno]["MARKS"])/len(student.student_list[rollno]["MARKS"])) >= 90:
            print("Grade:A")
        elif (sum(student.student_list[rollno]["MARKS"])/len(student.student_list[rollno]["MARKS"])) >= 80:
            print("Grade:B")
        elif (sum(student.student_list[rollno]["MARKS"])/len(student.student_list[rollno]["MARKS"])) >= 70:
            print("Grade:C")
        elif (sum(student.student_list[rollno]["MARKS"])/len(student.student_list[rollno]["MARKS"])) >= 40:
            print("Grade:D")
        else:
            print("Grade:F")
    else:
        print("Student not exist")
    print("======================================")
    print("======================================")
    print("============STUDENT RESULTS===========")


def top_student():
    top=0
    top_student_rollno = None
    top_student_name = None
    if len(student.student_list)==0:
        print("No student exist")
    else:
        for i in student.student_list:
            avg = sum(student.student_list[i]["MARKS"])/len(student.student_list[i]["MARKS"])
            if avg>top:
                top = avg
                top_student_rollno = i
                top_student_name = student.student_list[i]["Name"]
        print("=======================")
        print("🏆TOP STUDENT DETAILS🏆")
        print("======================")
        print("Top Student Roll No:",top_student_rollno)
        print("Top Student Name:",top_student_name)
        print("Top Student Average Marks:",top)
    