import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

# 设置页面标题
st.set_page_config(page_title="❤️ 爱妮 ❤️", layout="wide", page_icon="❤️")

# 创建爱心形状
def create_heart():
    t = np.linspace(0, 2*np.pi, 1000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

# 绘制爱心
def plot_heart():
    x, y = create_heart()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(x, y, color='red', linewidth=3)
    ax.fill(x, y, color='pink', alpha=0.5)
    ax.axis('equal')
    ax.axis('off')
    st.pyplot(fig)

# 主页面布局
# st.title("")
# st.write("")

# 创建两列布局
col = st.columns([2, 1, 2])

with col[0]:
    plot_heart()

with col[2]:
    st.write("")
    st.write("亲爱的，亚妮")
    st.write("")
    st.write("有妮在好开心！")
    st.write("妮好可爱！")
    st.write("时长会想妮在干嘛！")
    st.write("")
    st.write("爱妮的云☁️")

# 添加一些交互元素
st.write("")
st.write("")
st.write("请告诉我你的感受:")
feeling = st.selectbox("", ["非常喜欢", "喜欢"])
if st.button("提交"):
    st.success(f"谢谢你选择了 '{feeling}'！")

print("表白网站代码已生成，可以运行streamlit应用。")