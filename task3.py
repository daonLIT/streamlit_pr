import streamlit as st
import pandas as pd
import numpy as np

st.header("Task 2: 데이터 표시하기")

# -----------------------
# 데이터 생성
# -----------------------
df = pd.DataFrame({
    "x": range(50),
    "y1": np.random.randn(50).cumsum(),
    "y2": np.random.randn(50).cumsum(),
    "category": np.random.choice(["A", "B", "C"], 50)
})

# -----------------------
# 라인 차트
# -----------------------
st.subheader("라인 차트")
st.line_chart(df[["x", "y1"]], x="x", y="y1")

# -----------------------
# 바 차트
# -----------------------
st.subheader("바 차트")
st.bar_chart(df[["x", "y2"]], x="x", y="y2")

# -----------------------
# 에어리어(면적) 차트
# -----------------------
st.subheader("에어리어(Area) 차트")
st.area_chart(df[["x", "y1"]], x="x", y="y1")

# -----------------------
# 매트릭(지표)
# -----------------------
st.subheader("지표 정보")

col1, col2, col3 = st.columns(3)
col1.metric("평균 y1", f"{df['y1'].mean():.2f}")
col2.metric("평균 y2", f"{df['y2'].mean():.2f}")
col3.metric("A 비율", f"{(df['category']=='A').mean()*100:.1f}%")

# -----------------------
# 데이터프레임 표시
# -----------------------
st.subheader("데이터프레임")
st.dataframe(df)
