import streamlit as st

st.header("Task 1: 기본 UI 컴포넌트")

if 'name' not in st.session_state:
    st.session_state['name'] = ' '

if 'color' not in st.session_state:
    st.session_state['color'] = ' '

name_input = st.text_input("이름을 입력하세요")


age_input = st.select_slider(
    "나이를 선택하세요",
    options=list(range(0, 101)),   
    value=20                       
)

color_input = st.text_input("좋아하는 색")

if st.checkbox('이용 약관에 동의합니다'):
    st.write('약관에 동의 하셨습니다.')

st.button("제출")


