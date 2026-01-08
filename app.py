import streamlit as st
import pandas as pd

# 1. Cấu hình trang
st.set_page_config(page_title="Hệ thống quản lý mẫu in", layout="wide")

# 2. Đọc định mức từ Excel (File dinh_muc.xlsx của bạn)
@st.cache_data
def load_dinh_muc():
    try:
        df = pd.read_excel("dinh_muc.xlsx")
        return pd.Series(df.Gia_Tri.values, index=df.Ten_Muc).to_dict()
    except:
        return {}

DINH_MUC = load_dinh_muc()

# 3. CSS để ẩn thành phần thừa khi in (Áp dụng cho tất cả các mẫu)
st.markdown("""
    <style>
    @media print {
        header, footer, .stButton, [data-testid="stHeader"], [data-testid="stForm"], 
        .stSuccess, [data-testid="stSidebar"], [data-testid="stDecoration"] {
            display: none !important;
        }
        .main .block-container { padding-top: 0 !important; }
    }
    .vung-in {
        background: white; color: black; padding: 20px;
        font-family: "Times New Roman", serif;
    }
    table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    th, td { border: 1px solid black; padding: 8px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. MENU CHỌN MẪU (SIDEBAR) ---
st.sidebar.title("DANH MỤC MẪU GIẤY")
menu_chon = st.sidebar.radio(
    "Chọn loại giấy tờ cần tạo:",
    ["1. Giấy đề nghị thanh toán", "2. Bảng kê công tác phí", "3. Bảng kê mua hàng hóa"]
)

# =========================================================
# MẪU 1: GIẤY ĐỀ NGHỊ THANH TOÁN
# =========================================================
if menu_chon == "1. Giấy đề nghị thanh toán":
    st.header("📝 GIẤY ĐỀ NGHỊ THANH TOÁN")
    with st.form("mau_1"):
        ho_ten = st.text_input("Họ tên người đề nghị")
        noi_dung = st.text_area("Nội dung thanh toán")
        so_tien = st.number_input("Số tiền (VNĐ)", min_value=0, step=1000)
        
        if st.form_submit_button("XUẤT PHIẾU"):
            st.success("Đã tạo mẫu! Nhấn Ctrl + P để in.")
            html = f"""
            <div class="vung-in">
                <h2 style="text-align: center;">GIẤY ĐỀ NGHỊ THANH TOÁN</h2>
                <p>Kính gửi: Ban Lãnh đạo đơn vị</p>
                <p>Họ tên: {ho_ten}</p>
                <p>Nội dung: {noi_dung}</p>
                <p>Số tiền: <b>{so_tien:,.0f} VNĐ</b></p>
                <div style="display: flex; justify-content: space-around; margin-top: 30px;">
                    <div><b>Người đề nghị</b></div>
                    <div><b>Kế toán trưởng</b></div>
                </div>
            </div>
            """
            st.markdown(html, unsafe_allow_html=True)

# =========================================================
# MẪU 2: BẢNG KÊ CÔNG TÁC PHÍ (Có tính toán động)
# =========================================================
elif menu_chon == "2. Bảng kê công tác phí":
    st.header("📊 BẢNG KÊ CÔNG TÁC PHÍ")
    
    if 'rows_ctp' not in st.session_state:
        st.session_state.rows_ctp = [{"loai": "Tiền ăn", "sl": 1}]

    with st.container():
        for i, row in enumerate(st.session_state.rows_ctp):
            c1, c2, c3 = st.columns([3, 2, 1])
            with c1:
                st.session_state.rows_ctp[i]['loai'] = st.selectbox(f"Khoản chi {i+1}", list(DINH_MUC.keys()), key=f"ctp_l_{i}")
            with c2:
                st.session_state.rows_ctp[i]['sl'] = st.number_input(f"Số lượng {i+1}", min_value=1, key=f"ctp_s_{i}")
            with c3:
                if st.button("Xóa", key=f"ctp_d_{i}"):
                    st.session_state.rows_ctp.pop(i)
                    st.rerun()

    if st.button("➕ Thêm dòng chi phí"):
        st.session_state.rows_ctp.append({"loai": list(DINH_MUC.keys())[0], "sl": 1})
        st.rerun()

    if st.button("XUẤT BẢNG KÊ"):
        tong = 0
        table_body = ""
        for i, r in enumerate(st.session_state.rows_ctp):
            dg = DINH_MUC.get(r['loai'], 0)
            tt = r['sl'] * dg
            tong += tt
            table_body += f"<tr><td>{i+1}</td><td>{r['loai']}</td><td>{r['sl']}</td><td>{dg:,.0f}</td><td>{tt:,.0f}</td></tr>"
        
        st.markdown(f"""
        <div class="vung-in">
            <h2 style="text-align: center;">BẢNG KÊ CÔNG TÁC PHÍ</h2>
            <table>
                <tr><th>STT</th><th>Nội dung</th><th>Số lượng</th><th>Đơn giá</th><th>Thành tiền</th></tr>
                {table_body}
                <tr><td colspan="4"><b>TỔNG CỘNG</b></td><td><b>{tong:,.0f}</b></td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# MẪU 3: BẢNG KÊ MUA HÀNG HÓA (Dành cho mua lẻ)
# =========================================================
elif menu_chon == "3. Bảng kê mua hàng hóa":
    st.header("🛒 BẢNG KÊ MUA HÀNG HÓA")
    st.info("Mẫu này dùng để kê khai các mặt hàng mua lẻ không có hóa đơn đỏ.")
    # Bạn có thể tự viết tiếp logic nhập hàng hóa tương tự mẫu 2
