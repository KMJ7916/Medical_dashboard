import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from select_region import *

# 한글폰트 경로 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
st.page_link("main.py", label="Home", icon="🏠")


st.header("환자 수 통계", divider="blue")
st.subheader('종별 환자 수 그래프 📊')

# 데이터 가져오기
df = pd.read_excel("data_file/num_patients.xlsx")


df_analysis = df.groupby("구분").sum().reset_index()
data = pd.read_excel("data_file/num_patients.xlsx")
df = pd.DataFrame(data)

# "-" 문자를 NaN으로 변환
df = df.replace('-', np.nan)

# 문자열을 숫자로 변환 (변환할 수 없는 값은 NaN으로 처리)
for col in df.columns[1:]:  # '구분' 열을 제외하고 변환
    df[col] = pd.to_numeric(df[col], errors='coerce')

# '구분' 열을 제외한 열 목록 생성
columns_without = [col for col in df.columns if col != '구분']

# 수정된 열 목록을 multiselect의 옵션으로 사용
selected_columns = st.multiselect('그래프에 표시할 데이터 선택', columns_without)

# 선택된 열이 있을 경우에만 그래프를 그림
if len(selected_columns) > 0:
    selected_data = df[selected_columns]
    
    # 그래프 생성
    plt.figure(figsize=(10, 6))
    
    for column in selected_columns:
        plt.plot(df.index, df[column], label=column)
    
    plt.title("Selected Data Graph")
    plt.xlabel("Index")
    plt.ylabel("환자수(단위: 천명)")
    plt.legend()
    st.pyplot(plt)
else:
    st.write("데이터를 선택해주세요.")

df