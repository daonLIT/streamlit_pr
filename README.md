# streamlit_pr

## 역할 분담

- 최다온: 데이터 표시하기(task 2), 차트 그리기(task 3)
- 유용우: 인터랙티브 필터(task 4)
- 김영우: 기본 UI 컴포넌트(task 1), 파일 업로드(task 5)
- 김재민: 레이아웃 구성(task 6), 종합 대시보드(task 7)


## 1. 프로젝트 개요

본 프로젝트는 Streamlit의 기본 기능을 단계별로 실습하기 위해 구성된
멀티페이지 웹 애플리케이션입니다. Task 1~6에서는 기능별 실습을
수행하고, Task 7에서는 모든 기능을 하나로 통합하여 대시보드 형태로
구현하였습니다.

- 목표
  1. Streamlit 기본 UI 컴포넌트 이해
  2. 데이터 로딩 및 요약 지표 출력
  3. 다양한 차트 시각화
  4. 인터랙티브 필터 및 파일 업로드 처리
  5. 레이아웃 구성과 멀티페이지 앱 설계 경험

## 2. 폴더 구조

    streamlit_pr/
     ├─ pages/
     │   ├─ 1_Task6_layout.py
     │   └─ 2_Task7_dashboard.py
     ├─ penguins.csv
     ├─ task1.py
     ├─ task2.py
     ├─ task3.py
     ├─ task4.py
     ├─ task5.py
     ├─ Task_Util.py
     ├─ requirements.txt
     └─ README.md

## 3. 기능 요약 (Task별 설명)


### **Task 1** --- 기본 UI 컴포넌트
- text_input, select_slider, checkbox, button을 이용해 사용자 입력 UI 구성
- 간단한 개인정보 입력 폼 형태로 동작
  
### **Task 2** --- 데이터프레임 & 지표(metric) 표시
- 파일을 불러와 전체 데이터프레임 표시
- 평균 체중/부리길이/부리두께 등 핵심 통계 정보를 metric으로 요약
  
### **Task 3** --- 차트 시각화
- line, bar, area, scatter 차트를 사용해 데이터를 다양한 관점에서 시각화
- 종별 평균 체중 비교 및 변수 관계 탐색 가능

### **Task 4** --- 인터랙티브 필터링
- selectbox로 카테고리를 선택하면 데이터가 즉시 필터링
- 필터 결과를 dataframe과 bar_chart로 동시에 확인

### **Task 5** --- CSV 업로드   
- file_uploader로 외부 CSV 파일 입력 가능
- 업로드 즉시 상위 5행을 출력하여 데이터 구조 확인

### **Task 6** --- 레이아웃 구성
- columns(좌/우 입력-상태 분리)
- tabs(기능별 화면 그룹화)
- expander(설명 접기/펼치기 UI)

### **Task 7** --- 종합 기능 + 멀티페이지 내비게이션
- Task1~6 내용을 한 페이지에서 다시 데모
- 상단 탭을 클릭하면 개별 Task 페이지로 이동하는 멀티페이지 내비게이션 제공
- 
## 4. 실행 방법

### 4.1 라이브러리 설치
``` bash
pip install -r requirements.txt
```

### 4.2 실행
```
streamlit run pages/2_Task7_dashboard.py
```


## 5. 사용 시나리오

1. 사용자는 Task7 메인 화면에 접속한다.
2. 탭에서 “Task2 DataFrame/Metric”을 선택해 데이터 요약을 확인한다.
3. “Task3 Charts” 탭으로 이동해 차트 기반 분석을 수행한다.
4. 필요하면 Task5에서 CSV 파일을 업로드해 자신의 데이터도 동일하게 미리보기/분석한다.
5. Task6로 이동해 레이아웃 구조를 참고하며 대시보드 설계를 학습한다.

