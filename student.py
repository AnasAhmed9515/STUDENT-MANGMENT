import data
student_list = data.Student_list()
def add_student():
    rollno = int(input("Enter roll no:"))
    if rollno in student_list:
        print("Student exist:")
    else:
        student_list[rollno]={"Name":input("Enter student Name:"),
                                  "Course":input("Enter your Course:"),
                                  "MARKS":[int(input("Enter your marks in subject 1:")),
                                   int(input("Enter your marks in subject 2:")),
                                   int(input("Enter your marks in subject 3:")),
                                   int(input("Enter your marks in subject 4:")),
                                   int(input("Enter your marks in subject 5:"))]}
    print("======================================")
    print("======================================")
    print("=======STUDENT ADDED SUCCESSFULLY=====")
    return student_list,rollno


def view_student():
    if len(student_list) == 0:
        print("No students found.")
    else:
        for i in student_list:
            print("Roll no:",i)
            print("Name:",student_list[i]["Name"])
            print("Course:",student_list[i]["Course"])
            print("Marks:",student_list[i]["MARKS"])
            print("Total Marks:",sum(student_list[i]["MARKS"]))
            print("AVg marks:",(sum(student_list[i]["MARKS"])/len(student_list[i]["MARKS"])))
            if (sum(student_list[i]["MARKS"])/len(student_list[i]["MARKS"])) >= 90:
                print("Grade:A")
            elif (sum(student_list[i]["MARKS"])/len(student_list[i]["MARKS"])) >= 80:
                print("Grade:B")
            elif (sum(student_list[i]["MARKS"])/len(student_list[i]["MARKS"])) >= 70:
                print("Grade:C")
            elif (sum(student_list[i]["MARKS"])/len(student_list[i]["MARKS"])) >= 40:
                print("Grade:D")
            else:
                print("Grade:F")
            print("======================================")
            print("======================================")
            print("============STUDENT DETAILS===========")
def search_student():
    rollno = int(input("Enter roll no to search:"))
    if rollno in student_list:
        for i in student_list:
            print("Roll no:",i)
            print("Name:",student_list[i]["Name"])
            print("Course:",student_list[i]["Course"])
            print("Marks:",student_list[i]["MARKS"])
            print("Total Marks:",sum(student_list[i]["MARKS"]))
            print("AVg marks:",(sum(student_list[i]["MARKS"])/len(student_list[i]["MARKS"])))
            if (sum(student_list[i]["MARKS"])/len(student_list[i]["MARKS"])) >= 90:
                print("Grade:A")
            elif (sum(student_list[i]["MARKS"])/len(student_list[i]["MARKS"])) >= 80:
                print("Grade:B")
            elif (sum(student_list[i]["MARKS"])/len(student_list[i]["MARKS"])) >= 70:
                print("Grade:C")
            elif (sum(student_list[i]["MARKS"])/len(student_list[i]["MARKS"])) >= 40:
                print("Grade:D")
            else:
                print("Grade:F")   
    else:
        print("Student not exist")
    print("======================================")
    print("======================================")
    print("=============SEARCH RESULTS===========")
