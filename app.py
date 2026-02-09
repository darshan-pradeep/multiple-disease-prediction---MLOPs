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
        Pregnancies = st.number_input('Number of Pregnancies (0-20)', min_value=0, max_value=20, value=0)

    with col2:
        Glucose = st.number_input('Glucose Level (0-200)', min_value=0, max_value=200, value=0)

    with col3:
        BloodPressure = st.number_input('Blood Pressure value (0-130)', min_value=0, max_value=130, value=0)

    with col1:
        SkinThickness = st.number_input('Skin Thickness value (0-100)', min_value=0, max_value=100, value=0)

    with col2:
        Insulin = st.number_input('Insulin Level (0-900)', min_value=0, max_value=900, value=0)

    with col3:
        BMI = st.number_input('BMI value (0-70)', min_value=0.0, max_value=70.0, value=0.0)

    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value (0.0-2.5)', min_value=0.0, max_value=2.5, value=0.0, format="%.3f")

    with col2:
        Age = st.number_input('Age of the Person (0-100)', min_value=0, max_value=100, value=0)


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
        st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age (0-100)', min_value=0, max_value=100, value=0)

    with col2:
        sex = st.number_input('Sex (0 = female; 1 = male)', min_value=0, max_value=1, value=0)

    with col3:
        cp = st.number_input('Chest Pain types (0-3)', min_value=0, max_value=3, value=0)

    with col1:
        trestbps = st.number_input('Resting Blood Pressure (80-220)', min_value=80, max_value=220, value=80)

    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl (100-600)', min_value=100, max_value=600, value=100)

    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (0 = False; 1 = True)', min_value=0, max_value=1, value=0)

    with col1:
        restecg = st.number_input('Resting Electrocardiographic results (0-2)', min_value=0, max_value=2, value=0)

    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved (60-220)', min_value=60, max_value=220, value=60)

    with col3:
        exang = st.number_input('Exercise Induced Angina (0 = No; 1 = Yes)', min_value=0, max_value=1, value=0)

    with col1:
        oldpeak = st.number_input('ST depression induced by exercise (0.0-7.0)', min_value=0.0, max_value=7.0, value=0.0)

    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment (0-2)', min_value=0, max_value=2, value=0)

    with col3:
        ca = st.number_input('Major vessels colored by flourosopy (0-4)', min_value=0, max_value=4, value=0)

    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', min_value=0, max_value=2, value=0)

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
        st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input('MDVP:Fo (Hz) (80-270)', min_value=80.0, max_value=270.0, value=80.0)

    with col2:
        fhi = st.number_input('MDVP:Fhi (Hz) (100-600)', min_value=100.0, max_value=600.0, value=100.0)

    with col3:
        flo = st.number_input('MDVP:Flo (Hz) (60-250)', min_value=60.0, max_value=250.0, value=60.0)

    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter (%) (0.0-0.05)', min_value=0.0, max_value=0.05, value=0.0, format="%.5f")

    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter (Abs) (0.0-0.0003)', min_value=0.0, max_value=0.0003, value=0.0, format="%.6f")

    with col1:
        RAP = st.number_input('MDVP:RAP (0.0-0.03)', min_value=0.0, max_value=0.03, value=0.0, format="%.5f")

    with col2:
        PPQ = st.number_input('MDVP:PPQ (0.0-0.02)', min_value=0.0, max_value=0.02, value=0.0, format="%.5f")

    with col3:
        DDP = st.number_input('Jitter:DDP (0.0-0.07)', min_value=0.0, max_value=0.07, value=0.0, format="%.5f")

    with col4:
        Shimmer = st.number_input('MDVP:Shimmer (0.0-0.15)', min_value=0.0, max_value=0.15, value=0.0, format="%.5f")

    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer (dB) (0.0-1.5)', min_value=0.0, max_value=1.5, value=0.0, format="%.3f")

    with col1:
        APQ3 = st.number_input('Shimmer:APQ3 (0.0-0.06)', min_value=0.0, max_value=0.06, value=0.0, format="%.5f")

    with col2:
        APQ5 = st.number_input('Shimmer:APQ5 (0.0-0.08)', min_value=0.0, max_value=0.08, value=0.0, format="%.5f")

    with col3:
        APQ = st.number_input('MDVP:APQ (0.0-0.15)', min_value=0.0, max_value=0.15, value=0.0, format="%.5f")

    with col4:
        DDA = st.number_input('Shimmer:DDA (0.0-0.20)', min_value=0.0, max_value=0.20, value=0.0, format="%.5f")

    with col1:
        NHR = st.number_input('NHR (0.0-0.40)', min_value=0.0, max_value=0.40, value=0.0, format="%.5f")

    with col2:
        HNR = st.number_input('HNR (0.0-40.0)', min_value=0.0, max_value=40.0, value=0.0, format="%.3f")

    with col3:
        RPDE = st.number_input('RPDE (0.0-1.0)', min_value=0.0, max_value=1.0, value=0.0, format="%.5f")

    with col4:
        DFA = st.number_input('DFA (0.0-1.0)', min_value=0.0, max_value=1.0, value=0.0, format="%.5f")

    with col1:
        spread1 = st.number_input('spread1 (-10.0-0.0)', min_value=-10.0, max_value=0.0, value=-10.0, format="%.5f")

    with col2:
        spread2 = st.number_input('spread2 (0.0-1.0)', min_value=0.0, max_value=1.0, value=0.0, format="%.5f")

    with col3:
        D2 = st.number_input('D2 (0.0-5.0)', min_value=0.0, max_value=5.0, value=0.0, format="%.5f")

    with col4:
        PPE = st.number_input('PPE (0.0-1.0)', min_value=0.0, max_value=1.0, value=0.0, format="%.5f")

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
        st.success(parkinsons_diagnosis)


# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':

    # page title
    st.title('Breast Cancer Prediction using ML')

    # getting the input data from the user
    # Split into 5 columns for 30 features
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        mean_radius = st.number_input('Mean Radius (0-40)', min_value=0.0, max_value=40.0, value=0.0)
    with col2:
        mean_texture = st.number_input('Mean Texture (0-50)', min_value=0.0, max_value=50.0, value=0.0)
    with col3:
        mean_perimeter = st.number_input('Mean Perimeter (0-250)', min_value=0.0, max_value=250.0, value=0.0)
    with col4:
        mean_area = st.number_input('Mean Area (0-3000)', min_value=0.0, max_value=3000.0, value=0.0)
    with col5:
        mean_smoothness = st.number_input('Mean Smoothness (0-0.2)', min_value=0.0, max_value=0.2, value=0.0)

    with col1:
        mean_compactness = st.number_input('Mean Compactness (0-0.5)', min_value=0.0, max_value=0.5, value=0.0)
    with col2:
        mean_concavity = st.number_input('Mean Concavity (0-0.6)', min_value=0.0, max_value=0.6, value=0.0)
    with col3:
        mean_concave_points = st.number_input('Mean Concave Points (0-0.3)', min_value=0.0, max_value=0.3, value=0.0)
    with col4:
        mean_symmetry = st.number_input('Mean Symmetry (0-0.5)', min_value=0.0, max_value=0.5, value=0.0)
    with col5:
        mean_fractal_dimension = st.number_input('Mean Fractal Dim. (0-0.2)', min_value=0.0, max_value=0.2, value=0.0)

    with col1:
        radius_error = st.number_input('Radius Error (0-5)', min_value=0.0, max_value=5.0, value=0.0)
    with col2:
        texture_error = st.number_input('Texture Error (0-10)', min_value=0.0, max_value=10.0, value=0.0)
    with col3:
        perimeter_error = st.number_input('Perimeter Error (0-30)', min_value=0.0, max_value=30.0, value=0.0)
    with col4:
        area_error = st.number_input('Area Error (0-600)', min_value=0.0, max_value=600.0, value=0.0)
    with col5:
        smoothness_error = st.number_input('Smoothness Error (0-0.1)', min_value=0.0, max_value=0.1, value=0.0)

    with col1:
        compactness_error = st.number_input('Compactness Error (0-0.2)', min_value=0.0, max_value=0.2, value=0.0)
    with col2:
        concavity_error = st.number_input('Concavity Error (0-0.5)', min_value=0.0, max_value=0.5, value=0.0)
    with col3:
        concave_points_error = st.number_input('Concave Points Error (0-0.1)', min_value=0.0, max_value=0.1, value=0.0)
    with col4:
        symmetry_error = st.number_input('Symmetry Error (0-0.1)', min_value=0.0, max_value=0.1, value=0.0)
    with col5:
        fractal_dimension_error = st.number_input('Fractal Dim. Error (0-0.05)', min_value=0.0, max_value=0.05, value=0.0)

    with col1:
        worst_radius = st.number_input('Worst Radius (0-50)', min_value=0.0, max_value=50.0, value=0.0)
    with col2:
        worst_texture = st.number_input('Worst Texture (0-60)', min_value=0.0, max_value=60.0, value=0.0)
    with col3:
        worst_perimeter = st.number_input('Worst Perimeter (0-400)', min_value=0.0, max_value=400.0, value=0.0)
    with col4:
        worst_area = st.number_input('Worst Area (0-5000)', min_value=0.0, max_value=5000.0, value=0.0)
    with col5:
        worst_smoothness = st.number_input('Worst Smoothness (0-0.3)', min_value=0.0, max_value=0.3, value=0.0)

    with col1:
        worst_compactness = st.number_input('Worst Compactness (0-1.5)', min_value=0.0, max_value=1.5, value=0.0)
    with col2:
        worst_concavity = st.number_input('Worst Concavity (0-1.5)', min_value=0.0, max_value=1.5, value=0.0)
    with col3:
        worst_concave_points = st.number_input('Worst Concave Points (0-0.5)', min_value=0.0, max_value=0.5, value=0.0)
    with col4:
        worst_symmetry = st.number_input('Worst Symmetry (0-1.0)', min_value=0.0, max_value=1.0, value=0.0)
    with col5:
        worst_fractal_dimension = st.number_input('Worst Fractal Dim. (0-0.3)', min_value=0.0, max_value=0.3, value=0.0)

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

        user_input = [float(x) for x in user_input]
        bc_prediction = breast_cancer_model.predict([user_input])

        if bc_prediction[0] == 0:
            bc_diagnosis = 'The breast cancer is Malignant'
        else:
            bc_diagnosis = 'The breast cancer is Benign'
        st.success(bc_diagnosis)


# Maternal Health Prediction Page
if selected == 'Maternal Health Prediction':

    # page title
    st.title('Maternal Health Risk Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age (10-70)', min_value=10, max_value=70, value=10)
    with col2:
        systolic_bp = st.number_input('Systolic BP (70-160)', min_value=70, max_value=160, value=70)
    with col3:
        diastolic_bp = st.number_input('Diastolic BP (49-100)', min_value=49, max_value=100, value=49)
    with col1:
        bs = st.number_input('Blood Sugar (6.0-19.0)', min_value=6.0, max_value=19.0, value=6.0)
    with col2:
        body_temp = st.number_input('Body Temperature (98.0-103.0)', min_value=98.0, max_value=103.0, value=98.0)
    with col3:
        heart_rate = st.number_input('Heart Rate (7-90)', min_value=7, max_value=90, value=7)

    # code for Prediction
    maternal_diagnosis = ''

    # creating a button for Prediction
    if st.button('Maternal Health Test Result'):
        user_input = [age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate]
        
        user_input = [float(x) for x in user_input]

        # The model returns 'high risk', 'low risk', 'mid risk'
        maternal_prediction = maternal_health_model.predict([user_input])
        
        maternal_diagnosis = f'The predicted risk level is: {maternal_prediction[0]}'
        st.success(maternal_diagnosis)
