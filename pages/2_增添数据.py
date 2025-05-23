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

#用户数据
if "show_update_form" not in st.session_state:
    st.session_state["show_update_form"] = False
if st.button("添加用户数据"):
    st.session_state["show_update_form"] = not st.session_state["show_update_form"]

if st.session_state.show_update_form:
    user_id=st.number_input("用户id")
    user_name=st.text_input("姓名")
    user_department=st.text_input("所属部门")
    user_contact=st.text_input("联系方式")
    if st.button("确认"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            insert_sql = "INSERT INTO user (UserID,Name,Department,Contact) VALUES (%s,%s,%s,%s)"
            cursor.execute(insert_sql,(user_id,user_name,user_department,user_contact))
            conn.commit()

            if cursor.rowcount > 0:
                st.success(f"用户ID{user_id}信息已更新")
            else:
                st.warning("未找到该用户！")

            cursor.close()
            conn.close()
        except Exception as e:
            st.error(f"更新失败:{e}")

if "show_update_device_form" not in st.session_state:
    st.session_state["show_update_device_form"] = False

#设备数据
if st.button("添加设备数据"):
    st.session_state["show_update_device_form"] = not st.session_state["show_update_device_form"]

if st.session_state.show_update_device_form:
    device_id = st.number_input("设备ID")
    device_name = st.text_input("设备名称")
    device_model = st.text_input("设备型号")
    purchase_date = st.date_input("购买日期")
    purchase_cost = st.number_input("购买成本")
    device_status = st.text_input("设备状态")

    if st.button("确认"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            update_sql = "INSERT INTO device (DeviceID,DeviceName,Model,PurchaseDate,PurchaseCost,Status) VALUES (%s,%s,%s,%s%s)"
            cursor.execute(update_sql, (device_id,device_name, device_model, purchase_date, purchase_cost, device_status))
            conn.commit()

            if cursor.rowcount > 0:
                st.success(f"设备ID {device_id} 信息已更新")
            else:
                st.warning("未找到该设备！")

            cursor.close()
            conn.close()
        except Exception as e:
            st.error(f"更新失败: {e}")


#设备使用
if "show_update_use_form" not in st.session_state:
    st.session_state["show_update_use_form"] = False

if st.button("添加设备使用记录"):
    st.session_state["show_update_use_form"] = not st.session_state["show_update_use_form"]

if st.session_state.show_update_use_form:
    usage_id = st.number_input("使用记录ID")
    device_id = st.number_input("设备ID")
    user_id = st.number_input("用户ID")
    usage_date = st.date_input("使用日期")
    status = st.text_input("状态")

    if st.button("确认"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            update_sql = "INSERT INTO usage (UsageID,DeviceID,UserID,UsageDate,Status) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(update_sql, (usage_id,device_id, user_id, usage_date, status))
            conn.commit()

            if cursor.rowcount > 0:
                st.success(f"报废记录 UsageID {usage_id} 信息已更新")
            else:
                st.warning("未找到该报废记录！")

            cursor.close()
            conn.close()
        except Exception as e:
            st.error(f"更新失败: {e}")


#设备维修
if "show_repair_form" not in st.session_state:
    st.session_state["show_repair_form"] = False
if st.button("添加设备维修记录"):
    st.session_state["show_repair_form"] = not st.session_state["show_repair_form"]

if st.session_state.show_repair_form:
    repair_id = st.number_input("维修记录ID")
    device_id = st.text_input("设备ID")
    repair_date = st.date_input("维修日期")
    repair_content = st.text_input("维修内容")
    repair_Cost=st.number_input("维修花费")
    if st.button("确认"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            update_sql = "INSERT INTO devicerepair(ReapairID,DeviceID,RepairDate,RepairContent,RepairCost) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(update_sql, (device_id,repair_date, repair_content,repair_Cost, repair_id))
            conn.commit()

            if cursor.rowcount > 0:
                st.success(f"维修记录ID {repair_id} 信息已更新")
            else:
                st.warning("未找到该维修记录！")

            cursor.close()
            conn.close()
        except Exception as e:
            st.error(f"更新失败: {e}")

#设备报废
if "show_update_scrap_form" not in st.session_state:
    st.session_state["show_update_scrap_form"] = False

if st.button("添加报废记录"):
    st.session_state["show_update_scrap_form"] = not st.session_state["show_update_scrap_form"]

if st.session_state.show_update_scrap_form:
    scrap_id = st.number_input("报废记录")
    device_id = st.number_input("设备ID")
    scrap_date = st.date_input("报废日期")
    scrap_reason = st.text_area("报废原因")

    if st.button("确认"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            update_sql ="INSERT INTO devicescrap(ScrapID,DeviceID,ScrapDate,ScrapReason) VALUES (%s,%s,%s,%s)"
            cursor.execute(update_sql, (scrap_id,device_id, scrap_date, scrap_reason))
            conn.commit()

            if cursor.rowcount > 0:
                st.success(f"报废记录 ScrapID {scrap_id} 信息已更新")
            else:
                st.warning("未找到该报废记录！")

            cursor.close()
            conn.close()
        except Exception as e:
            st.error(f"更新失败: {e}")

