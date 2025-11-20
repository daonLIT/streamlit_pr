import streamlit as st
import pandas as pd
import numpy as np

# --- Task 4: 인터랙티브 필터 ---
st.header("Task 4: 인터랙티브 필터")

# 1. 실습용 샘플 데이터 생성 (데이터프레임)
# 실제 파일이 있다면 pd.read_csv('파일경로')를 사용.
df = pd.DataFrame({
    'category': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A'],
    'value': [10, 20, 30, 15, 25, 35, 40, 10, 20, 30],
    'date': pd.date_range(start='2024-01-01', periods=10)
})

st.subheader("데이터 필터링 및 시각화")

# 2. 카테고리 선택 박스 생성 (UI)
# '전체' 옵션을 맨 앞에 추가하고, 그 뒤에 데이터에 있는 고유 카테고리들을 붙입니다.
category_list = ['전체'] + sorted(df['category'].unique().tolist())
selected_category = st.selectbox("카테고리 선택", category_list)

# 3. 데이터 필터링 로직
if selected_category == '전체':
    filtered_df = df  # 전체 선택 시 원본 데이터 유지
else:
    filtered_df = df[df['category'] == selected_category] # 선택된 카테고리만 필터링

# 4. 결과 화면 출력
st.write(f"필터링된 결과 (선택값: **{selected_category}**)")

# 데이터프레임 표시 (Task 2 기능 활용)
st.dataframe(filtered_df)

# 차트 그리기 (Task 3 기능 활용 - 바 차트 예시)
# 차트를 그릴 때는 수치형 데이터를 보여주는 것이 일반적입니다.
st.bar_chart(filtered_df.set_index('date')['value'])