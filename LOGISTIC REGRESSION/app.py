import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("titanic_model.pkl", "rb"))

st.title("Titanic Survival Prediction App 🚢")

st.write("Enter passenger details below:")

# Inputs
pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["Male", "Female"])
age = st.slider("Age", 1, 80, 25)
sibsp = st.number_input("Number of Siblings/Spouses", 0, 8, 0)
parch = st.number_input("Number of Parents/Children", 0, 6, 0)
fare = st.number_input("Fare", 0.0, 600.0, 50.0)
embarked = st.selectbox("Embarked", ["Q", "S"])

# Convert categorical variables
sex = 1 if sex == "Male" else 0
embarked_Q = 1 if embarked == "Q" else 0
embarked_S = 1 if embarked == "S" else 0

if st.button("Predict"):
    input_data = np.array([[pclass, sex, age, sibsp, parch, fare, embarked_Q, embarked_S]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Survived ✅")
    else:
        st.error("Did Not Survive ❌")