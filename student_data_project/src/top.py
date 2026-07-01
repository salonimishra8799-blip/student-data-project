import pandas as pd

df = pd.read_csv("output/transformed_data.csv")

# Top 10 students by Marks
top10 = df.sort_values(by="Marks", ascending=False).head(10)

print("\n🏆 TOP 10 STUDENTS:\n")
print(top10)