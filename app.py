import streamlit as st
import pandas as pd

# ==========================================
# 1. CẤU HÌNH & DỮ LIỆU
# ==========================================
st.set_page_config(page_title="Hệ thống mẫu in", layout="wide")

@st.cache_data
def load_dinh_muc():
    try:
        df = pd.read_excel("dinh_muc.xlsx")
        return pd.Series(df.Gia_Tri.values, index=df.Ten_Muc).to_dict()
    except:
        return {"Tiền ăn": 150000, "Phòng nghỉ": 350000}

DINH_MUC = load_dinh_muc()

# CSS ĐÃ CẢI TIẾN: KHÓA CHẾ ĐỘ IN TRIỆT ĐỂ
st.markdown("""
    <style>
    /* HIỂN THỊ TRÊN WEB */
    .vung-in-chuan {
        background: white; color: black; padding: 40px;
        border: 1px solid #eee; font-family: "Times New Roman", Times, serif;
        line-height: 1.5; margin-top: 20px;
    }
    table { width: 100%; border-collapse: collapse; margin-top: 15px; }
    th, td { border: 1px solid black; padding: 8px; text-align: center; color: black; }

    /* CHẾ ĐỘ IN (CTRL + P) */
    @media print {
        /* Ẩn mọi thành phần của giao diện Streamlit */
        div[data-testid="stToolbar"], 
        div[data-testid="stHeader"], 
        div[data-testid="stSidebar"], 
        footer, .stButton, .stForm, .stAlert, .stSpinner,
        [data-testid="stVerticalBlock"] > div:not(:has(.vung-in-chuan)) {
            display: none !important;
            height: 0; padding: 0; margin: 0;
        }

        /* Ép nội dung in tràn lề và nằm đầu trang */
        .main .block-container { padding: 0 !important; margin: 0 !important; }
        
        .vung-in-chuan {
            display: block !important;
            border: none !important;
            padding: 0 !important;
            margin: 0 !important;
            position: relative;
            width: 100% !important;
        }
        
        .title-in {
            display: block !important;
            text-align: center;
            text-transform: uppercase;
            font-size: 20pt;
            margin-bottom: 20px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. CÁC HÀM MẪU GIẤY
# ==========================================

def mau_giay_de_nghi_thanh_toan():
    st.header("Thiết lập: Giấy đề nghị thanh toán")
    with st.form("form_1"):
        ho_ten = st.text_input("Họ tên người đề nghị")
        noi_dung = st.text_area("Nội dung thanh toán")
        so_tien = st.number_input("Số tiền", min_value=0, step=1000)
        submitted = st.form_submit_button("XUẤT MẪU IN")

    if submitted:
        st.success("Đã tạo mẫu thành công! Nhấn Ctrl + P để in.")
        # Dùng unsafe_allow_html=True và đảm bảo không có ký tự lạ làm hỏng chuỗi HTML
        st.
