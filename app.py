import streamlit as st

st.title("¡Hola desde Streamlit!")
st.write("Esta es mi primera aplicación web con Python.")

nombre = st.text_input("¿Cómo te llamas?")
if nombre:
    st.write(f"Mucho gusto, {nombre}")