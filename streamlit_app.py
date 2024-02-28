import streamlit as st

st.title("Viajando por el Norte")
st.write("El viaje se encamina por la via de un tren a lo largo del rio ")
st.markdown("## Laboratorio Botanico")
st.markdown("*Buenas tarde mi Botanico*")

animales= ("Mantis", "Dragon de Comodo", "Mandragora")
name = st.text_input('Introduce un Animal')
if name in animales:
    st.write(f"Este animal {name} existe en tu camino")

def aplicarEdad(x):
    return x * 10

edad= st.number_input('¿Que edad tienes')
if st.button("click Aqui"):
    st.write(f"Tu edad es {aplicarEdad(edad)}")

st.title("*Calculadora CM*")


def Sumar(x, y):
    return x+y

def Restar(x, y):
    return x-y

def Multiplicar(x, y):
    return x*y

def Dividir(x, y):
    return x/y

num1= st.number_input("Introducir el primer numero",
                      min_value=0, max_value=100)
num2= st.number_input("Introducir el segundo numero",
                      min_value=0, max_value=100)

calcular= oper =st.radio("Selecciona una operacion:", ["Sumar", "Multiplicar", "Restar", "Dividir"])

if st.button("calcular"):
    st.markdown(f"# {calcular(num1, num2, oper)}")

left_column, right_column = st.columns(2)

with left_column:
    st.markdown("# hola left")
    st.video("https://www.youtube.com/watch?v=LnEFo0pHj9U")
with right_column:
    st.markdown("# hola right")
    st.video("https://www.youtube.com/watch?v=ME9P6oHqcxQ")


# add_slider= st.sidebar.slider('Select a range of value', 0.0, 100,0 (25.0, 75.0))

lenguajes =("Java", "C+", "python")
opcion = st.sidebar.selectbox("Seleccionar un lenguaje", lenguajes)

if opcion:
    st.write(f"Has seleccionado :umbrella_with_rain_drops: {opcion}")



