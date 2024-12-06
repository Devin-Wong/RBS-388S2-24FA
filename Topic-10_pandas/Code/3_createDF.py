import pandas as pd

# from pd.Series
hw_series = pd.Series([100, 99, 98, 103], index=["Jack", "Mary", "Ben", "Jin"])
mid_term_series = pd.Series([90, 88, 95], index=["Jack", "Ben", "Mary"])
final_series = pd.Series([94, 92, 85], index=["Jack", "Mary", "Ben"])

d = {
    "hw": hw_series,
    "mid-term": mid_term_series,
    'final':final_series
}

df = pd.DataFrame(d)
print(df)