import streamlit as st
from datetime import datetime

st.title(' La eterna noche')

st.title(' Formulario')

with st.form("my_form", clear_on_submit=True):

   # nombres=(',')

    nombres= st.text_input(' Escribe tu nombre')
    problema = st.text_area('  Introduce el problema que as encontrado ')


    if st.form_submit_button(" Agregar problema"):
        descripcion =nombres + " - " + problema + " - " + str(datetime.now())
        with open("problemas.txt", "a") as f:
            f.write(descripcion + "\n")

        # f.write(f"{nombres} + {problema}")
    st.write(f"{nombres} gracias por darnos tu opinion  ")

if st.button("Agregar informe"):
    with open("problemas.txt", "r") as f:
        st.write(f.readline())
if "counter" not in st.session_state:
    st.session_state.counter=0

if st.button("contar"):
    st.session_state.counter +=1

st.write(f"{st.session_state.counter} veces que pinchamos")

st.write(f"introducir: usar st.write() para imprimir")

codigo = st.text_area("introduce codigo")

if codigo:
    exec(codigo)


