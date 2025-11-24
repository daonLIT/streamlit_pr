import streamlit as st

st.set_page_config(
    page_title="Streamlit Tutorial",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="auto"
)

st.title("Streamlit 기본 실습 - 메인 페이지")
st.write("""

- Task 6 페이지: 레이아웃 구성 (컬럼, 탭, Expander)
- Task 7 페이지: penguins 데이터 기반 종합 대시보드
왼쪽 사이드바에서 페이지를 선택 후 이동.
""")
