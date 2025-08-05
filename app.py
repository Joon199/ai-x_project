#web content/UI/UX Desgin/Box/Message
#html + Python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('./data/mydata.csv')

#global variable
url = 'https://www.youtube.com/watch?v=5lLuyGclDCg'


st.title('This is my first webapp!')
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('SubContent1...'):
        st.subheader('SubContent1')
        st.video(url)
    with st.expander('SubContent2...'):
        st.subheader('image Content...')
        st.image('./images/catdog.jpg')

    with st.expander('SubContent3...'):
        st.subheader('HTML Content...')
        import streamlit.components.v1 as htmlviewer
        with open('./htmls/index.html','r',encoding='utf-8') as f:
            html1 = f.read()
            f.close()
        htmlviewer.html(html1,height=800)

    with st.expander('SubContent4...'):
        st.subheader('Data App Content...')
        st.table(df)
        st.write(df.describe())
        fig, ax = plt.subplots(figsize=(20,10))
        df.plot(ax=ax)
        plt.savefig('./images/mygraph.png')
        st.image('./images/mygraph.png')
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

with col2:
    with st.expander('Tips...'):
        st.info('Tips........')
    with st.expander('Tips....'):
        st.info('Tips.....')
        
