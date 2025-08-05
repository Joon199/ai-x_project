
import streamlit as st
import plotly.express as px
import pandas as pd
from io import StringIO

# Streamlit 페이지 설정
st.set_page_config(page_title="Student Grades Visualization", layout="wide")

# 앱 제목
st.title("Student Grades Visualization App")
st.markdown("Upload a CSV file or use the default data to visualize student grades.")

# 기본 데이터
default_data = """name,grade,number,kor,eng,math,info
lee2,1,90,91,81,100
park,2,2,88,89,77,100
kim,2,3,99,99,99,100"""

# CSV 파일 업로드
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# 데이터 로드
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv(StringIO(default_data))

# 데이터 표시
st.subheader("Dataset")
st.dataframe(df)

# 시각화 섹션
st.subheader("Visualizations")

# 1. 과목별 점수 막대 그래프
st.write("### Subject Scores by Student")
fig_bar = px.bar(
    df.melt(id_vars=["name"], value_vars=["kor", "eng", "math", "info"], 
            var_name="Subject", value_name="Score"),
    x="name", y="Score", color="Subject", barmode="group",
    title="Subject Scores by Student",
    color_discrete_map={"kor": "#1f77b4", "eng": "#ff7f0e", "math": "#2ca02c", "info": "#d62728"}
)
fig_bar.update_layout(xaxis_title="Student", yaxis_title="Score", legend_title="Subject")
st.plotly_chart(fig_bar, use_container_width=True)

# 2. 학년과 번호 기반 산점도
st.write("### Grade vs. Number with Score Size")
fig_scatter = px.scatter(
    df, x="grade", y="number", size="kor", color="name",
    hover_data=["kor", "eng", "math", "info"],
    title="Grade vs. Number (Size: Korean Score)",
    color_discrete_map={"lee2": "#1f77b4", "park": "#ff7f0e", "kim": "#2ca02c"}
)
fig_scatter.update_layout(xaxis_title="Grade", yaxis_title="Number", legend_title="Student")
st.plotly_chart(fig_scatter, use_container_width=True)

# 3. 평균 점수 파이 차트
st.write("### Average Score by Student")
df["avg_score"] = df[["kor", "eng", "math", "info"]].mean(axis=1)
fig_pie = px.pie(
    df, names="name", values="avg_score",
    title="Average Score Distribution",
    color_discrete_map={"lee2": "#1f77b4", "park": "#ff7f0e", "kim": "#2ca02c"}
)
st.plotly_chart(fig_pie, use_container_width=True)

# 추가 정보
st.markdown("""
### About
This app visualizes student grades using Plotly Express in a Streamlit web application. 
Upload a CSV file with columns: name, grade, number, kor, eng, math, info, or use the default dataset.
- **Bar Chart**: Compares scores across subjects for each student.
- **Scatter Plot**: Shows grade vs. number with Korean score as size.
- **Pie Chart**: Displays the distribution of average scores.
""")