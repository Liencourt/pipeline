import streamlit as st
from datetime import datetime

email = st.text_input("e-mail")
data = st.date_input("Data",value="today",format="DD/MM/YYYY")
hora = st.time_input("Hora")
valor = st.number_input("Valor")
qtd = st.number_input("Quantidade")
produto = st.selectbox("Seleção",["GPT","ILAMA",'GEMINI'])
if st.button("Salvar"):
    data_hora = datetime.combine(data,hora)
    st.write(data_hora)