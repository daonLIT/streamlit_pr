import streamlit as st
import pandas as pd

st.header("Task 2: 데이터프레임 & 지표 표시")

# CSV 불러오기
df = pd.read_csv("penguins.csv")

# 데이터프레임 표시
st.subheader("데이터프레임")
st.dataframe(df)

# 지표 정보
st.subheader("지표 정보")

a, b = st.columns(2)
c, d = st.columns(2)

a.metric("평균 체중 (g)", f"{df['body_mass_g'].mean():.1f} g")
b.metric("평균 부리길이 (mm)", f"{df['bill_length_mm'].mean():.1f} mm")
c.metric("평균 부리두께 (mm)", f"{df['bill_depth_mm'].mean():.1f} mm")
d.metric("전체 개체 수", len(df))
