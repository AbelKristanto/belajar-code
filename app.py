# library heart disease prediction
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time
from PIL import Image

# Load the trained model
model_heart = pickle.load(open('hasilgenerate.pkl', 'rb'))

# Configure the Streamlit app
st.set_page_config(page_title="Health Prediction App", page_icon="❤️", layout="centered")

# Function heart disease prediction
def predict_heart_disease():
    st.title("Heart Disease Prediction")
    st.write("""         
    This app predicts the likelihood of heart disease based on various health parameters. Please fill in the details below to get your prediction.
    Data obtained from the UCI Machine Learning Repository: [Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease).
    """)
    st.image("heart-disease.jpg", caption="Heart Disease Prediction", use_container_width=True)
    # Input fields for user data
    st.sidebar.header("Input Parameters")
    st.sidebar.markdown("""Please enter the following health parameters to predict the likelihood of heart disease:
    - Age: Age of the patient (years)
    - Sex: Gender of the patient (1 = male, 0 = female)
                        etc...
    """)
    cp = st.sidebar.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
    if cp == 0:
        st.sidebar.write("Typical Angina")
    elif cp == 1:
        st.sidebar.write("Atypical Angina")
    elif cp == 2:
        st.sidebar.write("Non-Anginal Pain")
    elif cp == 3:
        st.sidebar.write("Asymptomatic")
    # 'cp', 'thalach', 'slope', 'oldpeak', 'exang', 'ca', 'thal', 'sex', dan 'age'
    thalach = st.sidebar.slider("Maximum Heart Rate Achieved (thalach)", 60, 220, 150)
    slope = st.sidebar.selectbox("Slope of the Peak Exercise ST Segment (slope)", [0, 1, 2])
    if slope == 0:
        st.sidebar.write("Upsloping")
    elif slope == 1:
        st.sidebar.write("Flat")
    elif slope == 2:
        st.sidebar.write("Downsloping")
    oldpeak = st.sidebar.slider("ST Depression Induced by Exercise Relative to Rest (oldpeak)", 0.0, 6.0, 1.0)
    exang = st.sidebar.selectbox("Exercise Induced Angina (exang)", [0, 1])
    if exang == 0:
        st.sidebar.write("No")
    elif exang == 1:
        st.sidebar.write("Yes")
    ca = st.sidebar.selectbox("Number of Major Vessels Colored by Fluoroscopy (ca)", [0, 1, 2, 3])
    if ca == 0:
        st.sidebar.write("0")
    elif ca == 1:
        st.sidebar.write("1")
    elif ca == 2:
        st.sidebar.write("2")
    elif ca == 3:
        st.sidebar.write("3")
    thal = st.sidebar.selectbox("Thalassemia (thal)", [0, 1, 2, 3])
    if thal == 0:
        st.sidebar.write("Normal")
    elif thal == 1:
        st.sidebar.write("Fixed Defect")
    elif thal == 2:
        st.sidebar.write("Reversible Defect")
    elif thal == 3:
        st.sidebar.write("Unknown")
    sex = st.sidebar.selectbox("Sex (sex)", [0, 1])
    if sex == 0:
        st.sidebar.write("Female")
    elif sex == 1:
        st.sidebar.write("Male")
    age = st.sidebar.slider("Age (age)", 20, 100, 50)
    # Create a DataFrame for the input data
    data = {
        'cp': cp,
        'thalach': thalach,
        'slope': slope,
        'oldpeak': oldpeak,
        'exang': exang,
        'ca': ca,
        'thal': thal,
        'sex': sex,
        'age': age
    }
    input_data = pd.DataFrame([data])
    st.write(input_data)
    # Predict the likelihood of heart disease
    if st.sidebar.button("Predict"):
        with st.spinner("Predicting..."):
            time.sleep(2)  # Simulate a delay for prediction
            prediction = model_heart.predict(input_data)
            if prediction[0] == 1:
                st.snow()
                st.error("The model predicts that you are likely to have heart disease. Please consult a healthcare professional for further evaluation.")
            else:
                st.balloons()
                st.success("The model predicts that you are unlikely to have heart disease. However, please maintain a healthy lifestyle and consult a healthcare professional for regular check-ups.")

# function about iris-dataset
def about_iris():
    st.title("About the Iris Dataset")
    st.write("""
    The Iris dataset is a classic dataset in the field of machine learning and statistics. It was introduced by the British statistician and biologist Ronald A. Fisher in 1936. The dataset consists of 150 samples of iris flowers, with 50 samples from each of three different species: Iris setosa, Iris versicolor, and Iris virginica.
    Each sample in the dataset has four features: sepal length, sepal width, petal length, and petal width. These features are used to classify the iris flowers into their respective species. The dataset is widely used for testing and demonstrating various machine learning algorithms, particularly in classification tasks.
    The simplicity and well-defined nature of the Iris dataset make it an excellent choice for beginners to learn about data analysis, visualization, and machine learning techniques.
             """)

# function about section
def about():
    st.title("About This App")
    st.write("""
    This Health Prediction App is designed to provide insights into the likelihood of heart disease based on user-inputted health parameters. The app utilizes a machine learning model trained on the UCI Heart Disease Dataset to make predictions. 
    The dataset includes various features such as age, sex, chest pain type, maximum heart rate achieved, and more. The model was trained using a Random Forest Classifier, which is known for its accuracy and robustness in classification tasks.
    The app is built using Streamlit, a powerful framework for creating interactive web applications in Python. It allows users to easily input their health data and receive predictions in real-time.
    Please note that this app is for educational purposes only and should not be used as a substitute for professional medical advice. Always consult with a healthcare provider for any health-related concerns.
    #### Disclaimer: The predictions made by this app are based on a machine learning model and may not be 100% accurate. Always seek professional medical advice for any health concerns.
    #### Credits: This app was developed by [Your Name] using the UCI Heart Disease Dataset and various Python libraries including Streamlit, Pandas, NumPy, and Scikit-learn.
             """)

# introduce developer
def developer():
    st.title("Meet the Developer")
    st.write("""
    Hello! I'm [Your Name], a passionate data scientist and machine learning enthusiast. I developed this Health Prediction App to help individuals gain insights into their health based on various parameters. 
    With a background in data science and a keen interest in healthcare, I aim to create tools that can assist people in making informed decisions about their health. 
    In my free time, I enjoy exploring new datasets, building machine learning models, and sharing my knowledge with the community. 
    If you have any questions or feedback about the app, feel free to reach out to me at [Your Email] or connect with me on LinkedIn at [Your LinkedIn Profile].
    Thank you for using the Health Prediction App!
             """)
        
# Main function to run the app
def main():
    st.sidebar.title("Navigation")
    options = ["Heart Disease Prediction", "About the Iris Dataset", "About", "Developer"]
    choice = st.sidebar.selectbox("Select an option", options)
    if choice == "Heart Disease Prediction":
        predict_heart_disease()
    elif choice == "About the Iris Dataset":
        about_iris()
    elif choice == "About":
        about()
    elif choice == "Developer":
        developer()

if __name__ == "__main__":
    main()