import streamlit as st
from PIL import Image
import time

st.set_page_config(
    page_title="Task 7 - 종합 기능",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="auto"
)

st.title("Task 7 : Streamlit 기본 기능 종합 예제")

# =====================================================
# 1. INPUT - TEXT  (타이틀, 헤더, 텍스트, 마크다운, 메시지박스, 이미지)
# =====================================================
st.header("1) INPUT - TEXT")

# 타이틀/헤더/서브헤더/텍스트/마크다운
st.title('스트림릿 튜토리얼')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('Hello Streamlit')
st.markdown('### This is a Markdown')

# 메시지 박스
st.error('This is an error')
st.warning('This is a warning')
st.info('This is a purely informational message')
st.success('This is a success message!')

# 이미지 (image.png가 같은 폴더에 있을 때)
try:
    img = Image.open("image.png")
    st.image(img, width=300, caption="Simple Image")
except Exception:
    st.info("image.png 파일이 없어서 이미지는 생략합니다.")

st.divider()

# =====================================================
# 2. INPUT - WRITE  (텍스트, 리스트 출력)
# =====================================================
st.header("2) INPUT - WRITE")

st.write('Hello, Streamlit!')
st.write(['Hello', 'Streamlit', 'List'])   # 리스트 출력 예제

st.divider()

# =====================================================
# 3. INPUT - BUTTON & CHECKBOX & DATE
# =====================================================
st.header("3) INPUT - BUTTON / CHECKBOX / DATE")

# 버튼 기본 예제
st.subheader("버튼 예제")

if st.button('Say Hello'):
    st.write('Hello')
else:
    st.write('Goodbye')

st.write("---")

# 체크박스 예제
st.subheader("체크박스 예제")

if st.checkbox('Check me out'):
    st.write('Checked!')

st.write("---")

# 날짜 입력 예제
st.subheader("날짜 입력 예제 (DATE INPUT)")
d = st.date_input(
    "생일 입력",
    min_value=None,
    max_value=None
)
st.write("선택한 날짜:", d)

st.divider()

# =====================================================
# 4. STATE - SESSION STATE  (이름/나이 저장 & 보기)
# =====================================================
st.header("4) STATE - SESSION STATE")

# 세션 스테이트 초기화
if 'name' not in st.session_state:
    st.session_state['name'] = ''
if 'age' not in st.session_state:
    st.session_state['age'] = 0
if 'show_data' not in st.session_state:
    st.session_state['show_data'] = False

st.write("이름과 나이를 입력하고, 버튼을 눌러 세션 스테이트에 저장합니다.")

# 입력 위젯
name_input = st.text_input("이름 입력", value=st.session_state['name'])
age_input = st.number_input("나이 입력", min_value=0, step=1, value=st.session_state['age'])

# 입력한 값을 세션 스테이트에 저장
if st.button("저장 (세션 값)", key="save_session"):
    st.session_state['name'] = name_input
    st.session_state['age'] = age_input
    st.success("세션 스테이트에 값이 저장되었습니다!")

# 보기 버튼 (토글)
if st.button("저장된 값 보기", type="primary"):
    st.session_state['show_data'] = not st.session_state['show_data']

# 저장된 값 보기
if st.session_state['show_data']:
    st.write("### 현재 세션 스테이트 값")
    st.write(f"이름: {st.session_state['name']}")
    st.write(f"나이: {st.session_state['age']}")

# 세션 초기화 버튼
if st.button("세션 초기화", key="reset_session"):
    st.session_state['name'] = ''
    st.session_state['age'] = 0
    st.session_state['show_data'] = False
    st.info("세션 스테이트가 초기화되었습니다.")

st.divider()

# =====================================================
# 5. STATE - PROGRESS BAR (세션 연동 + 시간 진행)
# =====================================================
st.header("5) STATE - PROGRESS BAR")

# progress 값이 세션에 없으면 초기화
if 'progress' not in st.session_state:
    st.session_state['progress'] = 0

# Progress Bar 생성
progress_bar = st.progress(st.session_state['progress'])

st.write("저장 버튼을 누를 때마다 Progress Bar가 20씩 증가합니다.")

# 입력 값에 맞춰 Progress Bar 증가
if st.button("저장 (Progress)", key="save_progress"):
    if st.session_state['progress'] < 100:
        st.session_state['progress'] += 20  # Progress 증가
        progress_bar.progress(st.session_state['progress'])
        st.info(f"'저장' 버튼을 {5 - st.session_state['progress'] // 20}번 더 눌러야 완료됩니다.")
    else:
        st.success("Progress Bar가 완료되었습니다! 값이 저장되었습니다.")

# Progress 초기화
if st.button("초기화 (Progress)", key="reset_progress"):
    st.session_state['progress'] = 0
    progress_bar.progress(0)
    st.info("세션 스테이트가 초기화되었습니다.")

st.write("---")

st.subheader("시간에 따라 자동으로 증가하는 Progress Bar")

my_bar = st.progress(0)
if st.button("자동 진행 시작"):
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)

st.success(" Task 7 :  종합 기능!")
