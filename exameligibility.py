total_classes = int(input("Enter the total number of classes held"))
attended_classes = int(input("Enter the number of classes attended"))

attendance_percentage = (attended_classes / total_classes) 

print(f" Attendance percentage : , {attendance_percentage * 100 }%")

if attendance_percentage >= 75:
    print("The student is eligible for the exam")

else:
    print("The student is not eligible for the exam")    




