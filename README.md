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
- Raw data in .jsonl format converted to .csv format
- Analyzing the data before use, includes:
    - Class-wise no. of problems
    - 
- Cleaning and normalizing problem statements  
- Encoding categorical features  
- Handling missing or inconsistent values  

### Feature Extraction
- Text-based features (e.g., TF-IDF, embeddings)  
- Numerical features (e.g., number of constraints, test cases)  

### Models
1. **Classification Model**  
   - Predicts difficulty category: Easy / Medium / Hard  
   - Algorithm: *(e.g., Random Forest / XGBoost / SVM)*  

2. **Regression Model**  
   - Predicts continuous difficulty score  
   - Algorithm: *(e.g., Random Forest Regressor / Linear Regression)*  

---

## Evaluation Metrics
- **Classification:** Accuracy  
- **Regression:** Mean Absolute Error (MAE), Root Mean Squared Error (RMSE)  

> Add your actual metric values here.

---

## Steps to Run the Project Locally

1. Clone the repository:  
   ```bash
   git clone <repo-link>
   cd AutoJudge
