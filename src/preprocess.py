import os
import pandas as pd


def clean_data(file_path):
    if os.path.isdir(file_path):
        csv_files = [f for f in os.listdir(file_path) if f.endswith('.csv')]
        if not csv_files:
            raise FileNotFoundError(f"No CSV file found in directory: {file_path}")
        file_path = os.path.join(file_path, csv_files[0])

    with open(file_path, 'r', encoding='utf-8') as f:
        first_line = f.readline().strip()
    skiprows = 1 if ',' not in first_line else 0

    df = pd.read_csv(file_path, skiprows=skiprows)
    if list(df.columns) != ['Age', 'Gender', 'Total_Bilirubin', 'Direct_Bilirubin',
                             'Alkaline_Phosphotase', 'SGPT', 'SGOT', 'Total_Proteins',
                             'Albumin', 'A/G_Ratio', 'Dataset']:
        df.columns = ['Age', 'Gender', 'Total_Bilirubin', 'Direct_Bilirubin',
                      'Alkaline_Phosphotase', 'SGPT', 'SGOT', 'Total_Proteins',
                      'Albumin', 'A/G_Ratio', 'Dataset']

    df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
    df.dropna(inplace=True)
    df['Dataset'] = df['Dataset'].apply(lambda x: 1 if x == 1 else 0)
    return df
