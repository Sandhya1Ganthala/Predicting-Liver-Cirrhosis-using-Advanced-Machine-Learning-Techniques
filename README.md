# Predicting-Liver-Cirrhosis-using-Advanced-Machine-Learning-Techniques


project structure
liver_cirrhosis_predictor/
│
├── data/                            # 🔹 Raw and cleaned datasets
│   ├── raw/                         # Original dataset
│      └── liver_data.csv
│
├── models/                          # 🔹 Trained models and preprocessing objects
│   └── model.pkl                    # Trained ML model
│
├── notebooks/                       # 🔹 Jupyter notebooks for EDA and experiments


│   └── liver_cirrhosis_eda.ipynb    # Exploratory Data Analysis
│
├── src/                             # 🔹 Source code for training and prediction
│   ├── __init__.py
│   ├── train_model.py               # Script to train and save the model
│   ├── predict.py                   # Function to load model and make predictions
│   └── preprocess.py                # Data cleaning and preprocessing functions
│
├── app/                             # 🔹 Streamlit web application
│   ├── app.py                       # Main Streamlit UI
│   └── config.py                    # Constants or settings (optional)
│
├── requirements.txt                 # 🔹 Python dependencies
├── README.md                        # 🔹 Project overview and instructions
├── liver_cirrhosis_predictor.zip    # Final deliverable ZIP
└── LICENSE (optional)               # 🔹 License for project use        give the details to be filled in evry part 

✅ To Run the Project:
1.Extract the ZIP file.

2.Create and activate a virtual environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3.Install dependencies:
bash
pip install -r requirements.txt
4.Train the model
bash
python src/train_model.py
5.Run the Streamlit app
bash
streamlit run app/app.py

> If the app cannot import `src`, run Streamlit from the project root directory.

📄 LICENSE (MIT)
MIT License

Copyright (c) 2025 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMIT
🧪 Bonus Ideas for Enhancement
| Feature                | Description                                                               |
| ---------------------- | ------------------------------------------------------------------------- |
| SHAP Explainability    | Show feature contributions for individual predictions                     |
| Downloadable Report    | Allow exporting prediction as PDF for medical record keeping              |
| Database Integration   | Save prediction history using SQLite or PostgreSQL                        |
| Multi-model Comparison | Allow user to choose between different trained models (e.g., RF, XGBoost) |

🚀 Technologies Included
🧠 Machine Learning & Data Processing
| Technology       | Purpose                                                  |
| ---------------- | -------------------------------------------------------- |
| **scikit-learn** | Model training, data splitting, evaluation               |
| **pandas**       | Data manipulation and preprocessing                      |
| **NumPy**        | Numerical operations (used internally by pandas/sklearn) |

📊 Exploratory Data Analysis (EDA)
| Technology     | Purpose                                                  |
| -------------- | -------------------------------------------------------- |
| **Matplotlib** | Data visualization                                       |
| **Seaborn**    | Advanced visualizations (correlation heatmaps, boxplots) |

🧼 Preprocessing & Serialization
| Technology | Purpose                               |
| ---------- | ------------------------------------- |
| **joblib** | Saving and loading models efficiently |

🌐 Web Application
| Technology    | Purpose                        |
| ------------- | ------------------------------ |
| **Streamlit** | Interactive UI for predictions |

📝 Notes for Documentation / Presentation
🔍 Problem Statement
Liver cirrhosis is a serious chronic liver disease. Early prediction can help in reducing complications and improving patient survival.

🎯 Project Goals
Predict cirrhosis risk using patient clinical data.

Make the model accessible via an easy-to-use web interface.

Demonstrate the power of ML in medical decision support.

🛠️ Project Workflow
Data Loading – Load liver patient data.

Data Cleaning – Handle missing values, encode categorical fields.

Feature Selection – Use relevant clinical markers (e.g., bilirubin, enzymes).

Model Training – Use RandomForestClassifier for high accuracy.

Model Evaluation – Use accuracy, precision, recall (optional enhancement).

Model Saving – Save trained model for reuse.

UI Deployment – Enable prediction via Streamlit frontend.

🏥 Clinical Features Used
Age, Gender

Total/Direct Bilirubin

Alkaline Phosphotase, SGPT, SGOT

Total Proteins, Albumin

Albumin/Globulin Ratio

🧪 Model Output
Risk Prediction: Cirrhosis (1) or Not (0)

Optionally: Probability of cirrhosis (e.g., 0.83)

#zipfile: [liver_cirrhosis_predictor (2).zip](https://github.com/user-attachments/files/21320440/liver_cirrhosis_predictor.2.zip)

#demofile: https://drive.google.com/file/d/1LYfllaQVMCxCyNCFCgVgl-zuaTTf14ly/view?usp=drivesdk
