import streamlit as st
import pandas as pd

base = pd.read_csv("C:/Users/user/강동구청 인턴/test_dataset.csv")

Korea = base.loc[:,['Year', 'Population_K', 'Birth_K', 'Deaths_K']].dropna().set_index('Year')
Japan = base.loc[:,['Year', 'Population_J', 'Birth_J', 'Deaths_J']].dropna().set_index('Year')

with st.sidebar:
    select_menu = st.sidebar.selectbox('Menu', ['Dataset', 'Graph'])

select_data = st.selectbox('Country', ['Korea', 'Japan', 'United States', 'World'])
if (select_menu == 'Dataset') & (select_data == 'Korea'):
    st.title("Democracy of Korea")
    st.text("대한민국의 연도별 평균 인구수, 출생수, 사망수 데이터")
    st.dataframe(Korea)
    st.markdown("### Describe")
    st.table(Korea.describe())
elif (select_menu == 'Dataset') & (select_data == 'Japan'):
    st.title("Democracy of Japan")
    st.text("일본의 연도별 평균 인구수, 출생수, 사망수 데이터")
    st.dataframe(Japan)
    st.markdown("### Describe")
    st.table(Japan.describe())
elif (select_menu == 'Dataset') & (select_data == 'United States'):
    st.title("Democracy of United States")
    st.text("미국의 연도별 평균 인구수, 출생수, 사망수 데이터")
    st.text("구현중")
elif (select_menu == 'Dataset') & (select_data == 'World'):
    st.title("Democracy of World")
    st.text("전 세계의 연도별 평균 인구수 데이터")
    st.text("구현중")
else:
    st.markdown("## 대한민국 인구수 그래프")
    st.area_chart(Korea)