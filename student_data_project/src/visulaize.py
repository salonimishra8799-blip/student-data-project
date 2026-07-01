import pandas as pd
import matplotlib.pyplot as plt

# transformed data load karo (Grade already present hota hai)
df = pd.read_csv("output/transformed_data.csv")

# -------------------------
# 1. Grade Distribution Graph
# -------------------------
plt.figure()

df["Grade"].value_counts().plot(kind="bar")

plt.title("Grade Distribution of Students")
plt.xlabel("Grade")
plt.ylabel("Number of Students")

plt.show()
# plt.figure()

# plt.scatter(df["Attendance"], df["Marks"])

# plt.title("Attendance vs Marks")
# plt.xlabel("Attendance")
# plt.ylabel("Marks")

# plt.show()