import streamlit as st

st.title('Teobaldo')

nome = st.text_input('Digite seu nome')
st.write(f'Olá, {nome}')

filmes = ['A princesa e o Sapo', 
          'Barbie e o Portal Secreto', 
          'Como Treinar Seu Dragão',
          'It follows',
          'Spiderman',
          '10 things i hate about you',
          'Parasite of love']

series = ['Grays Anatomy',
        'The sex life of college girls',
        'O mentalista',
        'The big bang theory',
        'Station 19',
        'Brooklyn 99']

jogos = ['Call of Duty',
         'Amor Doce',
         'Factorio',
         'Dying Light'
         'Minecraft',
         'Teh last of us']

filme = st.selectbox('Filme predileto', filmes)
st.write(f'filme predileto: {filme}')
serie = st.multiselect('Serie Predileta', series)
st.write(f'serie predileta: {serie}')
jogo = st.selectbox('Jogo predileto', jogos)
st.write(f'jogo predileto: {jogo}')