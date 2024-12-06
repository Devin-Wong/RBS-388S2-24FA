import pandas as pd

d = {
    "hw": [100, 99, 98],
    'mid-term': [90, 88, 95],
    'final': [94, 92, 85]
}
df = pd.DataFrame(d, index= ["Jack", "Mary", "Ben"])
# print(df)

# --- write  ---
# df.to_csv('grade.csv')

# read
# df_grade = pd.read_csv("grade.csv")
# print(df_grade)


# print(df.info())
# print(df.describe())

hw = df['hw'].to_numpy()
print(hw)