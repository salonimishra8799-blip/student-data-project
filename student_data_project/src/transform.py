# module 9
import pandas as pd

df = pd.read_csv("output/transformed_data.csv")

# -------------------------
# Basic Statistics
# -------------------------
print("\n📊 STATISTICAL ANALYSIS\n")

print("Mean:\n", df.mean(numeric_only=True))
print("\nMedian:\n", df.median(numeric_only=True))
print("\nMode:\n", df.mode(numeric_only=True).iloc[0])

print("\nStandard Deviation:\n", df.std(numeric_only=True))
print("\nVariance:\n", df.var(numeric_only=True))

# -------------------------
# Correlation Matrix
# -------------------------
print("\nCorrelation Matrix:\n")
print(df.corr(numeric_only=True))
# module10
import pandas as pd

df = pd.read_csv("output/transformed_data.csv")

total_students = len(df)
passed = len(df[df["Marks"] >= 40])
failed = len(df[df["Marks"] < 40])

report = {
    "Total Students": [total_students],
    "Passed Students": [passed],
    "Failed Students": [failed],
    "Highest Marks": [df["Marks"].max()],
    "Lowest Marks": [df["Marks"].min()],
    "Average Marks": [df["Marks"].mean()],
    "Average Attendance": [df["Attendance"].mean()]
}

report_df = pd.DataFrame(report)

# Grade distribution add karo
grade_dist = df["Grade"].value_counts().to_dict()

print("\n REPORT SUMMARY:\n")
print(report_df)
print("\nGrade Distribution:\n", grade_dist)

# save report
report_df.to_csv("output/report.csv", index=False)

print("\n Report saved successfully!")