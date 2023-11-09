import streamlit as st

st.title('Filmes escolhidos pela nossa turma.')
st.write('Terceiro ano do curso Técnico em Informática IFPR - Cascavel, 2023')

nome = st.text_input('Digite seu nome')
st.write(f'Olá, {nome}')

filmes = []

series = ['Grays Anatomy',
            ]

jogos = ['']

filme = st.selectbox('Filme predileto', filmes)
st.write(f'filme predileto: {filme}')
serie = st.multiselect('Serie Predileta', series)
st.write(f'serie predileta: {serie}')
jogo = st.selectbox('Jogo predileto', jogos)
st.write(f'jogo predileto: {jogo}')