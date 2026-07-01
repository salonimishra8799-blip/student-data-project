# module 11
import os
import pandas as pd

# ensure output folder exists
os.makedirs("output", exist_ok=True)



# 1. cleaned data
cleaned_df = pd.read_csv("output/cleaned_data.csv")
cleaned_df.to_csv("output/cleaned_data.csv", index=False)

# 2. toppers
toppers_df = pd.read_csv("output/top_performing_students.csv")
toppers_df.to_csv("output/toppers.csv", index=False)

# 3. failed students
failed_df = pd.read_csv("output/failed_students.csv")
failed_df.to_csv("output/failed_students.csv", index=False)

# 4. report
report_df = pd.read_csv("output/report.csv")
report_df.to_csv("output/report.csv", index=False)

print(" All files successfully stored inside OUTPUT folder!")