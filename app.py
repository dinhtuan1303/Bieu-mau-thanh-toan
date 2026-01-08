import streamlit as st
import pandas as pd

# ==========================================
# 1. CẤU HÌNH & DỮ LIỆU
# ==========================================
st.set_page_config(page_title="Hệ thống mẫu in", layout="wide")

@st.cache_data
def load_dinh_muc():
    try:
        # Đảm bảo file dinh_muc.xlsx có 2 cột: Ten_Muc và Gia_Tri
        df = pd.read_excel("dinh_muc.xlsx")
        return pd.Series(df.Gia_Tri.values, index=df.Ten_Muc).to_dict()
    except:
        return {"Tiền ăn": 150000, "Phòng nghỉ": 350000, "Phụ cấp lưu trú": 300000}

DINH_MUC = load_dinh_muc()

# CSS ĐỂ XỬ LÝ GIAO DIỆN IN (ẨN CÁC PHẦN THỪA)
st.markdown("""
    <style>
    .vung-in-chuan {
        background: white; color: black; padding: 40px;
        border: 1px solid #eee; font-family: "Times New Roman", serif;
        line-height: 1.5;
    }
    table { width: 100%; border-collapse: collapse; margin-top: 15px; }
    th, td { border: 1px solid black; padding: 8px; text-align: center; color: black; }
    
    @media print {
        header, footer, .stSidebar, .stButton, .stForm, .stAlert,
        [data-testid="stHeader"], [data-testid="stToolbar"],
        div[data-testid="stVerticalBlock"] > div:not(:has(.vung-in-chuan)) {
            display: none !important;
        }
        .vung-in-chuan { display: block !important; width: 100%; }
        .main .block-container { padding: 0 !important; }
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
        # Dùng chuỗi f-string và hiển thị bằng st.markdown với unsafe_allow_html=True
        html_output = f"""
        <div class="vung-in-chuan">
            <h2 style="text-align: center; text-transform: uppercase;">GIẤY ĐỀ NGHỊ THANH TOÁN</h2>
            <p style="text-align: center;"><i>Ngày {pd.Timestamp.now().day} tháng {pd.Timestamp.now().month} năm {pd.Timestamp.now().year}</i></p>
            <br>
            <p><b>Kính gửi:</b> Ban Lãnh đạo đơn vị</p>
            <p>Họ và tên người đề nghị: {ho_ten}</p>
            <p>Nội dung thanh toán: {noi_dung}</p>
            <p>Số tiền đề nghị: <b>{so_tien:,.0f} VNĐ</b></p>
            <p><i>(Bằng chữ: ....................................................................)</i></p>
            <br><br>
            <div style="display: flex; justify-content: space-around;">
                <div style="text-align: center;"><b>Người đề nghị</b><br><br><br><br><b>{ho_ten}</b></div>
                <div style="text-align: center;"><b>Kế toán trưởng</b><br><br><br><br>...........................</div>
            </div>
        </div>
        """
        st.markdown(html_output, unsafe_allow_html=True)

def mau_bang_ke_cong_tac_phi(): # Đã sửa: Thêm dấu ngoặc đơn ()
    st.header("Thiết lập: Bảng kê công tác phí")
    if 'rows_ctp' not in st.session_state:
        st.session_state.rows_ctp = [{"loai": list(DINH_MUC.keys())[0], "sl": 1}]

    for i, row in enumerate(st.session_state.rows_ctp):
        c1, c2, c3 = st.columns([3, 1, 1])
        with c1: st.session_state.rows_ctp[i]['loai'] = st.selectbox(f"Khoản chi {i+1}", list(DINH_MUC.keys()), key=f"l_{i}")
        with c2: st.session_state.rows_ctp[i]['sl'] = st.number_input(f"SL {i+1}", min_value=
