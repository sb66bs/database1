import streamlit as st

# 设置页面标题
st.set_page_config(page_title="设备管理数据库", page_icon="🔐")

id="admin"
ps="123456"

if "logged_in"not in st.session_state:
    st.session_state["logged_in"]=False

def log_in():
    UID=st.text_input("账号")
    UPS=st.text_input("密码",type="password")

    if st.button("登录"):
        if UID==id and UPS==ps:
            st.session_state["logged_in"]=True
            st.success("登录成功！请在左侧栏选择页面。")
        else:
            st.error("账号或密码错误，请重试。")

if not st.session_state["logged_in"]:
    st.title("请登录以访问内容")
    log_in()
else:
    st.title("您已登录")
    st.sidebar.success("欢迎！你现在可以访问左侧导航的页面了。")











