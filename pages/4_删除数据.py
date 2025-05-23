import streamlit as st
import mysql.connector


if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("请先登录以访问此页面。")
    st.stop()

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='123',
        database='demo'
    )

if "show_delete_user_form" not in st.session_state:
    st.session_state["show_delete_user_form"] = False

if st.button("删除用户数据"):
    st.session_state["show_delete_user_form"] = not st.session_state["show_delete_user_form"]

if st.session_state.show_delete_user_form:
    user_id = st.number_input("用户ID")
    if st.button("确认"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            delete_sql = "DELETE FROM user WHERE UserID=%s"
            cursor.execute(delete_sql, (user_id,))
            conn.commit()

            if cursor.rowcount > 0:
                st.success(f"用户ID {user_id} 已删除")
            else:
                st.warning("未找到该用户！")

            cursor.close()
            conn.close()
        except Exception as e:
            st.error(f"删除失败: {e}")

if "show_delete_device_form" not in st.session_state:
    st.session_state["show_delete_device_form"] = False

if st.button("删除设备数据"):
    st.session_state["show_delete_device_form"] = not st.session_state["show_delete_device_form"]

if st.session_state.show_delete_device_form:
    device_id = st.number_input("设备ID")
    if st.button("确认"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            delete_sql = "DELETE FROM device WHERE DeviceID=%s"
            cursor.execute(delete_sql, (device_id,))
            conn.commit()

            if cursor.rowcount > 0:
                st.success(f"设备ID {device_id} 已删除")
            else:
                st.warning("未找到该设备！")

            cursor.close()
            conn.close()
        except Exception as e:
            st.error(f"删除失败: {e}")

if "show_delete_use_form" not in st.session_state:
    st.session_state["show_delete_use_form"] = False

if st.button("删除设备使用记录"):
    st.session_state["show_delete_use_form"] = not st.session_state["show_delete_use_form"]

if st.session_state.show_delete_use_form:
    usage_id = st.number_input("使用记录ID")
    if st.button("确认"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            delete_sql = "DELETE FROM devicescrap WHERE UsageID=%s"
            cursor.execute(delete_sql, (usage_id,))
            conn.commit()

            if cursor.rowcount > 0:
                st.success(f"使用记录 UsageID {usage_id} 已删除")
            else:
                st.warning("未找到该使用记录！")

            cursor.close()
            conn.close()
        except Exception as e:
            st.error(f"删除失败: {e}")

if "show_delete_repair_form" not in st.session_state:
    st.session_state["show_delete_repair_form"] = False

if st.button("删除设备维修记录"):
    st.session_state["show_delete_repair_form"] = not st.session_state["show_delete_repair_form"]

if st.session_state.show_delete_repair_form:
    repair_id = st.number_input("维修记录ID")
    if st.button("确认"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            delete_sql = "DELETE FROM devicerepair WHERE RepairID=%s"
            cursor.execute(delete_sql, (repair_id,))
            conn.commit()

            if cursor.rowcount > 0:
                st.success(f"维修记录 RepairID {repair_id} 已删除")
            else:
                st.warning("未找到该维修记录！")

            cursor.close()
            conn.close()
        except Exception as e:
            st.error(f"删除失败: {e}")

if "show_delete_scrap_form" not in st.session_state:
    st.session_state["show_delete_scrap_form"] = False

if st.button("删除报废记录"):
    st.session_state["show_delete_scrap_form"] = not st.session_state["show_delete_scrap_form"]

if st.session_state.show_delete_scrap_form:
    scrap_id = st.number_input("报废记录ID")
    if st.button("确认"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            delete_sql = "DELETE FROM devicescrap WHERE ScrapID=%s"
            cursor.execute(delete_sql, (scrap_id,))
            conn.commit()

            if cursor.rowcount > 0:
                st.success(f"报废记录 ScrapID {scrap_id} 已删除")
            else:
                st.warning("未找到该报废记录！")

            cursor.close()
            conn.close()
        except Exception as e:
            st.error(f"删除失败: {e}")
