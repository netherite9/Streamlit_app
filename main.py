import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64

@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1, "Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val, my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediksi'])
if app_mode == 'Home':
    st.title('Loan Prediction')
    st.image('loan_image.jpg')
    st.markdown('Dataset:')
    data = pd.read_csv('loan_dataset.csv')
    st.write(data.head())
    st.bar_chart(data[['ApplicantIncome', 'LoanAmount']].head(20))

if app_mode == 'Prediction':
    ApplicantIncome = st.sidebar.slider('ApplicantIncome', 0, 10000, 0)
    LoanAmount = st.sidebar.slider('LoanAmount in K$', 9.0, 700.0, 200.0)
    if st.button("Predict"):
        file_ = open("6m-rain.gif", "rb")        
        contents = file_.read()        
        data_url = base64.b64encode(contents).decode("utf-8")        
        file_.close()        
        file = open("green-cola-no.gif", "rb")        
        contents = file.read()        
        data_url_no = base64.b64encode(contents).decode("utf-8")        
        file.close()        
        loaded_model = pickle.load(open('Random_Forest.sav', 'rb'))        
        prediction = loaded_model.predict(single_sample)        
        if prediction[0] == 0 :            
            st.error(    'According to our Calculations, you will not get the loan from Bank'    )            
            st.markdown(    f'<img src="data:image/gif;base64,{data_url_no}" alt="cat gif">', unsafe_allow_html=True,)        
        elif prediction[0] == 1 :            
            st.success(    'Congratulations!! you will get the loan from Bank'    )            
            st.markdown(    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True,)
