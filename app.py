import streamlit as st

st.title("¡Hola desde Streamlit!")
st.write("Esta es mi primera aplicación web con Python.")

# Entrada de texto
nombre = st.text_input("¿Cómo te llamas?")

# --- NUEVO: Entrada de número con un deslizador ---
edad = st.slider("¿Cuántos años tienes?", 0, 100, 25) 

if nombre:
    st.write(f"Mucho gusto, {nombre}")
    
    # Mensaje condicional según la edad
    if edad < 18:
        st.write(f"¡Eres muy joven, {nombre}! Tienes apenas {edad} años.")
    else:
        st.write(f"Qué bien, {nombre}. A los {edad} años se aprende mucho de programación.")
