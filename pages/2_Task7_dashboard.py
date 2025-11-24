import streamlit as st
from PIL import Image
import time
import datetime

st.set_page_config(
    page_title="Task 7 - 멀티페이지 대시보드",
    page_icon="📌",
    layout="wide",
    initial_sidebar_state="auto"
)

st.title("Task 7 : Streamlit 기본 기능 종합 + 멀티페이지 내비게이션")
st.write("아래 탭을 누르면 각 Task 페이지로 이동할 수 있습니다.")

st.divider()

# =====================================================
# ✅ 멀티페이지 탭 내비게이션
# =====================================================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    ["Task1 UI", "Task2 DataFrame/Metric", "Task3 Charts", "Task4 Filter", "Task5 Upload", "Task6 Layout"]
)

with tab1:
    st.subheader("Task 1: 기본 UI 컴포넌트")
    st.write("- text_input, select_slider, checkbox, button을 이용한 기본 입력 UI 실습")
    if st.button("➡ Task1 페이지 열기"):
        st.switch_page("task1.py")

with tab2:
    st.subheader("Task 2: 데이터프레임 & 지표 표시")
    st.write("- penguins.csv를 불러와 dataframe 출력 + metric으로 요약 지표 표시")
    if st.button("➡ Task2 페이지 열기"):
        st.switch_page("task2.py")

with tab3:
    st.subheader("Task 3: 차트 시각화")
    st.write("- line / bar / area / scatter 차트로 penguins 데이터 시각화")
    if st.button("➡ Task3 페이지 열기"):
        st.switch_page("task3.py")

with tab4:
    st.subheader("Task 4: 인터랙티브 필터")
    st.write("- selectbox로 카테고리를 선택해 필터링 후 bar_chart로 시각화")
    if st.button("➡ Task4 페이지 열기"):
        st.switch_page("task4.py")

with tab5:
    st.subheader("Task 5: CSV 업로드")
    st.write("- file_uploader로 CSV 올리면 상위 5행 미리보기")
    if st.button("➡ Task5 페이지 열기"):
        st.switch_page("task5.py")

with tab6:
    st.subheader("Task 6: 레이아웃 구성")
    st.write("- columns / tabs / expander로 레이아웃 대시보드 구성 실습")
    if st.button("➡ Task6 페이지 열기"):
        st.switch_page("pages/1_Task6_layout.py")

st.divider()

# =====================================================
# (기존 Task7 내용: 종합 기능 데모)
# =====================================================
st.header("Task 7 내부 데모 (기본 기능 한 화면에서 확인)")

# 1. TEXT / MARKDOWN / MESSAGE / IMAGE
st.subheader("1) TEXT / MARKDOWN / MESSAGE / IMAGE")

st.title('스트림릿 튜토리얼')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('Hello Streamlit')
st.markdown('### This is a Markdown')

st.error('This is an error')
st.warning('This is a warning')
st.info('This is a purely informational message')
st.success('This is a success message!')

try:
    img = Image.open("image.png")
    st.image(img, width=300, caption="Simple Image")
except Exception:
    st.info("image.png 파일이 없어서 이미지는 생략합니다.")

st.divider()

# 2. WRITE
st.subheader("2) WRITE")
st.write('Hello, Streamlit!')
st.write(['Hello', 'Streamlit', 'List'])

st.divider()

# 3. BUTTON / CHECKBOX / DATE
st.subheader("3) BUTTON / CHECKBOX / DATE")

if st.button('Say Hello'):
    st.write('Hello')
else:
    st.write('Goodbye')

if st.checkbox('Check me out'):
    st.write('Checked!')

d = st.date_input("생일 입력", value=datetime.date.today())
st.write("선택한 날짜:", d)

st.divider()

# 4. SESSION STATE
st.subheader("4) SESSION STATE")

if 'name' not in st.session_state:
    st.session_state['name'] = ''
if 'age' not in st.session_state:
    st.session_state['age'] = 0
if 'show_data' not in st.session_state:
    st.session_state['show_data'] = False

name_input = st.text_input("이름 입력", value=st.session_state['name'])
age_input = st.number_input("나이 입력", min_value=0, step=1, value=st.session_state['age'])

if st.button("저장 (세션 값)", key="save_session"):
    st.session_state['name'] = name_input
    st.session_state['age'] = age_input
    st.success("세션 스테이트에 값이 저장되었습니다!")

if st.button("저장된 값 보기", type="primary"):
    st.session_state['show_data'] = not st.session_state['show_data']

if st.session_state['show_data']:
    st.write(f"이름: {st.session_state['name']}")
    st.write(f"나이: {st.session_state['age']}")

if st.button("세션 초기화", key="reset_session"):
    st.session_state['name'] = ''
    st.session_state['age'] = 0
    st.session_state['show_data'] = False
    st.info("세션 스테이트가 초기화되었습니다.")

st.divider()

# 5. PROGRESS BAR
st.subheader("5) PROGRESS BAR")

if 'progress' not in st.session_state:
    st.session_state['progress'] = 0

progress_bar = st.progress(st.session_state['progress'])

if st.button("저장 (Progress)", key="save_progress"):
    if st.session_state['progress'] < 100:
        st.session_state['progress'] += 20
        progress_bar.progress(st.session_state['progress'])
    else:
        st.success("Progress Bar가 완료되었습니다!")

if st.button("초기화 (Progress)", key="reset_progress"):
    st.session_state['progress'] = 0
    progress_bar.progress(0)

st.write("---")

my_bar = st.progress(0)
if st.button("자동 진행 시작"):
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)

st.success("Task 7 : 멀티페이지 + 종합 기능 완료!")
