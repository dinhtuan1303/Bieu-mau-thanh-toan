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
        return {"Tiền ăn": 150000, "Phòng nghỉ": 350000}

DINH_MUC = load_dinh_muc()

# CSS NÂNG CAO ĐỂ KHÓA CHẾ ĐỘ IN (Đã sửa lỗi ẩn tiêu đề và dòng thừa)
st.markdown("""
    <style>
    /* CSS HIỂN THỊ TRÊN WEB */
    .vung-in-chuan {
        background: white; color: black; padding: 40px;
        border: 1px solid #eee; font-family: "Times New Roman", serif;
        line-height: 1.5; margin-top: 20px;
    }
    table { width: 100%; border-collapse: collapse; margin-top: 15px; }
    th, td { border: 1px solid black; padding: 8px; text-align: center; color: black; }

    /* CSS CHO CHẾ ĐỘ IN (CTRL + P) */
    @media print {
        /* 1. Ẩn toàn bộ các phần tử mặc định của Streamlit và các ô nhập liệu */
        header, footer, .stSidebar, .stButton, .stForm, .stAlert,
        [data-testid="stHeader"], [data-testid="stDecoration"], [data-testid="stToolbar"],
        div[data-testid="stVerticalBlock"] > div:not(:has(.vung-in-chuan)) {
            display: none !important;
            height: 0; padding: 0; margin: 0;
        }

        /* 2. Ép buộc vùng in hiển thị đúng định dạng */
        .vung-in-chuan {
            display: block !important;
            position: absolute; top: 0; left: 0; width: 100%;
            border: none !important; padding: 0 !important; margin: 0 !important;
        }

        /* 3. Đảm bảo tiêu đề in luôn hiện */
        .title-in {
            display: block !important;
            text-align: center; text-transform: uppercase;
            font-size: 20pt; font-weight: bold; margin-bottom: 20px;
        }

        /* 4. Xóa lề mặc định của Streamlit */
        .main .block-container { padding: 0 !important; margin: 0 !important; }
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. CÁC HÀM MẪU GIẤY (Đã sửa lỗi hiển thị HTML)
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
        # CHÚ Ý: Không thụt đầu dòng các thẻ HTML để tránh lỗi hiển thị code nguyên bản
        html_output = f"""<div class="vung-in-chuan">
<h2 class="title-in">GIẤY ĐỀ NGHỊ THANH TOÁN</h2>
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
</div>"""
        st.markdown(html_output, unsafe_allow_html=True)

def mau_bang_ke_cong_tac_phi
