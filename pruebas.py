import streamlit as st
import sqlite3
import pandas as pd

# --- CONFIGURACIÓN DE BASE DE DATOS ---
def init_db():
    conn = sqlite3.connect('consumo_gaseosas.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS consumos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            denominacion TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio_unitario REAL NOT NULL,
            total REAL NOT NULL,
            fecha DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    return conn

# --- LÓGICA DE NEGOCIO ---
def guardar_registro(denominacion, cantidad, p_unitario):
    total = cantidad * p_unitario
    conn = sqlite3.connect('consumo_gaseosas.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO consumos (denominacion, cantidad, precio_unitario, total)
        VALUES (?, ?, ?, ?)
    ''', (denominacion, cantidad, p_unitario, total))
    conn.commit()
    conn.close()

# --- INTERFAZ STREAMLIT ---
st.set_page_config(page_title="Control de Inventario", layout="wide")
init_db()

st.title("🥤 Registro de Consumo de Gaseosas")

# Formulario de entrada
with st.form("registro_form", clear_on_submit=True):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        denominacion = st.text_input("Denominación (ej. Inca Kola 500ml)")
    with col2:
        cantidad = st.number_input("Cantidad", min_value=1, step=1)
    with col3:
        p_unitario = st.number_input("Precio Unitario", min_value=0.0, format="%.2f")
    
    submit = st.form_submit_button("Registrar Consumo")

if submit:
    if denominacion:
        guardar_registro(denominacion, cantidad, p_unitario)
        st.success(f"Registro guardado: {denominacion}")
    else:
        st.error("Por favor, ingresa una denominación.")

# Visualización de datos
st.divider()
st.subheader("Historial de Consumos")

conn = sqlite3.connect('consumo_gaseosas.db')
df = pd.read_sql_query("SELECT denominacion, cantidad, precio_unitario, total, fecha FROM consumos ORDER BY fecha DESC", conn)
conn.close()

if not df.empty:
    st.dataframe(df, use_container_width=True)
    
    # Resumen analítico
    st.metric("Inversión Total", f"S/. {df['total'].sum():.2f}")
else:
    st.info("Aún no hay registros en la base de datos.")