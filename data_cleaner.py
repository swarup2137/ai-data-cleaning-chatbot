import pandas as pd

def clean_data(df):

    report = []

    # remove duplicates
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        df = df.drop_duplicates()
        report.append(f"Removed {duplicates} duplicate rows")

    # fill missing values
    missing = df.isnull().sum().sum()
    if missing > 0:
        df = df.fillna(method="ffill")
        report.append(f"Filled {missing} missing values")

    return df, report