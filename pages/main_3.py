import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 한글폰트 경로 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
st.page_link("main.py", label="Home", icon="🏠")


st.header("환자 수 통계", divider="blue")
st.subheader('종별 환자 수 그래프 📊')

# 데이터 가져오기
df = pd.read_excel("data_file/num_patients.xlsx")
data_num_person = pd.read_excel("data_file/num_patients.xlsx")


df_analysis = df.groupby("구분").sum().reset_index()
data = pd.read_excel("data_file/num_patients.xlsx")
df = pd.DataFrame(data)


#-------------------------------------------------------- okay
# x = df['구분']  # 예시로 '시간' 열을 x축 데이터로 사용
# y = df['2018년']  # 예시로 '온도' 열을 y축 데이터로 사용

# # 그래프 생성
# plt.figure(figsize=(10, 6))  # 그래프 크기 설정
# plt.plot(x, y)  # x와 y 데이터를 이용해 선 그래프 생성
# plt.title("Temperature Over Time")  # 그래프 제목 설정
# plt.xlabel("Time")  # x축 라벨 설정
# plt.ylabel("Temperature")  # y축 라벨 설정

# st.pyplot(plt)
#--------------------------------------------------------------------------------------
columns_without = [col for col in df.columns if col != '구분']


selected_columns = st.multiselect('그래프에 표시할 데이터 선택', columns_without)


if len(selected_columns) > 0:
    selected_data = df[selected_columns]
    
    
    plt.figure(figsize=(10, 6))
    
    for column in selected_columns:
        plt.plot(df.index, df[column], label=column)
    
    plt.title("Selected Data Graph")
    plt.xlabel("Index")
    plt.ylabel("환자수 (단위: 천명)")
    plt.legend()
    st.pyplot(plt)
else:
    st.write("데이터를 선택해주세요.")

df