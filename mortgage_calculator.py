import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import math 

st.title("Mortgage Repayment Calculator")

st.write('### Input Data')
col1, col2 = st.columns(2)
home_value = col1.number_input("Home Value", min_value=0, max_value=500000)
deposit = col1.number_input("Deposit", min_value=0, max_value=100000)
