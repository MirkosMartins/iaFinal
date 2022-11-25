import streamlit as st
import pandas as pd
import joblib


arvore = joblib.load('arvore.sav')

st.title('Arvore de Decisao - Alunos')
individuo = []

genero = st.selectbox('Digite o sexo do aluno:',('Masculino','Feminino'))
if genero=='Masculino':
  individuo.append(0)
else:
  individuo.append(1)
st.write(individuo)

