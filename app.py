# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:53:51 2022

@author: Thamarai kannan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# loading the saved models
import streamlit as st
from streamlit_login_auth_ui.widgets import __login__

__login__obj = __login__(auth_token = "courier_auth_token", 
                    company_name = "Shims",
                    width = 200, height = 250, 
                    logout_button_name = 'Logout', hide_menu_bool = False, 
                    hide_footer_bool = False, 
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:
    diabetes_model = pickle.load(open('saved models/diabetes_model.sav', 'rb'))

    heart_disease_model = pickle.load(open('saved models/heart_disease.sav','rb'))

    parkinsons_model = pickle.load(open('saved models/parkinsons_disease.sav', 'rb'))

    model = pickle.load(open('saved models/model.pkl','rb'))

    # sidebar for navigation
    with st.sidebar:
        
        selected = option_menu('Multiple Disease Prediction System',
                            
                            ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Symptoms'],
                            icons=['activity','heart','person','tree'],
                            default_index=0)

        
        
    # Diabetes Prediction Page
    if (selected == 'Diabetes Prediction'):
        
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
        
        # creating a button for Prediction
        
        if st.button('Diabetes Test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if (diab_prediction[0] == 1):
                st.markdown('<h1 style="color:red;font-size:24px">⚠️ WE HIGHLY RECOMMEND YOU TO CONSULT WITH A SPECIALIST!</h1>',unsafe_allow_html=True)
            else:
                st.markdown('<h1 style="color:green;font-size:24px">😄YOU ARE GOOD TO GO, HOWEVER IT IS GOOD TO HAVE A REGULAR HEALTH CHECKUP. CHEERS!</h1>',unsafe_allow_html=True)




    # Heart Disease Prediction Page
    if (selected == 'Heart Disease Prediction'):
        
        # page title
        st.title('Heart Disease Prediction using ML')
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            age = st.text_input('Age')
            
        with col2:
            sex = st.text_input('Gender: Male-1, Women-0')
            
        with col3:
            cp = st.text_input('Chest Pain types: Values (0,1,2)')
            
        with col1:
            trestbps = st.text_input('Resting blood pressure (on admission to the hospital):Values(94, 200)')
            
        with col2:
            chol = st.text_input('Serum Cholestoral in mg/dl: Values(125, 560)')
            
        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl: Values(0,1)')
            
        with col1:
            restecg = st.text_input('Resting Electrocardiographic results: \n Values(0,1,2)')
            
        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved: Values(70,200)')
            
        with col3:
            exang = st.text_input("Exercise Induced Angina: Values(0='no',1='yes')")
            
        with col1:
            oldpeak = st.text_input('ST depression induced by exercise: Values(0-6)')
            
        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment:Values(0-2)')
            
        with col3:
            ca = st.text_input('Major vessels colored by flourosopy: Values(0,1,2,3,4)')
            
        with col1:
            thal = st.text_input('maximum heart rate achieved: 0 = normal; 1 = fixed defect; 2 = reversable defect')
            
            
        
        
        # code for Prediction
        
        # creating a button for Prediction
        
        if st.button('Heart Disease Test Result'):
          
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
            
            if (heart_prediction[0] == 1):
                st.markdown('<h1 style="color:red;font-size:24px">⚠️WE HIGHLY RECOMMEND YOU TO CONSULT WITH A SPECIALIST!</h1>',unsafe_allow_html=True)
            else:
                st.markdown('<h1 style="color:green;font-size:24px">😄YOU ARE GOOD TO GO, HOWEVER IT IS GOOD TO HAVE A REGULAR HEALTH CHECKUP. CHEERS!</h1>',unsafe_allow_html=True)

            
        
        

    # Parkinson's Prediction Page
    if (selected == "Parkinsons Prediction"):
        
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
        
        # creating a button for Prediction    
        if st.button("Parkinson's Test Result"):
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
            
            if (parkinsons_prediction[0] == 1):
                st.markdown('<h1 style="color:red;font-size:24px">⚠️ WE HIGHLY RECOMMEND YOU TO CONSULT WITH A SPECIALIST!</h1>',unsafe_allow_html=True)
            else:
                st.markdown('<h1 style="color:green;font-size:24px">😄YOU ARE GOOD TO GO, HOWEVER IT IS GOOD TO HAVE A REGULAR HEALTH CHECKUP. CHEERS!</h1>',unsafe_allow_html=True)

        st.markdown("<h3>Attribute Information:</h3><br><p>Matrix column entries (attributes):</p>" ,unsafe_allow_html=True )
        st.markdown("<ul><li>name - ASCII subject name and recording number </li><li>MDVP:Fo(Hz) - Average vocal fundamental frequency </li><li>MDVP:Fhi(Hz) - Maximum vocal fundamental frequency </li><li>MDVP:Flo(Hz) - Minimum vocal fundamental frequency * MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP - Several measures of variation in fundamental frequency </li><li>MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA - Several measures of variation in amplitude </li><li>NHR,HNR - Two measures of ratio of noise to tonal components in the voice </li><li>status - Health status of the subject (one) - Parkinson's, (zero) - healthy </li><li>RPDE,D2 - Two nonlinear dynamical complexity measures </li<li>DFA - Signal fractal scaling exponent * spread1,spread2,PPE - Three nonlinear measures of fundamental frequency variation</li></ul>" ,unsafe_allow_html=True )
    symb = ['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
    'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
    'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
    'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
    'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
    'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
    'yellow_crust_ooze']

    disease=['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis',
        'Drug Reaction', 'Peptic ulcer diseae', 'AIDS', 'Diabetes ',
        'Gastroenteritis', 'Bronchial Asthma', 'Hypertension ', 'Migraine',
        'Cervical spondylosis', 'Paralysis (brain hemorrhage)', 'Jaundice',
        'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
        'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E',
        'Alcoholic hepatitis', 'Tuberculosis', 'Common Cold', 'Pneumonia',
        'Dimorphic hemmorhoids(piles)', 'Heart attack', 'Varicose veins',
        'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
        'Osteoarthristis', 'Arthritis',
        '(vertigo) Paroymsal  Positional Vertigo', 'Acne',
        'Urinary tract infection', 'Psoriasis', 'Impetigo']

    if (selected=="Symptoms"):
        
        pred = np.zeros((1,95))
        st.title("Prediction using Symptoms")
            
        col1, col2, col3 = st.columns(3)
            
        with col1:
            option1 = st.selectbox('Symptom-1', ('default','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
        'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
        'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
        'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
        'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
        'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
        'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
        'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
        'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
        'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
        'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
        'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
        'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
        'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
        'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
        'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
        'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
        'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
        'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
        'yellow_crust_ooze'))
                
        with col2:
            option2 = st.selectbox('Symptom-2', ('default','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
        'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
        'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
        'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
        'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
        'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
        'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
        'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
        'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
        'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
        'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
        'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
        'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
        'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
        'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
        'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
        'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
        'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
        'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
        'yellow_crust_ooze'))
                
        with col3:
            option3 = st.selectbox('Symptom-3', ('default','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
        'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
        'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
        'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
        'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
        'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
        'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
        'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
        'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
        'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
        'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
        'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
        'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
        'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
        'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
        'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
        'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
        'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
        'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
        'yellow_crust_ooze'))
                
        with col1:
            option4 = st.selectbox('Symptom-4', ('default','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
        'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
        'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
        'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
        'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
        'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
        'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
        'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
        'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
        'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
        'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
        'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
        'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
        'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
        'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
        'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
        'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
        'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
        'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
        'yellow_crust_ooze'))

        with col2:
            option5 = st.selectbox('Symptom-5', ('default','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
        'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
        'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
        'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
        'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
        'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
        'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
        'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
        'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
        'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
        'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
        'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
        'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
        'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
        'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
        'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
        'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
        'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
        'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
        'yellow_crust_ooze'))

        with col3:
            option6 = st.selectbox('Symptom-6', ('default','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
        'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
        'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
        'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
        'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
        'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
        'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
        'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
        'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
        'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
        'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
        'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
        'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
        'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
        'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
        'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
        'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
        'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
        'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
        'yellow_crust_ooze'))
            
        op2=[i for i,s in enumerate(symb) if option2 in s]
        op1=[i for i,s in enumerate(symb) if option1 in s]
        op4=[i for i,s in enumerate(symb) if option4 in s]
        op5=[i for i,s in enumerate(symb) if option5 in s]
        op6=[i for i,s in enumerate(symb) if option6 in s]
        op3=[i for i,s in enumerate(symb) if option3 in s]
        try:
            pred[0][op1[0]]=1
            pred[0][op2[0]]=1
            pred[0][op3[0]]=1
            pred[0][op4[0]]=1
            pred[0][op5[0]]=1
            pred[0][op6[0]]=1
        except:
            pass
        
        if st.button("Test result"):
            if option1 == 'default' or option2 == 'default'  or option3 == 'default':
                st.markdown("Please select above options")
            else:
                symptom = model.predict(pred)
                st.markdown(f'<h1 style="color:red;font-size:24px">⚠️ You are likely to have {disease[symptom[0]]} (Disease)</h1>',unsafe_allow_html=True)
