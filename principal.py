import streamlit as st
import pandas as pd
import joblib


arvore = joblib.load('arvore.sav')

st.title('Arvore de Decisao - Alunos')
