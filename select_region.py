import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_excel("data_file/medical_person.xlsx")

# 지역을 선택하면 해당 지역 의료종사자 수 파악 가능
def select_region():
    option = st.selectbox(
        "지역을 선택해주세요.",
        ("전체", "서울", "부산", "인천", "대구", "광주", "대전", "울산", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "세종", "제주"),
        index=None,
        placeholder=""
    )

    if option == "전체":
        st.write(df)
    else:
        region_row = df[df['지역'] == option]
        if not region_row.empty: # 데이터 확인하고 해당하는 행만 필터링하여 출력
            st.write(region_row)
        else:
            st.write("선택된 지역이 없거나 데이터가 없습니다.")
    
    