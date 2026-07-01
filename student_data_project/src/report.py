# module 7
import pandas as pd

# transformed data load karo (Grade bhi safe rahega)
df = pd.read_csv("output/transformed_data.csv")

# 
# 1. Sort by Marks (High to Low)

marks_sorted = df.sort_values(by="Marks", ascending=False)
print("\n Students Sorted by Marks:\n")
print(marks_sorted)

# 
# 2. Sort by Attendance (High to Low)

attendance_sorted = df.sort_values(by="Attendance", ascending=False)
print("\n Students Sorted by Attendance:\n")
print(attendance_sorted)

#
# 3. Sort by Study Hours (High to Low)

study_sorted = df.sort_values(by="StudyHours", ascending=False)
print("\n Students Sorted by Study Hours:\n")
print(study_sorted)


marks_sorted.to_csv("output/sorted_by_marks.csv", index=False)
attendance_sorted.to_csv("output/sorted_by_attendance.csv", index=False)
study_sorted.to_csv("output/sorted_by_studyhours.csv", index=False)

print("\n Sorting completed and files saved!")

# module 8

import pandas as pd

# transformed data l
df = pd.read_csv("output/transformed_data.csv")

#
# 1. Average Marks by Grade

avg_marks_grade = df.groupby("Grade")["Marks"].mean()
print("\nAverage Marks by Grade:\n")
print(avg_marks_grade)

#
# 2. Number of Students in Each Grade

count_grade = df["Grade"].value_counts()
print("\n Number of Students in Each Grade:\n")
print(count_grade)


# 3. Average Attendance by Grade

avg_attendance_grade = df.groupby("Grade")["Attendance"].mean()
print("\nAverage Attendance by Grade:\n")
print(avg_attendance_grade)
