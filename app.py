import streamlit as st
import pandas as pd

# ==========================================
# 1. CẤU HÌNH & DỮ LIỆU GỐC
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

# CSS dùng chung để ẩn thành phần thừa khi in
st.markdown("""
    <style>
    @media print {
        h1, h2, .stButton, .stSuccess, .stAlert, [data-testid="stHeader"], 
        footer, [data-testid="stSidebar"], [data-testid="stForm"], [data-testid="stMetric"] {
            display: none !important;
        }
        .main .block-container { padding: 0 !important; margin: 0 !important; }
        .vung-in-chuan { display: block !important; border: none !important; width: 100% !important; }
    }
    .vung-in-chuan {
        background: white; color: black; padding: 40px;
        border: 1px solid #eee; font-family: "Times New Roman", serif; line-height: 1.5;
    }
    table { width: 100%; border-collapse: collapse; }
    th, td { border: 1px solid black; padding: 8px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. ĐỊNH NGHĨA CÁC MẪU GIẤY (DỄ DÀNG BỔ SUNG TẠI ĐÂY)
# ==========================================

def mau_giay_de_nghi_thanh_toan():
    st.header("📝 Lập Giấy Đề Nghị Thanh Toán")
    with st.form("form_thanh_toan"):
        ho_ten = st.text_input("Họ tên người đề nghị")
        noi_dung = st.text_area("Nội dung thanh toán")
        so_tien = st.number_input("Số tiền", min_value=0, step=1000)
        submitted = st.form_submit_button("Tạo mẫu in")

    if submitted:
        st.success("Đã tạo! Nhấn Ctrl + P để in.")
        st.markdown(f"""
        <div class="vung-in-chuan">
            <h2 style="text-align: center;">GIẤY ĐỀ NGHỊ THANH TOÁN</h2>
            <p>Họ tên: {ho_ten}</p>
            <p>Nội dung: {noi_dung}</p>
            <p>Số tiền: <b>{so_tien:,.0f} VNĐ</b></p>
            <div style="display: flex; justify-content: space-around; margin-top: 50px;">
                <div style="text-align: center;"><b>Người đề nghị</b><br><br><br><br><b>{ho_ten}</b></div>
                <div style="text-align: center;"><b>Kế toán trưởng</b></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def mau_bang_ke_cong_tac_phi():
    st.header("📊 Lập Bảng Kê Công Tác Phí")
    if 'rows' not in st.session_state:
        st.session_state.rows = [{"loai": list(DINH_MUC.keys())[0], "sl": 1}]

    # Nhập liệu động
    for i, row in enumerate(st.session_state.rows):
        c1, c2, c3 = st.columns([3, 2, 1])
        with c1: st.session_state.rows[i]['loai'] = st.selectbox(f"Khoản chi {i+1}", list(DINH_MUC.keys()), key=f"l_{i}")
        with c2: st.session_state.rows[i]['sl'] = st.number_input(f"Số lượng {i+1}", min_value=1, key=f"s_{i}")
        with c3:
            if st.button("Xóa", key=f"d_{i}"):
                st.session_state.rows.pop(i)
                st.rerun()

    if st.button("➕ Thêm dòng"):
        st.session_state.rows.append({"loai": list(DINH_MUC.keys())[0], "sl": 1})
        st.rerun()

    if st.button("✨ XUẤT BẢNG KÊ"):
        tong = 0
        rows_html = ""
        for idx, r in enumerate(st.session_state.rows):
            dg = DINH_MUC.get(r['loai'], 0)
            tt = r['sl'] * dg
            tong += tt
            rows_html += f"<tr><td>{idx+1}</td><td>{r['loai']}</td><td>{r['sl']}</td><td>{dg:,.0f}</td><td>{tt:,.0f}</td></tr>"
        
        st.markdown(f"""
        <div class="vung-in-chuan">
            <h2 style="text-align: center;">BẢNG KÊ CHI TIẾT THANH TOÁN</h2>
            <table>
                <tr><th>STT</th><th>Nội dung</th><th>Số lượng</th><th>Đơn giá</th><th>Thành tiền</th></tr>
                {rows_html}
                <tr><td colspan="4"><b>TỔNG CỘNG</b></td><td><b>{tong:,.0f}</b></td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

# HƯỚNG DẪN: Để thêm mẫu mới, bạn chỉ cần tạo hàm def mau_moi_cua_ban(): ... tại đây.

# ==========================================
# 3. ĐIỀU KHIỂN CHƯƠNG TRÌNH (MAIN)
# ==========================================

st.sidebar.title("DANH MỤC MẪU")
lua_chon = st.sidebar.selectbox(
    "Chọn mẫu cần dùng:",
    ["Giấy đề nghị thanh toán", "Bảng kê công tác phí"]
)

# Gọi hàm tương ứng với lựa chọn
if lua_chon == "Giấy đề nghị thanh toán":
    mau_giay_de_nghi_thanh_toan()
elif lua_chon == "Bảng kê công tác phí":
    mau_bang_ke_cong_tac_phi()
