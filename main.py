import streamlit as st

st.title(":house:")
st.header('의료현황을 알 수 있는 대시보드', divider="blue")

st.write("")
st.page_link("pages/main_2.py", label="의료인력 현황", icon="🩺")
st.write("• 지역과 종별로 나타낸 의료인력 데이터를 이용하여 그래프와 표를 나타내었습니다.")
st.write("")
st.page_link("pages/main_3.py", label="환자 수 통계", icon="🛌")
st.write("• 종별로 나타낸 환자 수 데이터를 이용하여 그래프와 표를 나타내었습니다.")