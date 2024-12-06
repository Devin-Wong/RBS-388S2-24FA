import pandas as pd

d = {
    "hw": [100, 99, 98],
    'mid-term': [90, 88, 95],
    'final': [94, 92, 85]
}
df = pd.DataFrame(d, index= ["Jack", "Mary", "Ben"])
print(df)
# ---- select columns ------
# # method 1: use column number
# hw = df.iloc[:,0]
# print(hw)

# # method 2: use column name(s)
# hw = df['hw']
# # print(hw)

# hw_midterm = df[ ["hw", "mid-term"] ]
# print(hw_midterm)

# --- insert new columns -----
project = [95, 80, 85]
df["project"] = project
print(df)

# --- conditional selection ----

df_project_greater90 = df[df["project"]>90]
print(df_project_greater90)

