import streamlit as st

st.title(" Gente. Esta es la pagina de emprendedores")

st.write("Esto es una prueba para utilizar el write")
st.write("Vamos a utilizar algunas funciones del modulo streamlit")

nombre = st.text_input("Ingresa tu nombre o alias?")

st.write(nombre)
