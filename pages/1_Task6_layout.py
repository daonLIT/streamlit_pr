import streamlit as st
import datetime

st.title("Task 6 : 레이아웃 구성 연습")
st.write("컬럼(Columns), 탭(Tabs), Expander를 이용한 대시보드 레이아웃")

# =================================================
# 1) 컬럼 예제 : 왼쪽 입력, 오른쪽 상태
# =================================================
st.subheader("1) 컬럼(Columns) 예제")

left, right = st.columns(2)

with left:
    st.write("**왼쪽 컬럼 - 입력 영역**")
    name = st.text_input("이름 입력")

    birthday = st.date_input(
        "생일 입력",
        value=datetime.date.today(),
        min_value=None,
        max_value=None
    )


with right:
    st.write("**오른쪽 컬럼 - 상태 영역**")
    agree = st.checkbox("개인정보 제공에 동의합니다.")
    if st.button("제출"):
        if agree:
            st.success(f"{name or '이름 미입력'} 님의 정보가 제출되었습니다.")
        else:
            st.warning("동의 체크박스를 먼저 선택해 주세요.")

st.divider()

# =================================================
# 2) 탭 예제 : 같은 화면을 탭으로 나누기
# =================================================
st.subheader("2) 탭(Tabs) 예제")

tab1, tab2, tab3 = st.tabs(["텍스트 출력", "메시지 박스", "기타"])

with tab1:
    st.write("### write() 예제")
    st.write("Hello, Streamlit!")
    st.write(["Hello", "Streamlit", "List"])

with tab2:
    st.write("### 메시지 박스 예제")
    st.error("This is an error")
    st.warning("This is a warning")
    st.info("This is a purely informational message")
    st.success("This is a success message!")

with tab3:
    st.write("### 버튼 예제")
    if st.button("Say Hello", key="tab_button"):
        st.write("Hello")
    else:
        st.write("Goodbye")

st.divider()

# =================================================
# 3) Expander 예제 : 설명 접기/펼치기
# =================================================
st.subheader("3) Expander 예제")

with st.expander("이 페이지에서 사용한 기능 설명 보기"):
    st.markdown("""
    - **Columns**  
     

    - **Tabs** 
     

    - **Expander**   
      
    """)

st.success("Task 6 : 레이아웃 구성")
