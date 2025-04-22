import streamlit as st

st.set_page_config(page_title="Calculadora de Gases Ideales", page_icon="🌡️")

R = 0.0821  # Constante de los gases ideales en L·atm/(mol·K)

st.title("🌡️ Calculadora de Gases Ideales")
st.markdown("**Ecuación:** PV = nRT")

opciones = ["Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)"]
eleccion = st.selectbox("¿Qué variable quieres calcular?", opciones)

if eleccion == "Presión (P)":
    V = st.number_input("Volumen (L)", min_value=0.01, step=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01, step=0.1)
    n = st.number_input("Número de moles (mol)", min_value=0.01, step=0.01)
    if st.button("Calcular Presión"):
        P = (n * R * T) / V
        st.success(f"La presión es: {P:.2f} atm")

elif eleccion == "Volumen (V)":
    P = st.number_input("Presión (atm)", min_value=0.01, step=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01, step=0.1)
    n = st.number_input("Número de moles (mol)", min_value=0.01, step=0.01)
    if st.button("Calcular Volumen"):
        V = (n * R * T) / P
        st.success(f"El volumen es: {V:.2f} litros")

elif eleccion == "Temperatura (T)":
    V = st.number_input("Volumen (L)", min_value=0.01, step=0.01)
    P = st.number_input("Presión (atm)", min_value=0.01, step=0.01)
    n = st.number_input("Número de moles (mol)", min_value=0.01, step=0.01)
    if st.button("Calcular Temperatura"):
        T = (P * V) / (n * R)
        st.success(f"La temperatura es: {T:.2f} K")

elif eleccion == "Número de moles (n)":
    V = st.number_input("Volumen (L)", min_value=0.01, step=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01, step=0.1)
    P = st.number_input("Presión (atm)", min_value=0.01, step=0.01)
    if st.button("Calcular Número de moles"):
        n = (P * V) / (R * T)
        st.success(f"El número de moles es: {n:.2f} mol")
