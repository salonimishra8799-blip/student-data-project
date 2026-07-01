# module 3

import pandas as pd

# dataset load karo
df = pd.read_csv("data/student_dataset_v2.csv")

# 1. Remove duplicate records
df = df.drop_duplicates()

# 2. Handle missing values

df["Marks"] = df["Marks"].fillna(df["Marks"].median())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].median())
df["StudyHours"] = df["StudyHours"].fillna(df["StudyHours"].median())

# 3. Remove invalid entries
# negative ya unrealistic 
df = df[(df["Marks"] >= 0) & (df["Marks"] <= 100)]

# 4. Validate Attendance (0 to 100 only)
df = df[(df["Attendance"] >= 0) & (df["Attendance"] <= 100)]

# 5. Validate Study Hours (0 to 24 only)
df = df[(df["StudyHours"] >= 0) & (df["StudyHours"] <= 24)]

# cleaned data save
df.to_csv("output/cleaned_data.csv", index=False)

print("Cleaned dataset saved successfully!")
import pandas as pd

# cleaned data load karo
df = pd.read_csv("output/cleaned_data.csv")

# module 4


# 1. Grade Column

def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

df["Grade"] = df["Marks"].apply(assign_grade)

# 
# 2. Result Column (Pass/Fail)
# 
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

#
# 3. Performance Score
# (weighted formula)

df["PerformanceScore"] = (
    (df["Marks"] * 0.5) +
    (df["Attendance"] * 0.3) +
    (df["StudyHours"] * 0.2)
)

# final file save
df.to_csv("output/transformed_data.csv", index=False)

print("Data transformation complete!")