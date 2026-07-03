English = 0
Maths = 0
Science = 0
Social = 0
Computer = 0
Total_mark = 0
Average_Mark = 0

def get_marks():
    global English, Maths, Science, Social, Computer
    English = int(input("Enter your marks in English: "))
    Maths = int(input("Enter your marks in Maths: "))
    Science = int(input("Enter your marks in Science: "))
    Social = int(input("Enter your marks in Social: "))
    Computer = int(input("Enter your marks in Computer: "))
    return English, Maths, Science, Social, Computer
get_marks()
def calculate_total():
    global Total_mark, English, Maths, Science, Social, Computer
    Total_mark = English + Maths + Science + Social + Computer
    return Total_mark
calculate_total()
def calculate_average():
    global Average_Mark, English, Maths, Science, Social, Computer
    Average_Mark = (English + Maths + Science + Social + Computer) / 5
    return Average_Mark
calculate_average()
def find_grade(subjects):
    if subjects >= 90:
        return "A"
    elif subjects >= 80:
        return "B"
    elif subjects >= 70:
        return "C"
    elif subjects >= 60:
        return "D"
    else:
        return "F"
def display_results():
    global English, Maths, Science, Social, Computer, Total_mark, Average_Mark
    print("Marks in English:", English)
    print("Grade in English:", find_grade(English))
    print("Marks in Maths:", Maths)
    print("Grade in Maths:", find_grade(Maths))
    print("Marks in Science:", Science)
    print("Grade in Science:", find_grade(Science))
    print("Marks in Social:", Social)
    print("Grade in Social:", find_grade(Social))
    print("Marks in Computer:", Computer)
    print("Grade in Computer:", find_grade(Computer))
    print("Total Marks:", Total_mark)
    print("Average Marks:", Average_Mark)
display_results()
