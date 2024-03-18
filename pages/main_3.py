import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 한글폰트 경로 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
st.page_link("main.py", label="Home", icon="🏠")
# Streamlit 앱의 제목 설정
st.title("특정지역 의료종사자 수")

# 데이터 가져오기
df = pd.read_csv("data_file/ttest.csv")
data_num_person = pd.read_excel("data_file/num_patients.xlsx")

# 데이터 정제
selected_columns = ["자치구별", "의사"]
df_selected = df[selected_columns]

# 데이터 분석
# 이 부분에서는 각 자치구별로 의사 수를 집계합니다.
df_analysis = df_selected.groupby("자치구별").sum().reset_index()

# 그래프 그리기
# 바 차트를 사용하여 각 자치구별 의사 수를 시각화합니다.
st.bar_chart(df_analysis.set_index("자치구별"))

st.title('Excel 데이터로 직선 그래프 그리기')

df = pd.read_excel('data_file/num_patients.xlsx', na_values='-')
title_font = {
    'fontsize': 10,
    'fontweight': 'bold',
    'family': 'Malgun Gothic'
}

# NaN 값을 0으로 대체합니다.
df.fillna(0, inplace=True)

# 데이터 확인
print(df.head())
# if st.button("Home"):
#     st.switch_page("your_app.py")
# matplotlib를 이용해 그래프를 생성합니다. 여기서는 첫 번째 열을 x축, 두 번째 열을 y축으로 사용합니다.
fig, ax = plt.subplots()
ax.plot(df.iloc[:,0], df.iloc[:,1])  # 첫 번째 열과 두 번째 열의 데이터를 사용합니다.
plt.xlabel('병원종류명')
plt.xticks(df.iloc[:,0], fontsize=5)  # x축 라벨
plt.ylabel('환자 수(단위:) ')  # y축 라벨
plt.title('Excel 데이터로 생성한 직선 그래프')  # 그래프 제목




# 생성한 그래프를 Streamlit 웹 애플리케이션에 표시합니다.
st.pyplot(fig)
# 만약 자세한 조정이 필요하다면, Matplotlib를 사용하여 그래프를 그리고
# Streamlit에서 그래프를 표시할 수 있습니다. 예를 들면 아래와 같습니다.

# fig, ax = plt.subplots()
# ax.bar(df_analysis["자치구별"], df_analysis["의사"])
# ax.set_xlabel("자치구별")
# ax.set_ylabel("의사 수")
# ax.set_title("자치구별 의료종사자(의사) 수")
# st.pyplot(fig)