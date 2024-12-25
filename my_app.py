import streamlit as st
import numpy as np
import pickle

model_path ='model (1).pkl' 
with open(model_path, 'rb') as file:
model = pickle.load(file)

st.title("Mijozning Omonat Qo'yishi Haqida Bashorat")
st.write("Iltimos, quyidagi ma'lumotlarni kiriting:")

age = st.number_input("Yosh:", 18, 100)
job = st.selectbox("Kasb:", ["admin.", "technician", "services", "management", 
                               "blue-collar", "retired", "student", "unemployed", 
                               "entrepreneur", "housemaid", "self-employed"])
marital = st.selectbox("Turmush holati:", ["married", "single", "divorced"])
balance = st.number_input("Hisob qoldig'i:", -10000, 100000)
default = st.selectbox("Bankrotlik:", ["no", "yes"])
housing = st.selectbox("Uy-joy krediti:", ["no", "yes"])
loan = st.selectbox("Kredit-qarz:", ["no", "yes"])

if st.button("Bashorat qilish"):
    input_data = np.array([[age, job, marital, balance, default, housing, loan]])
    prediction = model.predict(input_data)
    result = "Omonat qo'yishi mumkin" if prediction[0] == "yes" else "Omonat qo'yishi mumkin emas"
    st.success(result)
