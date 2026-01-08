# AutoJudge : Predicts Programming Problem Difficulty 

## Project Overview:
**AutoJudge** is a ML-based system designed to evaluate coding problems (like those at Codeforces, Kattis, Codechef, etc.) by predicting their difficulty and categorizing them into Classes, Formally **Easy**, **Medium**, or **Hard** levels. The system uses machine learning models for classification and regression to provide accurate difficulty scores and supports a basic user-friendly web interface for interaction. Generally, this process usually depends on human judgement and user feedback, but AutoJudge predictions is solely based on textual data (Title, Description, Input/Output description).

---

## Dataset Used:
Since, predictions are based on textual data, therefore, the project is based on a dataset containing coding problems (About 4112 problems) with the following textual data and result of difficulty level:  
- Title
- Description
- Input desciption
- Output description
- Problem Class
- Problem Score

Addition to these textual data, some additional data that was present in the raw data file were:
- Sample Input/Output
- url for the problem
---

## Approach and Models Used

### Data Preprocessing
- Raw data in `.jsonl` format converted to `.csv` format
- Analyzing the data before use, includes:
    - Class-wise no. of problems
    - Class-wise Min., Max., and Median scores
    - Length of description
- Cleaning and normalizing problem statements 
- Handling missing values
- Converting all text fields into single text field (user_input)
- Differentiating Title, Description, input/output description in user_input
- Finally Splitting the data into two parts- Training (80% of data) and Testing (20% of data)

### Feature Extraction
- Text-based features using TF-IDF (Term Frequency-Inverse Document Frequency)
- TF-IDF is used to mark words according to their frequency
- Numerical features (e.g., count of keywords, arithmetic operations, etc. )
- Keywords include `greedy`,`dp`,`dynamic programming`,`tree`,`graph`,`dfs`,`bfs`,`two pointers`,`binary search`,`bitmasks`,`dfs`,`combinatorics`  

### Models
1. **Classification Model** :  Predicts class-wise difficulty (Easy / Medium / Hard)
   - Logistic Regression
   - Support Vector Machine (Linear SVM)
   - Multinomial Naive Bayes
   - Random Forest classifier

2. **Regression Model** : Predicts continuous difficulty score on a scale of 10
   - Linear Regression
   - Ridge Regressor
   - Random Forest Regressor
   - Gradient Boosting Regressor

---

### Evaluation Metrics
- **Classification:** `Accuracy`, `f1-score`, `Confusion Matrix`  
- **Regression:** `Mean Absolute Error (MAE)`, `Root Mean Squared Error (RMSE)`  

## Model Results
1. **Classification:**
   
|        Model       |  Accuracy | F1-Score (Easy) | F1-Score (Med.) | F1-Score (Hard) |
|--------------------|-----------|-----------------|-----------------|-----------------|
| Logistic Regression| 0.466     | 0.46            | 0.35            | 0.56            |
|     Linear SVM     | 0.210     | 0.32            | 0.00            | 0.11            |
|   Multinomial NB   | 0.482     | 0.10            | 0.19            | 0.65            |
|    Random Forest   | 0.526     | 0.44            | 0.24            | 0.66            |

- Linear Reg: It struggles while predicting Medium and Hard problems
- Linear SVM: It predicts most of the problems as Easy
- Multinomial NB: It predicts almost all problems as Medium
- Random Forest: It is mainly confused between Easy-Medium and sometimes between Medium-Hard

- Final Classifier used: `Random Forest Classifier`

2. **Regression:**
   
|        Model       |    MAE    |       RSME      |
|--------------------|-----------|-----------------|
|    Logistic Reg.   | 2.359     | 2.934           |
|        Ridge       | 1.737     | 2.075           |
|   Random Forest    | 1.672     | 2.022           |
|   Gradient Boost   | 1.687     | 2.015           |

- Final Regressor used: `Gradient Boosting Regressor`
---

## Web-Application
It is a Streamlit based interactive interface where users can submit the required text fields of a programming problem and can get a difficulty class and score on the basis of the textual data only. Predictions are made, based on the final ML models that performed best during experimental phase.

## Steps to run project locally
### 1. Clone the repository
```bash
git clone https://github.com/bean-bagg/AutoJugde.git
git clone 
cd AutoJudge
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Required dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Web Application
```bash
streamlit run app.py
```

### 5. Open the application in browser
```
http://localhost:8501
```
### 6. Use the application
- Enter the required input fields
- Predict Class difficulty and Score
---
## Author Details:
- Name: Parth Bansal
- Enrollment No.: 24112081

## Report and Demo Video
- Link to Drive: https://drive.google.com/drive/folders/1V1s9qtGAu-jhhYlyEIlU-s9u0FVv7vdD
