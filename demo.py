# # # -*- coding: utf-8 -*-
# # """
# # Created on Thu Apr 17 19:36:17 2025
# # @author: jhans
# # """

# # import os
# # import pickle
# # import streamlit as st
# # from streamlit_option_menu import option_menu

# # # Set page configuration
# # st.set_page_config(
# #     page_title="Health Assistant",
# #     layout="wide",
# #     page_icon="🧑‍⚕️"
# # )

# # # Get the working directory of this file
# # working_dir = os.path.dirname(os.path.abspath(__file__))

# # # Define model paths
# # diabetes_model_path = os.path.join(working_dir, 'sav_file', 'diabetes_model.sav')
# # heart_model_path = os.path.join(working_dir, 'sav_file', 'heart_disease_model.sav')
# # parkinsons_model_path = os.path.join(working_dir, 'sav_file', 'parkinsons_model.sav')

# # # Load models with error handling
# # try:
# #     diabetes_model = pickle.load(open(diabetes_model_path, 'rb'))
# #     heart_disease_model = pickle.load(open(heart_model_path, 'rb'))
# #     parkinsons_model = pickle.load(open(parkinsons_model_path, 'rb'))
# # except FileNotFoundError as e:
# #     st.error(f"Model file not found: {e}")
# #     st.stop()

# # # Sidebar menu
# # with st.sidebar:
# #     selected = option_menu(
# #         'Multiple Disease Prediction System',
# #         ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
# #         menu_icon='hospital-fill',
# #         icons=['activity', 'heart', 'person'],
# #         default_index=0
# #     )

# # # ---------------- Diabetes Prediction ----------------
# # if selected == 'Diabetes Prediction':
# #     st.title('Diabetes Prediction using ML')

# #     col1, col2, col3 = st.columns(3)

# #     with col1:
# #         Pregnancies = st.text_input('Number of Pregnancies')
# #     with col2:
# #         Glucose = st.text_input('Glucose Level')
# #     with col3:
# #         BloodPressure = st.text_input('Blood Pressure value')
# #     with col1:
# #         SkinThickness = st.text_input('Skin Thickness value')
# #     with col2:
# #         Insulin = st.text_input('Insulin Level')
# #     with col3:
# #         BMI = st.text_input('BMI value')
# #     with col1:
# #         DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
# #     with col2:
# #         Age = st.text_input('Age of the Person')

# #     diab_diagnosis = ''

# #     if st.button('Diabetes Test Result'):
# #         try:
# #             user_input = [float(x) for x in [
# #                 Pregnancies, Glucose, BloodPressure, SkinThickness,
# #                 Insulin, BMI, DiabetesPedigreeFunction, Age
# #             ]]
# #             prediction = diabetes_model.predict([user_input])[0]
# #             diab_diagnosis = 'The person is diabetic' if prediction == 1 else 'The person is not diabetic'
# #         except ValueError:
# #             st.error("Please enter valid numeric values for all fields.")

# #     st.success(diab_diagnosis)

# # # ---------------- Heart Disease Prediction ----------------
# # if selected == 'Heart Disease Prediction':
# #     st.title('Heart Disease Prediction using ML')

# #     col1, col2, col3 = st.columns(3)
# #     with col1:
# #         age = st.text_input('Age')
# #     with col2:
# #         sex = st.text_input('Sex')
# #     with col3:
# #         cp = st.text_input('Chest Pain types')
# #     with col1:
# #         trestbps = st.text_input('Resting Blood Pressure')
# #     with col2:
# #         chol = st.text_input('Serum Cholestoral in mg/dl')
# #     with col3:
# #         fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
# #     with col1:
# #         restecg = st.text_input('Resting Electrocardiographic results')
# #     with col2:
# #         thalach = st.text_input('Maximum Heart Rate achieved')
# #     with col3:
# #         exang = st.text_input('Exercise Induced Angina')
# #     with col1:
# #         oldpeak = st.text_input('ST depression induced by exercise')
# #     with col2:
# #         slope = st.text_input('Slope of the peak exercise ST segment')
# #     with col3:
# #         ca = st.text_input('Major vessels colored by flourosopy')
# #     with col1:
# #         thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

# #     heart_diagnosis = ''

# #     if st.button('Heart Disease Test Result'):
# #         try:
# #             user_input = [float(x) for x in [
# #                 age, sex, cp, trestbps, chol, fbs, restecg,
# #                 thalach, exang, oldpeak, slope, ca, thal
# #             ]]
# #             prediction = heart_disease_model.predict([user_input])[0]
# #             heart_diagnosis = 'The person is having heart disease' if prediction == 1 else 'The person does not have any heart disease'
# #         except ValueError:
# #             st.error("Please enter valid numeric values for all fields.")

# #     st.success(heart_diagnosis)

# # # ---------------- Parkinson's Prediction ----------------
# # if selected == "Parkinsons Prediction":
# #     st.title("Parkinson's Disease Prediction using ML")

# #     fields = [
# #         'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
# #         'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
# #         'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR',
# #         'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
# #     ]

# #     inputs = []
# #     cols = st.columns(5)
# #     for i, field in enumerate(fields):
# #         col = cols[i % 5]
# #         inputs.append(col.text_input(field))

# #     parkinsons_diagnosis = ''

# #     if st.button("Parkinson's Test Result"):
# #         try:
# #             user_input = [float(x) for x in inputs]
# #             prediction = parkinsons_model.predict([user_input])[0]
# #             parkinsons_diagnosis = "The person has Parkinson's disease" if prediction == 1 else "The person does not have Parkinson's disease"
# #         except ValueError:
# #             st.error("Please enter valid numeric values for all fields.")

# #     st.success(parkinsons_diagnosis)





# # -*- coding: utf-8 -*-
# """
# Created on Thu Apr 17 19:36:17 2025
# @author: jhans
# """

# import os
# import pickle
# import streamlit as st
# from streamlit_option_menu import option_menu

# # Set page configuration
# st.set_page_config(
#     page_title="Health Assistant",
#     layout="wide",
#     page_icon="🧑‍⚕️"
# )

# # Use current working directory
# working_dir = os.getcwd()

# # Define model paths
# diabetes_model_path = os.path.join(working_dir, 'sav_file', 'diabetes_model.sav')
# heart_model_path = os.path.join(working_dir, 'sav_file', 'heart_disease_model.sav')
# parkinsons_model_path = os.path.join(working_dir, 'sav_file', 'parkinsons_model.sav')

# # Load models with error handling
# try:
#     diabetes_model = pickle.load(open(diabetes_model_path, 'rb'))
#     heart_disease_model = pickle.load(open(heart_model_path, 'rb'))
#     parkinsons_model = pickle.load(open(parkinsons_model_path, 'rb'))
# except FileNotFoundError as e:
#     st.error(f"Model file not found: {e}")
#     st.stop()

# # Sidebar menu
# with st.sidebar:
#     selected = option_menu(
#         'Multiple Disease Prediction System',
#         ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
#         menu_icon='hospital-fill',
#         icons=['activity', 'heart', 'person'],
#         default_index=0
#     )

# # ---------------- Diabetes Prediction ----------------
# if selected == 'Diabetes Prediction':
#     st.title('Diabetes Prediction using ML')

#     col1, col2, col3 = st.columns(3)

#     with col1:
#         Pregnancies = st.text_input('Number of Pregnancies')
#     with col2:
#         Glucose = st.text_input('Glucose Level')
#     with col3:
#         BloodPressure = st.text_input('Blood Pressure value')
#     with col1:
#         SkinThickness = st.text_input('Skin Thickness value')
#     with col2:
#         Insulin = st.text_input('Insulin Level')
#     with col3:
#         BMI = st.text_input('BMI value')
#     with col1:
#         DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
#     with col2:
#         Age = st.text_input('Age of the Person')

#     diab_diagnosis = ''

#     if st.button('Diabetes Test Result'):
#         try:
#             user_input = [float(x) for x in [
#                 Pregnancies, Glucose, BloodPressure, SkinThickness,
#                 Insulin, BMI, DiabetesPedigreeFunction, Age
#             ]]
#             prediction = diabetes_model.predict([user_input])[0]
#             diab_diagnosis = 'The person is diabetic' if prediction == 1 else 'The person is not diabetic'
#         except ValueError:
#             st.error("Please enter valid numeric values for all fields.")

#     st.success(diab_diagnosis)

# # ---------------- Heart Disease Prediction ----------------
# if selected == 'Heart Disease Prediction':
#     st.title('Heart Disease Prediction using ML')

#     col1, col2, col3 = st.columns(3)
#     with col1:
#         age = st.text_input('Age')
#     with col2:
#         sex = st.text_input('Sex')
#     with col3:
#         cp = st.text_input('Chest Pain types')
#     with col1:
#         trestbps = st.text_input('Resting Blood Pressure')
#     with col2:
#         chol = st.text_input('Serum Cholesterol in mg/dl')
#     with col3:
#         fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
#     with col1:
#         restecg = st.text_input('Resting Electrocardiographic results')
#     with col2:
#         thalach = st.text_input('Maximum Heart Rate achieved')
#     with col3:
#         exang = st.text_input('Exercise Induced Angina')
#     with col1:
#         oldpeak = st.text_input('ST depression induced by exercise')
#     with col2:
#         slope = st.text_input('Slope of the peak exercise ST segment')
#     with col3:
#         ca = st.text_input('Major vessels colored by fluoroscopy')
#     with col1:
#         thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

#     heart_diagnosis = ''

#     if st.button('Heart Disease Test Result'):
#         try:
#             user_input = [float(x) for x in [
#                 age, sex, cp, trestbps, chol, fbs, restecg,
#                 thalach, exang, oldpeak, slope, ca, thal
#             ]]
#             prediction = heart_disease_model.predict([user_input])[0]
#             heart_diagnosis = 'The person is having heart disease' if prediction == 1 else 'The person does not have any heart disease'
#         except ValueError:
#             st.error("Please enter valid numeric values for all fields.")

#     st.success(heart_diagnosis)

# # ---------------- Parkinson's Prediction ----------------
# if selected == "Parkinsons Prediction":
#     st.title("Parkinson's Disease Prediction using ML")

#     fields = [
#         'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
#         'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
#         'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR',
#         'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
#     ]

#     inputs = []
#     cols = st.columns(5)
#     for i, field in enumerate(fields):
#         col = cols[i % 5]
#         inputs.append(col.text_input(field))

#     parkinsons_diagnosis = ''

#     if st.button("Parkinson's Test Result"):
#         try:
#             user_input = [float(x) for x in inputs]
#             prediction = parkinsons_model.predict([user_input])[0]
#             parkinsons_diagnosis = "The person has Parkinson's disease" if prediction == 1 else "The person does not have Parkinson's disease"
#         except ValueError:
#             st.error("Please enter valid numeric values for all fields.")

#     st.success(parkinsons_diagnosis)
st.write(f"Diabetes model path: {diabetes_model_path}")
if os.path.exists(os.path.dirname(diabetes_model_path)):
    st.write("Directory exists.")
else:
    st.write("Directory does not exist.")
import logging

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler
file_handler = logging.FileHandler('health_assistant.log')
file_handler.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# ...

# Log messages
logger.info(f"Diabetes model path: {diabetes_model_path}")
if os.path.exists(os.path.dirname(diabetes_model_path)):
    logger.info("Directory exists.")
else:
    logger.info("Directory does not exist.")