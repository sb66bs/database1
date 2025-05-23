import streamlit as st
import pandas as pd
import mysql.connector

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("请先登录以访问此页面。")
    st.stop()

if "show_user" not in st.session_state:
    st.session_state.show_user = False
if "show_device" not in st.session_state:
    st.session_state.show_device = False
if "show_usage" not in st.session_state:
    st.session_state.show_usage = False
if "show_repair" not in st.session_state:
    st.session_state.show_repair = False
if "show_scrap" not in st.session_state:
    st.session_state.show_scrap = False

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123",
        database="demo",
    )
if st.button("查看用户数据"):
    st.session_state.show_user=not st.session_state.show_user
if st.session_state.show_user:
    conn=get_connection()
    df=pd.read_sql("SELECT *FROM user",conn)
    st.dataframe(df)
    conn.close()

if st.button("查看设备数据"):
    st.session_state.show_device=not st.session_state.show_device
if st.session_state.show_device:
    conn=get_connection()
    df=pd.read_sql("SELECT *FROM device",conn)
    st.dataframe(df)
    conn.close()

if st.button("查看设备使用记录"):
    st.session_state.show_usage = not st.session_state.show_usage
if st.session_state.show_usage:
    conn=get_connection()
    df=pd.read_sql("SELECT *FROM deviceusage",conn)
    st.dataframe(df)
    conn.close()


if st.button("查看设备修复记录"):
    st.session_state.show_repair= not st.session_state.show_repair
if st.session_state.show_repair:
    conn=get_connection()
    df=pd.read_sql("SELECT *FROM devicerepair",conn)
    st.dataframe(df)
    conn.close()


if st.button("查看设备报废记录"):
    st.session_state.show_scrap= not st.session_state.show_scrap
if st.session_state.show_scrap:
    conn=get_connection()
    df=pd.read_sql("SELECT *FROM devicescrap",conn)
    st.dataframe(df)
    conn.close()



