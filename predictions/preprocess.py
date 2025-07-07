import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df.columns = ['Age','Gender','Total_Bilirubin','Direct_Bilirubin',
                  'Alkaline_Phosphotase','SGPT','SGOT','Total_Proteins',
                  'Albumin','A/G_Ratio','Dataset']
    df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
    df.dropna(inplace=True)
    df['Dataset'] = df['Dataset'].apply(lambda x: 1 if x == 1 else 0)
    return df
