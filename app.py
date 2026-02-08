import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

breast_cancer_model = pickle.load(open(f'{working_dir}/saved_models/breast_cancer_model.sav', 'rb'))

maternal_health_model = pickle.load(open(f'{working_dir}/saved_models/maternal_health_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction',
                            'Maternal Health Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person', 'gender-female', 'person-check'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        if all(user_input):
            user_input = [float(x) for x in user_input]
            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
            st.success(diab_diagnosis)
        else:
            st.error("Please fill in all the fields")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        if all(user_input):
            user_input = [float(x) for x in user_input]
            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
            st.success(heart_diagnosis)
        else:
            st.error("Please fill in all the fields")

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        if all(user_input):
            user_input = [float(x) for x in user_input]
            parkinsons_prediction = parkinsons_model.predict([user_input])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
            st.success(parkinsons_diagnosis)
        else:
            st.error("Please fill in all the fields")


# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':

    # page title
    st.title('Breast Cancer Prediction using ML')

    # getting the input data from the user
    # Split into 5 columns for 30 features
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        mean_radius = st.text_input('Mean Radius')
    with col2:
        mean_texture = st.text_input('Mean Texture')
    with col3:
        mean_perimeter = st.text_input('Mean Perimeter')
    with col4:
        mean_area = st.text_input('Mean Area')
    with col5:
        mean_smoothness = st.text_input('Mean Smoothness')

    with col1:
        mean_compactness = st.text_input('Mean Compactness')
    with col2:
        mean_concavity = st.text_input('Mean Concavity')
    with col3:
        mean_concave_points = st.text_input('Mean Concave Points')
    with col4:
        mean_symmetry = st.text_input('Mean Symmetry')
    with col5:
        mean_fractal_dimension = st.text_input('Mean Fractal Dimension')

    with col1:
        radius_error = st.text_input('Radius Error')
    with col2:
        texture_error = st.text_input('Texture Error')
    with col3:
        perimeter_error = st.text_input('Perimeter Error')
    with col4:
        area_error = st.text_input('Area Error')
    with col5:
        smoothness_error = st.text_input('Smoothness Error')

    with col1:
        compactness_error = st.text_input('Compactness Error')
    with col2:
        concavity_error = st.text_input('Concavity Error')
    with col3:
        concave_points_error = st.text_input('Concave Points Error')
    with col4:
        symmetry_error = st.text_input('Symmetry Error')
    with col5:
        fractal_dimension_error = st.text_input('Fractal Dimension Error')

    with col1:
        worst_radius = st.text_input('Worst Radius')
    with col2:
        worst_texture = st.text_input('Worst Texture')
    with col3:
        worst_perimeter = st.text_input('Worst Perimeter')
    with col4:
        worst_area = st.text_input('Worst Area')
    with col5:
        worst_smoothness = st.text_input('Worst Smoothness')

    with col1:
        worst_compactness = st.text_input('Worst Compactness')
    with col2:
        worst_concavity = st.text_input('Worst Concavity')
    with col3:
        worst_concave_points = st.text_input('Worst Concave Points')
    with col4:
        worst_symmetry = st.text_input('Worst Symmetry')
    with col5:
        worst_fractal_dimension = st.text_input('Worst Fractal Dimension')

    # code for Prediction
    bc_diagnosis = ''

    # creating a button for Prediction
    if st.button('Breast Cancer Test Result'):
        user_input = [mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness,
                      mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension,
                      radius_error, texture_error, perimeter_error, area_error, smoothness_error,
                      compactness_error, concavity_error, concave_points_error, symmetry_error, fractal_dimension_error,
                      worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness,
                      worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension]

        if all(user_input):
            user_input = [float(x) for x in user_input]
            bc_prediction = breast_cancer_model.predict([user_input])

            if bc_prediction[0] == 0:
                bc_diagnosis = 'The breast cancer is Malignant'
            else:
                bc_diagnosis = 'The breast cancer is Benign'
            st.success(bc_diagnosis)
        else:
            st.error("Please fill in all the fields")


# Maternal Health Prediction Page
if selected == 'Maternal Health Prediction':

    # page title
    st.title('Maternal Health Risk Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        systolic_bp = st.text_input('Systolic BP')
    with col3:
        diastolic_bp = st.text_input('Diastolic BP')
    with col1:
        bs = st.text_input('Blood Sugar')
    with col2:
        body_temp = st.text_input('Body Temperature')
    with col3:
        heart_rate = st.text_input('Heart Rate')

    # code for Prediction
    maternal_diagnosis = ''

    # creating a button for Prediction
    if st.button('Maternal Health Test Result'):
        user_input = [age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate]
        
        if all(user_input):
            user_input = [float(x) for x in user_input]

            # The model returns 'high risk', 'low risk', 'mid risk'
            maternal_prediction = maternal_health_model.predict([user_input])
            
            maternal_diagnosis = f'The predicted risk level is: {maternal_prediction[0]}'
            st.success(maternal_diagnosis)
        else:
            st.error("Please fill in all the fields")
