
import pandas as pd

# Read the CSV file from the data folder
df = pd.read_csv("data/student_dataset_v2.csv")



# Module 1 : Data Loading


# Display the first 5 rows of the dataset
print(" First 5 Records")
print(df.head())


# Display the last 5 rows of the dataset
print("\n Last 5 Records ")
print(df.tail())


# Display the number of rows and columns
print("\n Shape of Dataset ")
print(df.shape)


# Display all column names
print("\nColumn Names ")
print(df.columns)


# Display the data type of each column
print("\n Data Types ")
print(df.dtypes)
# ===========================
# Module 2 : Data Inspection
# ===========================

# Display the number of missing (null) values in each column
print("\nMissing Values ")
print(df.isnull().sum())


# Display the number of duplicate records
print("\nDuplicate Records ")
print(df.duplicated().sum())


# Display statistical summary of numerical columns
print("\nDescriptive Statistics ")
print(df.describe())


# Display memory usage of each column
print("\nMemory Usage -")
print(df.memory_usage())


# Display complete summary information of the dataset
print("\n- Dataset Information")
df.info()