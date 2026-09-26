# Student Exam Score Prediction ML

## 1. Project Overview

This project aims to predict a student's final exam score using Machine Learning regression models.

The application uses information about the student's academic performance, personal profile, and school environment to estimate the final `Exam_Score`.

A Streamlit application was developed to allow users to enter a student's profile and obtain:

* The predicted exam score.
* A risk signal for students with a predicted score below 50.

---

## 2. Project Objectives

The main objectives of this project are:

* Analyze and prepare the student dataset.
* Handle missing values, duplicates, and outliers.
* Perform exploratory data analysis.
* Encode categorical variables.
* Split the dataset into training and testing sets.
* Scale numerical features.
* Train and compare regression models.
* Optimize model hyperparameters using `GridSearchCV`.
* Select and export the final model.
* Develop a Streamlit application for prediction.
* Ensure reproducibility of the project.

---

## 3. Dataset

The dataset contains information about students and their academic performance.

The initial dataset contains:

* 6,607 observations.
* 20 columns.

The target variable is:

```text
Exam_Score
```

### Main Features

Numerical features include:

* `Hours_Studied`
* `Attendance`
* `Sleep_Hours`
* `Previous_Scores`
* `Tutoring_Sessions`
* `Physical_Activity`

Categorical features include:

* `Gender`
* `School_Type`
* `Extracurricular_Activities`
* `Internet_Access`
* `Learning_Disabilities`
* `Peer_Influence`
* `Parental_Involvement`
* `Access_to_Resources`
* `Motivation_Level`
* `Family_Income`
* `Teacher_Quality`
* `Parental_Education_Level`
* `Distance_from_Home`

---

## 4. Machine Learning Workflow

The project follows these main steps:

```text
Data Understanding
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Categorical Encoding
        ↓
Train/Test Split
        ↓
Feature Scaling
        ↓
Model Training
        ↓
Hyperparameter Optimization
        ↓
Model Evaluation
        ↓
Final Pipeline
        ↓
Streamlit Application
```

---

## 5. Data Cleaning

The following preprocessing operations were performed:

### Missing Values

Missing values were found in:

* `Teacher_Quality`
* `Parental_Education_Level`
* `Distance_from_Home`

The missing categorical values were replaced using the mode of each column.

### Duplicates

Duplicate rows were checked and removed when present.

### Outliers

Outliers in `Exam_Score` were analyzed using:

* Boxplot.
* IQR method.
* Z-score method.

The IQR method was used for the final outlier removal.

The resulting dataset contained:

```text
6,503 observations
```

---

## 6. Feature Engineering and Encoding

Two encoding strategies were used.

### Nominal Encoding

The following nominal variables were encoded using `OneHotEncoder`:

* `Gender`
* `School_Type`
* `Extracurricular_Activities`
* `Internet_Access`
* `Learning_Disabilities`
* `Peer_Influence`

`drop="first"` was used to avoid redundant dummy variables.

### Ordinal Encoding

The following ordinal variables were encoded using `OrdinalEncoder`:

* `Parental_Involvement`
* `Access_to_Resources`
* `Motivation_Level`
* `Family_Income`
* `Teacher_Quality`
* `Parental_Education_Level`
* `Distance_from_Home`

The category order was explicitly defined according to the meaning of each variable.

---

## 7. Train/Test Split

The dataset was divided into:

* 80% training data.
* 20% testing data.

The split used:

```text
random_state = 42
```

Final shapes:

```text
X_train: 5202 × 20
X_test: 1301 × 20
```

---

## 8. Feature Scaling

`StandardScaler` was applied to the numerical variables:

* `Hours_Studied`
* `Attendance`
* `Sleep_Hours`
* `Previous_Scores`
* `Tutoring_Sessions`
* `Physical_Activity`

Categorical encoded variables were not standardized.

---

## 9. Models Tested

Three regression algorithms were evaluated:

### Linear Regression

`LinearRegression`

### Random Forest

`RandomForestRegressor`

### Support Vector Regression

`SVR`

---

## 10. Initial Model Evaluation

The initial models produced the following results:

| Model             |     RMSE |      MAE |       R² |
| ----------------- | -------: | -------: | -------: |
| Linear Regression | 0.327058 | 0.271589 | 0.989723 |
| Random Forest     | 1.067775 | 0.846879 | 0.890455 |
| SVR               | 0.456399 | 0.357219 | 0.979987 |

---

## 11. Hyperparameter Optimization

`GridSearchCV` with 3-fold cross-validation was used to optimize the models.

The cross-validation strategy used:

```text
KFold
n_splits = 3
shuffle = True
random_state = 42
```

### Optimized Linear Regression

```text
fit_intercept = True
positive = False
```

### Optimized Random Forest

```text
n_estimators = 200
max_depth = None
min_samples_split = 2
```

### Optimized SVR

```text
C = 10
kernel = linear
epsilon = 0.2
```

---

## 12. Optimized Model Evaluation

After hyperparameter optimization:

| Model             |     RMSE |      MAE |       R² |
| ----------------- | -------: | -------: | -------: |
| Linear Regression | 0.327058 | 0.271589 | 0.989723 |
| Random Forest     | 1.064144 | 0.845734 | 0.891199 |
| SVR               | 0.327814 | 0.272224 | 0.989675 |

The final model used in the application is the optimized Linear Regression model.

---

## 13. Final Pipeline

A complete Scikit-learn `Pipeline` was created containing:

```text
Raw Student Data
       ↓
ColumnTransformer
       ↓
StandardScaler
OrdinalEncoder
OneHotEncoder
       ↓
LinearRegression
       ↓
Prediction
```

The pipeline was exported using `joblib`:

```text
models/student_exam_score_pipeline.pkl
```

The pipeline was trained using:

```text
scikit-learn 1.6.1
```

Using the same compatible version when loading the model is important for reproducibility.

---

## 14. Streamlit Application

The Streamlit application allows the user to enter the student's profile using:

* Number inputs for numerical variables.
* Select boxes for categorical variables.

The application then:

1. Collects the student's information.
2. Creates a DataFrame with the original feature names.
3. Sends the data to the exported pipeline.
4. Applies the same preprocessing used during training.
5. Predicts the exam score.
6. Displays the predicted score.
7. Displays a risk signal.

### Risk Signal

For the application, a predicted score below `50` is considered a risk signal:

```text
Predicted Score < 50
        ↓
Student at risk
```

Otherwise:

```text
Predicted Score >= 50
        ↓
Student not at risk
```

This threshold is an application-level choice because the project specification does not provide an official risk threshold.

---

## 15. Input Validation

The Streamlit application uses input constraints to prevent invalid values.

Examples:

```text
Hours Studied: 0–24
Attendance: 0–100
Sleep Hours: 0–24
Previous Scores: 0–100
Tutoring Sessions: 0–10
Physical Activity: 0–10
```

Categorical variables are controlled using predefined selection lists.

---

## 16. Project Structure

```text
Student-Exam-Score-Prediction-ML/
│
├── app/
│   └── app.py
│
├── data/
│   └── raw/
│       └── dataset.csv
│
├── models/
│   └── student_exam_score_pipeline.pkl
│
├── notebooks/
│   └── student_exam_score_prediction.ipynb
│
├── README.md
├── requirements.txt
├── pyproject.toml
└── uv.lock
```

---

## 17. Technologies

The project uses:

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* Jupyter / Google Colab
* uv
* Git / GitHub
* Jira

Main versions:

```text
scikit-learn = 1.6.1
joblib = 1.6.0
streamlit = 1.64.0
```

---

## 18. Installation

Clone the repository:

```bash
git clone <https://github.com/ISMAILBENMEZI/Student-Exam-Score-Prediction-ML.git>
```

Navigate to the project:

```bash
cd Student-Exam-Score-Prediction-ML
```

Install dependencies:

```bash
uv sync
```

---

## 19. Run the Streamlit Application

Run:

```bash
uv run streamlit run app/app.py
```

The application will be available locally through the URL displayed by Streamlit.

---

## 20. Reproducibility

To reproduce the project:

1. Use the provided dataset.
2. Open the Jupyter notebook.
3. Follow the documented preprocessing steps.
4. Train the models.
5. Run the GridSearchCV optimization.
6. Evaluate the optimized models.
7. Export the final pipeline with `joblib`.
8. Use the exported pipeline in the Streamlit application.

The project uses fixed random states where applicable to make the experiments reproducible.

---

## 21. Author

**Ismail Benmezi**

Full Stack Developer / AI Development Student

YouCode – UM6P
