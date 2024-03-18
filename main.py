import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




st.title(":house:")
st.header('의료현황을 알 수 있는 대시보드', divider="blue")
st.write("")

st.page_link("pages/main_2.py", label="의료인력 현황", icon="🩺")
st.write("")
st.page_link("pages/main_3.py", label="환자 수 통계", icon="🛌")

base_position =  [37.5073423, 127.0572734]
#중심점의 위도, 경도 좌표를 리스트에 담습니다.

# base_position에, 랜덤으로 생성한 값을 더하여 5개의 좌표를 데이터 프레임으로 생성하였고,
# 컬럼명은 위도 :lat  경도 lon으로 지정하였습니다. 


map_data = pd.DataFrame(
    np.random.randn(5, 1) / [20, 20] + base_position , 
    columns=['lat', 'lon'])
# map data 생성 : 위치와 경도 

print(map_data)

# df3 = pd.read_excel("Hospital_location.xlsx")

# st.map(df3)
#st.page_link("http://www.google.com", label="Google", icon="🌎")
