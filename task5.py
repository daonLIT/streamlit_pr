import streamlit as st
import pandas as pd

st.header("Task 5: CSV 파일 업로드 및 미리보기")

# 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

# 파일이 업로드된 경우
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.success("CSV 파일 업로드 완료!")

        # 데이터 상위 5행 미리보기
        st.subheader("📌 데이터 미리보기 (상위 5행)")
        st.write(df.head())


    except Exception as e:
        st.error("⚠ CSV 파일을 읽는 도중 오류가 발생했습니다.")
        st.error(e)
else:
    st.info("CSV 파일을 업로드하면 데이터 미리보기를 확인할 수 있습니다.")
