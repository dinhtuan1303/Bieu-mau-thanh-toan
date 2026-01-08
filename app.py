import streamlit as st
import pandas as pd

# ==========================================
# 1. CẤU HÌNH HỆ THỐNG
# ==========================================
st.set_page_config(page_title="Hệ thống in Giấy đề nghị thanh toán", layout="wide")

# CSS để định dạng bản in chuyên nghiệp
st.markdown("""
    <style>
    .vung-in-chuan {
        background: white; color: black; padding: 30px;
        border: 1px solid #ddd; font-family: "Times New Roman", Times, serif;
        line-height: 1.4; font-size: 13pt;
    }
    .header-table { width: 100%; border: none !important; margin-bottom: 10px; }
    .header-table td { border: none !important; text-align: center; vertical-align: top; padding: 0; color: black; }
    
    @media print {
        header, footer, .stSidebar, .stButton, .stForm, .stAlert,
        [data-testid="stHeader"], [data-testid="stToolbar"],
        div[data-testid="stVerticalBlock"] > div:not(:has(.vung-in-chuan)) {
            display: none !important;
        }
        .main .block-container { padding: 0 !important; margin: 0 !important; }
        .vung-in-chuan { display: block !important; border: none !important; width: 100%; padding: 0; }
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. HÀM XỬ LÝ MẪU IN
# ==========================================

def mau_giay_de_nghi_thanh_toan():
    st.subheader("⚙️ Nhập thông tin Giấy đề nghị thanh toán")
    
    with st.form("form_qnu"):
        c1, c2 = st.columns(2)
        with c1:
            ten_dv = st.text_input("Tên đơn vị", "TRƯỜNG ĐẠI HỌC QUY NHƠN")
            ma_dv = st.text_input("Mã ĐVCQHVNS", "1055595")
            ho_ten = st.text_input("Họ tên người đề nghị")
            dv_cong_tac = st.text_input("Đơn vị công tác")
        with c2:
            dia_danh = st.text_input("Địa danh", "Gia Lai")
            chuc_vu = st.text_input("Chức vụ")
            stk = st.text_input("Số tài khoản")
            ngan_hang = st.text_input("Tại ngân hàng")
            
        noi_dung = st.text_area("Nội dung thanh toán")
        so_tien = st.number_input("Số tiền đề nghị (VNĐ)", min_value=0, step=1000)
        bang_chu = st.text_input("Bằng chữ")
        kem_theo = st.text_input("Số chứng từ gốc kèm theo", "0")
        
        submitted = st.form_submit_button("⚡ TẠO MẪU IN")

    if submitted:
        st.success("Đã tạo mẫu thành công! Nhấn Ctrl + P để in.")
        
        # Căn lề sát trái cho chuỗi f-string để tránh lỗi thụt lề và đóng nháy kép ở cuối
        html_output = f"""<div class="vung-in-chuan">
<table class="header-table">
    <tr>
        <td style="width: 45%; text-align: left;">
            <b>{ten_dv.upper()}</b><br>
            Mã ĐVCQHVNS: {ma_dv}
        </td>
        <td style="width: 55%;">
            <b>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</b><br>
            <b>Độc lập - Tự do
