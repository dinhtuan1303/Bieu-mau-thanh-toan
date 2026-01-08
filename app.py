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

# CSS NÂNG CAO ĐỂ KHÓA CHẾ ĐỘ IN
st.markdown("""
    <style>
    /* CSS CHO MÀN HÌNH WEB */
    .vung-in-chuan {
        background: white; color: black; padding: 40px;
        border: 1px solid #eee; font-family: "Times New Roman", serif;
        line-height: 1.5; margin-top: 20px;
    }
    table { width: 100%; border-collapse: collapse; margin-top: 15px; }
    th, td { border: 1px solid black; padding: 8px; text-align: center; }

    /* CSS CHO CHẾ ĐỘ IN (CTRL + P) */
    @media print {
        /* 1. Ẩn toàn bộ các phần tử mặc định của Streamlit */
        div[data-testid="stToolbar"], 
        div[data-testid="stHeader"], 
        div[data-testid="stSidebar"], 
        footer, 
        .stButton, 
        .stForm, 
        .stAlert, 
        .stMarkdown h1, 
        .stMarkdown h2:not(.title-in),
        div[data-testid="stVerticalBlock"] > div:not(:has(.vung-in-chuan)) {
            display: none !important;
        }

        /* 2. Ép buộc chỉ hiển thị vùng in */
        .vung-in-chuan {
            display: block !important;
            position: absolute;
            top: 0; left: 0; width: 100%;
            border: none !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        /* 3. Xóa khoảng trắng lề của Streamlit */
        .main .block-container {
            padding: 0 !important;
            margin: 0 !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. CÁC HÀM MẪU GIẤY (Đã sửa logic Title)
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
        # Tiêu đề GIẤY ĐỀ NGHỊ... phải nằm TRONG div vung-in-chuan
        st.markdown(f"""
        <div class="vung-in-chuan">
            <h2 class="title-in" style="text-align: center; text-transform: uppercase;">Giấy đề nghị thanh toán</h2>
            <br>
            <p><b>Kính gửi:</b> Ban Lãnh đạo đơn vị</p>
            <p>Họ và tên người đề nghị: {ho_ten}</p>
            <p>Nội dung thanh toán: {noi_dung}</p>
            <p>Số tiền đề nghị: <b>{so_tien:,.0f} VNĐ</b></p>
            <p><i>(Bằng chữ: ....................................................................)</i></p>
            <br>
            <div style="display: flex; justify-content: space-around;">
                <div style="text-align: center;"><b>Người đề nghị</b><br><br><br><br><b>{ho_ten}</b></div>
                <div style="text-align: center;"><b>Kế toán trưởng</b><br><br><br><br>...........................</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def mau_bang_ke_cong_tac_phi():
    st.header("Thiết lập: Bảng kê công tác phí")
    if 'rows_ctp' not in st.session_state:
        st.session_state.rows_ctp = [{"loai": list(DINH_MUC.keys())[0], "sl": 1}]

    # Nhập liệu động ngoài Form để nút xóa/thêm chạy mượt
    for i, row in enumerate(st.session_state.rows_ctp):
        c1, c2, c3 = st.columns([3, 1, 1])
        with c1: st.session_state.rows_ctp[i]['loai'] = st.selectbox(f"Khoản chi {i+1}", list(DINH_MUC.keys()), key=f"l_{i}")
        with c2: st.session_state.rows_ctp[i]['sl'] = st.number_input(f"SL {i+1}", min_value=1, key=f"s_{i}")
        with c3: 
            if st.button("Xóa", key=f"d_{i}"):
                st.session_state.rows_ctp.pop(i)
                st.rerun()

    if st.button("➕ Thêm dòng chi phí"):
        st.session_state.rows_ctp.append({"loai": list(DINH_MUC.keys())[0], "sl": 1})
        st.rerun()

    if st.button("✨ XUẤT BẢNG KÊ"):
        tong = 0
        rows_html = ""
        for idx, r in enumerate(st.session_state.rows_ctp):
            dg = DINH_MUC.get(r['loai'], 0)
            tt = r['sl'] * dg
            tong += tt
            rows_html += f"<tr><td>{idx+1}</td><td>{r['loai']}</td><td>{r['sl']}</td><td>{dg:,.0f}</td><td>{tt:,.0f}</td></tr>"
        
        st.success("Đã tạo mẫu thành công! Nhấn Ctrl + P để in.")
        st.markdown(f"""
        <div class="vung-in-chuan">
            <h2 class="title-in" style="text-align: center; text-transform: uppercase;">Bảng kê chi tiết thanh toán</h2>
            <br>
            <table>
                <tr><th>STT</th><th>Nội dung</th><th>Số lượng</th><th>Đơn giá</th><th>Thành tiền</th></tr>
                {rows_html}
                <tr><td colspan="4"><b>TỔNG CỘNG</b></td><td><b>{tong:,.0f}</b></td></tr>
            </table>
            <div style="display: flex; justify-content: space-around; margin-top: 40px;">
                <div style="text-align: center;"><b>Người lập biểu</b></div>
                <div style="text-align: center;"><b>Kế toán trưởng</b></div>
                <div style="text-align: center;"><b>Thủ trưởng đơn vị</b></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 3. ĐIỀU KHIỂN CHƯƠNG TRÌNH
# ==========================================

st.sidebar.title("DANH MỤC MẪU")
lua_chon = st.sidebar.selectbox(
    "Chọn loại giấy tờ:",
    ["Giấy đề nghị thanh toán", "Bảng kê công tác phí"]
)

if lua_chon == "Giấy đề nghị thanh toán":
    mau_giay_de_nghi_thanh_toan()
elif lua_chon == "Bảng kê công tác phí":
    mau_bang_ke_cong_tac_phi()
