#Biblioteca usada para carregar servidores web, usada mais para data science
import streamlit as st

#Titulo 
st.title('Frases Star Wars')


frase = st.text_input("Hello there")

st.write("I have a bad feeling about this")

x = st.selectbox("May the force be with you", ["no", "screw you", "You too!"])
st.write(f'')

click = st.button("Don't press here!")
