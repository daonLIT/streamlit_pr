import streamlit as st
import pandas as pd

st.header("Task 3: 차트 시각화")


df = pd.read_csv("penguins.csv")

st.subheader("라인 차트: Body Mass")
st.line_chart(df["body_mass_g"])

st.subheader("바 차트: Species별 평균 체중")
species_mean = df.groupby("species")["body_mass_g"].mean()
st.bar_chart(species_mean)


st.subheader("에어리어 차트: Bill Length")
st.area_chart(df["bill_length_mm"])


st.subheader("산점도: Bill Length vs Bill Depth")
st.scatter_chart(df, x="bill_length_mm", y="bill_depth_mm")
