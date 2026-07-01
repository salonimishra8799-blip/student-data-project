# module 5
import pandas as pd

# cleaned data 
df = pd.read_csv("output/cleaned_data.csv")

# ----------------------------
# 1. Top Performing Students
# (Marks >= 75)

top_students = df[df["Marks"] >= 75]
top_students.to_csv("output/top_performing_students.csv", index=False)

# 
# 2. Failed Students
# (Marks < 40)

failed_students = df[df["Marks"] < 40]
failed_students.to_csv("output/failed_students.csv", index=False)

# 
# 3. Attendance < 75%
# 
low_attendance = df[df["Attendance"] < 75]
low_attendance.to_csv("output/low_attendance_students.csv", index=False)

# 
# 4. Study Hours > 8

hard_workers = df[df["StudyHours"] > 8]
hard_workers.to_csv("output/students_study_more_than_8hrs.csv", index=False)

print("Module 5 completed: All filtered datasets saved!")
# module 6
import pandas as pd

df = pd.read_csv("output/transformed_data.csv")

print(" DATA ANALYSIS REPORT\n")

print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

print("\nAverage Attendance:", df["Attendance"].mean())
print("Average Study Hours:", df["StudyHours"].mean())

# Pass/Fail
total = len(df)
pass_count = len(df[df["Marks"] >= 40])
fail_count = len(df[df["Marks"] < 40])

print("\nPass %:", (pass_count/total)*100)
print("Fail %:", (fail_count/total)*100)

# Grade distribution
print("\nGrade Distribution:\n", df["Grade"].value_counts())
