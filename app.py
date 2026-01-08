import streamlit as st
import pandas as pd

# ==========================================
# 1. CẤU HÌNH THÔNG TIN MẶC ĐỊNH
# ==========================================
TEN_DON_VI_MAC_DINH = "TRƯỜNG ĐẠI HỌC QUY NHƠN"
MA_DON_VI_MAC_DINH = "1055595"
DIA_DANH_MAC_DINH = "Gia Lai"

st.set_page_config(page_title="Hệ thống in Giấy đề nghị thanh toán", layout="wide")

st.markdown("""
<style>
.vung-in-chuan {
    background: white; color: black; padding: 40px;
    border: 1px solid #ddd; font-family: "Times New Roman", Times, serif;
    line-height: 1.6; font-size: 13pt;
}
.header-table { width: 100%; border: none !important; margin-bottom: 10px; }
.header-table td { border: none !important; text-align: center; vertical-align: top; padding: 0; color: black; }
.info-line { margin-bottom: 8px; }
.label { font-weight: normal; }
.value { font-weight: bold; }

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
    st.subheader("⚙️ Nhập thông tin thanh toán")
    
    with st.form("form_qnu"):
        c1, c2 = st.columns(2)
        with c1:
            ho_ten = st.text_input("Họ tên người đề nghị")
            dv_cong_tac = st.text_input("Đơn vị công tác")
        with c2:
            chuc_vu = st.text_input("Chức vụ")
            stk = st.text_input("Số tài khoản")
            ngan_hang = st.text_input("Tại ngân hàng")
            
        noi_dung = st.text_area("Nội dung thanh toán")
        
        c3, c4 = st.columns(2)
        with c3:
            so_tien = st.number_input("Số tiền (VNĐ)", min_value=0, step=1000)
        with c4:
            kem_theo = st.text_input("Số chứng từ gốc kèm theo", "0")
            
        bang_chu = st.text_input("Bằng chữ")
        
        submitted = st.form_submit_button("⚡ TẠO MẪU IN")

    if submitted:
        st.success("Đã tạo mẫu thành công! Nhấn Ctrl + P để in.")
        
        html_output = f"""<div class="vung-in-chuan">
<table class="header-table">
    <tr>
        <td style="width: 45%; text-align: left;">
            <b>{TEN_DON_VI_MAC_DINH.upper()}</b><br>
            Mã ĐVCQHVNS: {MA_DON_VI_MAC_DINH}
        </td>
        <td style="width: 55%;">
            <b>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</b><br>
            <b>Độc lập - Tự do - Hạnh phúc</b><br>
            <span style="text-decoration: overline;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
        </td>
    </tr>
    <tr>
        <td></td>
        <td style="text-align: right; padding-right: 20px; font-style: italic;">
            {DIA_DANH_MAC_DINH}, ngày {pd.Timestamp.now().day} tháng {pd.Timestamp.now().month} năm {pd.Timestamp.now().year}
        </td>
    </tr>
</table>

<h2 style="text-align: center; margin-top: 10px; margin-bottom: 20px;">GIẤY ĐỀ NGHỊ THANH TOÁN</h2>

<p style="padding-left: 50px;"><b><i>Kính gửi:</i> &nbsp;&nbsp;&nbsp; - Hiệu trưởng Trường Đại học Quy Nhơn</b></p>

<div class="info-line">Họ và tên người đề nghị thanh toán: <span class="value">{ho_ten}</span></div>
<div class="info-line">Đơn vị: <span class="value">{dv_cong_tac}</span></div>
<div class="info-line">Chức vụ: <span class="value">{chuc_vu}</span></div>
<div class="info-line">Số tài khoản: <span class="value">{stk}</span> tại ngân hàng: <span class="value">{ngan_hang}</span></div>
<div class="info-line">Nội dung thanh toán: <span class="value">{noi_dung}</span></div>
<div class="info-line">Đề nghị thanh toán số tiền: <span class="value">{so_tien:,.0f} VNĐ</span></div>
<div class="info-line">Bằng chữ: <span class="value">{bang_chu}</span></div>
<div class="info-line"><i>(Kèm theo <span class="value">{kem_theo}</span> chứng từ gốc)</i></div>

<table class="header-table" style="margin-top: 30px;">
    <tr>
        <td><b>Người đề nghị</b><br><i>(Ký, họ tên)</i><br><br><br><br><b>{ho_ten}</b></td>
        <td><b>Trưởng đơn vị</b><br><i>(Ký, họ tên)</i></td>
    </tr>
</table>

<div style="margin-top: 60px; border-top: 1px dashed black; padding-top: 15px;">
    <p style="text-align: center; font-weight: bold;">Phần kiểm soát phê duyệt thanh toán của Trường</p>
    <p>Bằng số: .................................................................................................................</p>
    <p>Bằng chữ: ................................................................................................................</p>
    <table class="header-table" style="margin-top: 15px; font-size: 11pt;">
        <tr>
            <td><b>Kế toán thanh toán</b><br><i>(Ký, họ tên)</i></td>
            <td><b>Kế toán Trưởng</b><br><i>(Ký, họ tên)</i></td>
            <td><b>Duyệt của Hiệu trưởng</b><br><i>(Ký, họ tên)</i></td>
        </tr>
    </table>
</div>
</div>"""
        st.markdown(html_output, unsafe_allow_html=True)

# ==========================================
# 3. ĐIỀU KHIỂN
# ==========================================
st.sidebar.title("DANH MỤC")
chon = st.sidebar.selectbox("Chọn mẫu:", ["Giấy đề nghị thanh toán"])

if chon == "Giấy đề nghị thanh toán":
    mau_giay_de_nghi_thanh_toan()
