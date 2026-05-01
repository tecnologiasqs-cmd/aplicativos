import streamlit as st

# 1. Configuración de Estilo (Fondo Azul y Texto Blanco)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1E3A8A;
    }
    .stApp h1, .stApp p, .stApp span, .stApp label, .stMarkdown {
        color: white !important;
    }
    /* Estilo para las cajas de entrada */
    .stNumberInput input {
        color: #1E3A8A !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🥤 Registro de Consumo de Bebidas")
st.write("Complete la información para calcular el total del pedido.")

# 2. Definición de los productos por categorías
productos = {
    "Gaseosas": ["Gaseosa 2L", "Gaseosa 1L", "Gaseosa 1/2L Retornable", "Gaseosa 1/2L Descartable", "Gaseosa Personal"],
    "Cervezas": ["Cerveza Trujillo", "Cerveza Callao", "Cerveza de Trigo", "Cerveza Negra"],
    "Otros": ["Agua Mineral"]
}

# 3. Interfaz de Usuario
st.subheader("Selección de Productos")

# Creamos una lista para guardar los datos registrados
datos_registro = []

# Iteramos sobre las categorías para organizar la vista
for categoria, lista_productos in productos.items():
    with st.expander(f"Ver {categoria}"):
        for producto in lista_productos:
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.write(f"**{producto}**")
            
            with col2:
                # Campo de Cantidad
                cantidad = st.number_input(f"Cant. ({producto})", min_value=0, step=1, key=f"cant_{producto}")
            
            with col3:
                # Campo de Precio Unitario
                precio = st.number_input(f"Precio S/. ({producto})", min_value=0.0, step=0.1, key=f"prec_{producto}")
            
            # Cálculo de Total por producto
            total_producto = cantidad * precio
            
            if cantidad > 0:
                datos_registro.append({
                    "Producto": producto,
                    "Cantidad": cantidad,
                    "Precio U.": precio,
                    "Total": total_producto
                })
                st.write(f"👉 Subtotal: **S/. {total_producto:.2f}**")

# 4. Resumen Final
st.markdown("---")
if datos_registro:
    st.subheader("📊 Resumen del Registro")
    # Mostramos una tabla con lo consumido
    st.table(datos_registro)
    
    # Calculamos el Gran Total
    gran_total = sum(item["Total"] for item in datos_registro)
    st.success(f"### TOTAL A PAGAR: S/. {gran_total:.2f}")
else:
    st.info("Aún no se han registrado consumos.")