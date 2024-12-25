import streamlit as st
import numpy as np
import pickle

# Modelni yuklash
model_path = 'model.pkl' 
with open(model_path, 'rb') as file:
    model = pickle.load(file)

st.title("Mijozning Omonat Qo'yishi Haqida Bashorat")
st.write("Iltimos, quyidagi ma'lumotlarni kiriting:")

age = st.number_input("Yosh:", 18, 100)

job_options = ["admin.", "technician", "services", "management", 
               "blue-collar", "retired", "student", "unemployed", 
               "entrepreneur", "housemaid", "self-employed"]
job = st.selectbox("Kasb:", job_options)
job_index = job_options.index(job)

marital_options = ["married", "single", "divorced"]
marital = st.selectbox("Turmush holati:", marital_options)
marital_index = marital_options.index(marital)

education_options = ["primary", "secondary", "tertiary", "unknown"]
education = st.selectbox("Ta'lim darajasi:", education_options)
education_index = education_options.index(education)

default_options = ["no", "yes"]
default = st.selectbox("Bankrotlik:", default_options)
default_index = default_options.index(default)

balance = st.number_input("Hisob qoldig'i:", -10000, 100000)

housing_options = ["no", "yes"]
housing = st.selectbox("Uy-joy krediti:", housing_options)
housing_index = housing_options.index(housing)

loan_options = ["no", "yes"]
loan = st.selectbox("Kredit-qarz:", loan_options)
loan_index = loan_options.index(loan)

contact_options = ["cellular", "telephone", "unknown"]
contact = st.selectbox("Kontakt turi:", contact_options)
contact_index = contact_options.index(contact)

day = st.number_input("Kun:", 1, 31)
month = st.number_input("Oy:", 1, 12)
duration = st.number_input("Muloqot davomiyligi (soniya):", 0)
campaign = st.number_input("Kampaniya marta:", 0)
pdays = st.number_input("Oldingi kampaniya o‘tgach kunlar soni:", -1)
previous = st.number_input("Oldingi kampaniyalar soni:", 0)
poutcome = st.number_input("Oldingi kampaniya natijasi:", 0)

if st.button("Bashorat qilish"):
    input_data = np.array([age, job_index, marital_index, education_index, default_index, balance, 
                           housing_index, loan_index, contact_index, day, month, duration, 
                           campaign, pdays, previous, poutcome])
    input_data = input_data.reshape(1, -1)  # Modelga mos shaklga o‘tkazish

    prediction = model.predict(input_data)  # Bashorat qilish
    result = "Omonat qo'yishi mumkin" if prediction[0] == "yes" else "Omonat qo'yishi mumkin emas"
    st.success(result)
