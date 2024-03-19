import streamlit as st
import matplotlib.pyplot as plt
from select_region import *



# 한글폰트 경로 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
st.page_link("main.py", label="Home", icon="🏠")
st.header('의료인력 현황', divider="blue")


# 의료 종사자 수 가져오기
st.subheader("지역별 의료인력 표 🗃️")    
select_region()

st.write("")
st.write("")

st.subheader("지역별 의료인력 그래프 📊")
selected_columns = ["인력코드상위", "의사"]
df_selected = df[selected_columns]
st.bar_chart(df.set_index('지역')['의사'])






