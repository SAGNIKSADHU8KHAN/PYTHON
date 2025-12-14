import matplotlib.pyplot as plt

students_name = ["Sanjay", "Rahul", "Riya", "Priya", "Wasim", "Roy", "Iqbal"]

students_marks = [30, 35, 50, 25, 28, 32, 37]

marks_perc = []

for x in students_marks:
    res = (x/50)*100

    marks_perc.append(res)

print(marks_perc)


def marks_line_chart():

    plt.plot(students_name, students_marks)
    plt.title("Students marks graph")
    plt.xlabel("Students name")
    plt.ylabel("Students marks")
    plt.show()

marks_line_chart()


def percentage_bar_chart():

    plt.bar(students_name,marks_perc)
    plt.title("Students' percentage graph")
    plt.xlabel("Students' names")
    plt.ylabel("Students percentage ")
    plt.show()

percentage_bar_chart()