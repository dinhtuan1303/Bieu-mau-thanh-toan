import pandas as pd
import streamlit as st

@st.cache_data
def load_phong_ban():
    try:
        # Đọc sheet 'PhongBan' trong file excel
        df = pd.read_excel("data/danh_muc.xlsx", sheet_name="PhongBan")
        return df['TenPhong'].tolist()
    except:
        return ["Phòng Đào tạo", "Phòng Kế hoạch", "Phòng Tổ chức"]

@st.cache_data
def load_dinh_muc():
    try:
        df = pd.read_excel("data/danh_muc.xlsx", sheet_name="DinhMuc")
        return dict(zip(df['LoaiChi'], df['DonGia']))
    except:
        return {"Tiền ăn": 150000, "Công tác phí": 200000}