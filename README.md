import streamlit as st
import pandas as pd
import pickle


model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)


st.title("Mijozning Omonat Qo'yishi Haqida Bashorat")
st.write("Iltimos, quyidagi ma'lumotlarni kiriting:")


age = st.number_input("Yosh:", min_value=18, max_value=100)
job = st.selectbox("Kasb:", ["admin.", "technician", "services", "management", "blue-collar", "retired", "student", "unemployed", "entrepreneur", "housemaid", "self-employed"])
marital = st.selectbox("Turmush holati:", ["married", "single", "divorced"])
education = st.selectbox("Ta'lim darajasi:", ["primary", "secondary", "tertiary", "unknown"])
default = st.selectbox("Bankrotlik:", ["no", "yes"])
balance = st.number_input("Hisob qoldig'i:")
housing = st.selectbox("Uy-joy krediti:", ["no", "yes"])
loan = st.selectbox("Kredit-qarz:", ["no", "yes"])
contact = st.selectbox("Aloqa usuli:", ["unknown", "cellular", "telephone"])
day = st.number_input("Kun:", min_value=1, max_value=31)
month = st.selectbox("Oy:", ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])
duration = st.number_input("Muddati (sekundlarda):")
campaign = st.number_input("Aksiya soni:")
pdays = st.number_input("Oxirgi aloqa qilingan kundan beri o'tgan kunlar:")
previous = st.number_input("Avvalgi aloqalar soni:")
poutcome = st.selectbox("Avvalgi natija:", ["unknown", "success", "failure", "other"])


input_data = [[age, job, marital, education, default, balance, housing, loan, contact, day, month, duration, campaign, pdays, previous, poutcome]]
input_df = pd.DataFrame(input_data, columns=[
    "age", "job", "marital", "education", "default", "balance", "housing", "loan", 
    "contact", "day", "month", "duration", "campaign", "pdays", "previous", "poutcome"
])


if st.button("Bashorat qilish"):
    prediction = model.predict(input_df)
    result = "Omonat qo'yishi mumkin" if prediction[0] == "yes" else "Omonat qo'yishi mumkin emas"
    st.success(result)
