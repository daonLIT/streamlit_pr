import streamlit as st
import pandas as pd
import pickle
import os.path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# 사이킷런, 판다스가 없는경우 아래코드 실행
# pip install streamlit pandas scikit-learn

# Task 4
st.header("Task 4")
st.subheader("인터렉티브 필터")

