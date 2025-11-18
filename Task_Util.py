import streamlit as st
from PIL import Image

# 페이지 설정
st.set_page_config(
    page_title="Streamlit Tutorial",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="auto"
)

# =====================================================
# Task 6 : 레이아웃 구성 - 컬럼, 탭, Expander
# =====================================================

st.title("Task 6 : 레이아웃 구성 연습")
st.write("컬럼, 탭, Expander를 이용해서 화면을 나눠보는 예제입니다.")

# 1) 컬럼 예제 -------------------------------------------------
st.subheader("1) 컬럼(Columns) 예제")

col1, col2 = st.columns(2)

with col1:
    st.write("**왼쪽 컬럼**")
    name = st.text_input("이름 입력", key="col_name")

with col2:
    st.write("**오른쪽 컬럼**")
    age = st.number_input("나이 입력", min_value=0, max_value=120, value=20, key="col_age")

st.write(f"입력 결과 → 이름: {name}, 나이: {age}")

st.divider()

# 2) 탭 예제 ---------------------------------------------------
st.subheader("2) 탭(Tabs) 예제")

tab1, tab2, tab3 = st.tabs(["소개", "입력 폼", "결과"])

with tab1:
    st.write("여기는 **소개** 탭입니다.")
    st.write("Task 6에서 탭을 사용하는 예제입니다.")

with tab2:
    st.write("여기는 **입력 폼** 탭입니다.")
    city = st.text_input("사는 도시를 입력하세요.", key="tab_city")
    hobby = st.text_input("취미를 입력하세요.", key="tab_hobby")

with tab3:
    st.write("여기는 **결과** 탭입니다.")
    st.write(f"- 도시: {city}")
    st.write(f"- 취미: {hobby}")

st.divider()

# 3) Expander 예제 ---------------------------------------------
st.subheader("3) Expander 예제")

with st.expander("추가 설명 보기"):
    st.write(""" 
    """)
