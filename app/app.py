import streamlit as st
import joblib
import pandas as pd

model = joblib.load("models/student_exam_score_pipeline.pkl")

st.title("Student Exam Score Prediction")
st.write("Predict a student's exam score using a machine learning model.")
st.header("Academic Information")

col1, col2 = st.columns(2)

with col1:
    hours_studied = st.number_input("Hours Studied", min_value=0, max_value=24, value=5)

    attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, value=75)

    previous_scores = st.number_input(
        "Previous Scores", min_value=0, max_value=100, value=70
    )

    tutoring_sessions = st.number_input(
        "Tutoring Sessions", min_value=0, max_value=10, value=2
    )

with col2:
    sleep_hours = st.number_input("Sleep Hours", min_value=0, max_value=24, value=7)

    physical_activity = st.number_input(
        "Physical Activity", min_value=0, max_value=10, value=5
    )

st.header("Student Profile")

col1, col2 = st.columns(2)

with col1:
    parental_involvement = st.selectbox(
        "Parental Involvement", ["Low", "Medium", "High"]
    )

    motivation_level = st.selectbox("Motivation Level", ["Low", "Medium", "High"])

    learning_disabilities = st.selectbox("Learning Disabilities", ["No", "Yes"])

    gender = st.selectbox("Gender", ["Female", "Male"])

with col2:
    access_to_resources = st.selectbox("Access to Resources", ["Low", "Medium", "High"])

    family_income = st.selectbox("Family Income", ["Low", "Medium", "High"])

    parental_education_level = st.selectbox(
        "Parental Education Level", ["High School", "College", "Postgraduate"]
    )

    distance_from_home = st.selectbox("Distance From Home", ["Near", "Moderate", "Far"])

st.header("School Environment")

col1, col2 = st.columns(2)

with col1:
    school_type = st.selectbox("School Type", ["Public", "Private"])

    teacher_quality = st.selectbox("Teacher Quality", ["Low", "Medium", "High"])

    internet_access = st.selectbox("Internet Access", ["No", "Yes"])

with col2:
    extracurricular_activities = st.selectbox(
        "Extracurricular Activities", ["No", "Yes"]
    )

    peer_influence = st.selectbox("Peer Influence", ["Negative", "Neutral", "Positive"])


input_data = pd.DataFrame(
    {
        "Hours_Studied": [hours_studied],
        "Attendance": [attendance],
        "Parental_Involvement": [parental_involvement],
        "Access_to_Resources": [access_to_resources],
        "Extracurricular_Activities": [extracurricular_activities],
        "Sleep_Hours": [sleep_hours],
        "Previous_Scores": [previous_scores],
        "Motivation_Level": [motivation_level],
        "Internet_Access": [internet_access],
        "Tutoring_Sessions": [tutoring_sessions],
        "Family_Income": [family_income],
        "Teacher_Quality": [teacher_quality],
        "School_Type": [school_type],
        "Peer_Influence": [peer_influence],
        "Physical_Activity": [physical_activity],
        "Learning_Disabilities": [learning_disabilities],
        "Parental_Education_Level": [parental_education_level],
        "Distance_from_Home": [distance_from_home],
        "Gender": [gender],
    }
)


if st.button("Predict Exam Score"):
    prediction = model.predict(input_data)
    predicted_score = prediction[0]
    st.success(f"Predicted Exam Score: {prediction[0]:.2f}")

    if predicted_score < 50:
        st.warning("Student at risk")
    else:
        st.success("Student not at risk")
