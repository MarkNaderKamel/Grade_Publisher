#student_info={"Mina", "John", "Jeoe", "Poul", "Pole", "Jean"}
student_pin={
    "Mina":"2001",
    "John":"2002", 
    "Jeo":"2003",
    "Poul":"2004", 
    "Pole":"2005", 
    "Jean":"2006"
    }
mina_grades= "Not Ready Yet"
andrew_grades= {"Math":"50", "English":"50", "Art":"50","History":"50"}
Jeo_grades= {"Math":"50", "English":"50", "Art":"50","History":"50"}
Poul_grades= "Not Ready Yet"
Pole_grades= {"Math":"50", "English":"50", "Art":"50","History":"50"}
Jean_grades= {"Math":"50", "English":"50", "Art":"50","History":"50"}

student_name=input("What's Your Name? \n").strip().capitalize()
student_password=input("What's Your Password? \n")

if student_name in student_pin and student_pin[student_name] == student_password:
    print(f"Greetings {student_name}")
    print("You have successfully Logged in")
    if student_name == "Poul":
        print("Your Grades Are:")
        print("Subject   | Grade")
        print("-----------------")
        for subject, grade in Poul_grades.items():
            print(f"{subject:<10} | {grade}")
    elif student_name == "Mina":
        print("Your Grades Are:")
        print("Subject   | Grade")
        print("-----------------")
        for subject, grade in mina_grades.items():
            print(f"{subject:<10} | {grade}")
    elif student_name == "John":
        print("Your Grades Are:")
        print("Subject   | Grade")
        print("-----------------")
        for subject, grade in andrew_grades.items():
            print(f"{subject:<10} | {grade}")   
    elif student_name == "Jeo":
        print("Your Grades Are:")
        print("Subject   | Grade")
        print("-----------------")
        for subject, grade in Jeo_grades.items():
            print(f"{subject:<10} | {grade}")
    elif student_name == "Pole":
        print("Your Grades Are:")
        print("Subject   | Grade")
        print("-----------------")
        for subject, grade in Pole_grades.items():
            print(f"{subject:<10} | {grade}")
    elif student_name == "Jean":
        print("Your Grades Are:")
        print("Subject   | Grade")
        print("-----------------")
        for subject, grade in Jean_grades.items():
            print(f"{subject:<10} | {grade}")
    else:
        print("Your're a Student With Us")
elif student_name in student_pin and student_pin[student_name] != student_password: 
    print(f"Greetings {student_name}, Could You Please Check Your Password")                     
   
else:
    print("Something is Wrong, Please Check with Yout ITS Administrator")
