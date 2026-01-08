import streamlit as st
import pandas as pd

# ==========================================
# 1. CẤU HÌNH THÔNG TIN MẶC ĐỊNH
# ==========================================
TEN_DON_VI = "TRƯỜNG ĐẠI HỌC QUY NHƠN"
MA_DV = "1055595"
DIA_DANH = "Gia Lai"

st.set_page_config(page_title="Hệ thống in Giấy đề nghị thanh toán", layout="wide")

# Hàm tự động chuyển số thành chữ
def chieu_so_thanh_chu(number):
    dict_chu = {
        '0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn',
        '5': 'năm', '6': 'sáu', '7': 'bảy', '8': 'tám', '9': 'chín'
    }
    
    def read_group_3(n):
        res = ""
        n = n.zfill(3)
        if n[0] != '0':
            res += dict_chu[n[0]] + " trăm "
        elif n[1] != '0' or n[2] != '0':
            res += "không trăm "
        if n[1] == '1':
            res += "mười "
        elif n[1] != '0':
            res += dict_chu[n[1]] + " mươi "
        elif n[0] != '0' and n[2] != '0':
            res += "lẻ "
        if n[2] == '5' and n[1] != '0':
            res += "lăm"
        elif n[2] == '1' and n[1] != '0' and n[1] != '1':
            res += "mốt"
        elif n[2] != '0' or (n[0] == '0' and n[1] == '0' and n[2] == '0'):
            if not (n[2] == '0' and (n[0] != '0' or n[1] != '0')):
                res += dict_chu[n[2]]
        return res.strip()

    if number == 0: return "Không đồng"
    s = str(int(number))[::-1]
    groups = [s[i:i+3][::-1] for i in range(0, len(s), 3)]
    units = ["", "nghìn", "triệu", "tỷ", "nghìn tỷ", "triệu tỷ"]
    parts = []
    for i, g in enumerate(groups):
        read = read_group_3(g)
        if read:
            parts.append(read + " " + units[i])
    final_text = " ".join(parts[::-1]).strip()
    return final_text.capitalize() + " đồng"

# CSS định dạng bản in
st.markdown("""
<style>
.vung-in-chuan {
    background: white; color: black; padding: 40px;
    font-family: "Times New Roman", Times, serif;
    line-height: 1.6; font-size: 13pt;
}
.header-table { width: 100%; border: none !important; margin-bottom: 10px; }
.header-table td { border: none !important; text-align: center; vertical-align: top; padding: 0; color: black; }
.info-line { margin-bottom: 5px; }
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
# 2. GIAO DIỆN NHẬP LIỆU
# ==========================================
def mau_giay_de_nghi_thanh_toan():
    st.subheader("📝 Lập Giấy đề nghị thanh toán")
    
    with st.form("form_thanh_toan"):
        c1, c2 = st.columns(2)
        with c1:
            ho_ten = st.text_input("Họ tên người đề nghị")
            dv_cong_tac = st.text_input("Đơn vị công tác")
        with c2:
            chuc_vu = st.text_input("Chức vụ")
            stk = st.text_input("Số tài khoản")
            ngan_hang = st.text_input("Ngân hàng")
            
        noi_dung = st.text_area("Nội dung thanh toán")
        
        c3, c4 = st.columns(2)
        with c3:
            so_tien = st.number_input("Số tiền (VNĐ)", min_value=0, step=10000)
        with c4:
            kem_theo = st.text_input("Số chứng từ gốc kèm theo", "0")
            
        submitted = st.form_submit_button("⚡ TẠO MẪU IN")

    if submitted:
        # Xử lý dữ liệu trước khi in
        so_tien_chu = chieu_so_thanh_chu(so_tien)
        so_tien_so = f"{so_tien:,.0f}".replace(",", ".")
        
        st.success("Đã tạo mẫu! Nhấn Ctrl + P để in.")

        # HTML MẪU IN
        html_output = f"""<div class="vung-in-chuan">
<table class="header-table">
    <tr>
        <td style="width: 45%; text-align: left;">
            <b>{TEN_DON_VI.upper()}</b><br>
            Mã ĐVCQHVNS: {MA_DV}
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
            {DIA_DANH}, ngày {pd.Timestamp.now().day} tháng {pd.Timestamp.now().month} năm {pd.Timestamp.now().year}
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
<div class="info-line">Đề nghị thanh toán số tiền: <span class="value">{so_tien_so} VNĐ</span></div>
<div class="info-line">Bằng chữ: <span class="value">{so_tien_chu}</span></div>
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
# 3. CHẠY ỨNG DỤNG
# ==========================================
st.sidebar.title("HỆ THỐNG BIỂU MẪU")
lua_chon = st.sidebar.selectbox("Chọn mẫu:", ["Giấy đề nghị thanh toán"])

if lua_chon == "Giấy đề nghị thanh toán":
    mau_giay_de_nghi_thanh_toan()
