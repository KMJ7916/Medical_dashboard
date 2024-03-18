import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from unitest import *



# 한글폰트 경로 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
# Streamlit 앱의 제목 설정
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


# st.write("구분선")
# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["구분", "2018", "2019"])
# chart_data
# st.line_chart(chart_data)





