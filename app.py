import streamlit as st
import pandas as pd

# ==========================================
# 1. CẤU HÌNH HỆ THỐNG
# ==========================================
st.set_page_config(page_title="Hệ thống in Giấy đề nghị thanh toán", layout="wide")

# CSS để định dạng bản in chuyên nghiệp
st.markdown("""
    <style>
    /* Hiển thị trên Web */
    .vung-in-chuan {
        background: white; color: black; padding: 30px;
        border: 1px solid #ddd; font-family: "Times New Roman", Times, serif;
        line-height: 1.4; font-size: 13pt;
    }
    .header-table { width: 100%; border: none !important; margin-bottom: 20px; }
    .header-table td { border: none !important; text-align: center; vertical-align: top; padding: 0; }
    
    /* Hiển thị bảng kê chi phí */
    .table-chi-phi { width: 100%; border-collapse: collapse; margin-top: 10px; }
    .table-chi-phi th, .table-chi-phi td { border: 1px solid black !important; padding: 5px; text-align: center; }

    /* Chế độ in (Ctrl + P) */
    @media print {
        header, footer, .stSidebar, .stButton, .stForm, .stAlert,
        [data-testid="stHeader"], [data-testid="stToolbar"],
        div[data-testid="stVerticalBlock"] > div:not(:has(.vung-in-chuan)) {
            display: none !important;
        }
        .main .block-container { padding: 0 !important; margin: 0 !important; }
        .vung-in-chuan { display: block !important; border: none !important; width: 100%; padding: 0; }
        body { background: white; }
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. HÀM XỬ LÝ MẪU IN (THEO MẪU ĐH QUY NHƠN)
# ==========================================

def mau_giay_de_nghi_thanh_toan():
    st.subheader("⚙️ Nhập thông tin theo mẫu Giấy đề nghị thanh toán")
    
    with st.form("form_qnu"):
        col1, col2 = st.columns(2)
        with col1:
            ten_dv = st.text_input("Tên đơn vị (Ví dụ: Khoa Toán - Thống kê)", "TRƯỜNG ĐẠI HỌC QUY NHƠN")
            ma_dv = st.text_input("Mã ĐVCQHVNS", "1055595")
            ho_ten = st.text_input("Họ và tên người đề nghị thanh toán")
            chuc_vu = st.text_input("Chức vụ")
        with col2:
            dia_danh = st.text_input("Địa danh ký (Ví dụ: Quy Nhơn)", "Gia Lai")
            dv_cong_tac = st.text_input("Đơn vị công tác")
            sdt = st.text_input("Số điện thoại")
            stk = st.text_input("Số tài khoản")
            ngan_hang = st.text_input("Tại ngân hàng")
            
        noi_dung = st.text_area("Nội dung thanh toán")
        so_tien = st.number_input("Số tiền đề nghị thanh toán (VNĐ)", min_value=0, step=1000)
        bang_chu = st.text_input("Số tiền bằng chữ")
        kem_theo = st.text_input("Số lượng chứng từ gốc kèm theo", "0")
        
        submitted = st.form_submit_button("⚡ TẠO MẪU IN CHUẨN")

    if submitted:
        st.success("Đã tạo mẫu! Nhấn Ctrl + P để in.")
        
        # HTML Cấu trúc theo mẫu ảnh bạn gửi
        html_output = f"""
        <div class="vung-in-chuan">
            <table class="header-table">
                <tr>
                    <td style="width: 45%;">
                        <b>{ten_dv.upper()}</b><br>
                        Mã ĐVCQHVNS: {ma_dv}
                    </td>
                    <td style="width: 55%;">
                        <b>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</b><br>
                        <b>Độc lập - Tự do - Hạnh phúc</b><br>
                        <span style="border-top: 1px solid black; width: 150px; display: inline-block; margin-top: 5px;"></span>
                    </td>
                </tr>
                <tr>
                    <td></td>
                    <td style="text-align: right; padding-right: 50px; font-style: italic; padding-top: 10px;">
                        {dia_danh}, ngày {pd.Timestamp.now().day} tháng {pd.Timestamp.now().month} năm {pd.Timestamp.now().year}
                    </td>
                </tr>
            </table>

            <h2 style="text-align: center; margin-bottom: 20px;">GIẤY ĐỀ NGHỊ THANH TOÁN</h2>

            <p style="padding-left: 50px;"><b><i>Kính gửi:</i> &nbsp;&nbsp;&nbsp; - Hiệu trưởng Trường Đại học Quy Nhơn</b></p>
            
            <p>Họ và tên người đề nghị thanh toán: ...................{ho_ten}....................................................................</p>
            <p>Đơn vị: ...................{dv_cong_tac}...................................................................................................................</p>
            <p>Chức vụ: ...................{chuc_vu}.....................................................................................................................</p>
            <p>Số điện thoại: ...................{sdt}...............................................................................................................</p>
            <p>Số tài khoản: ...................{stk}................ tại ngân hàng: .................{ngan_hang}.................</p>
            <p>Nội dung thanh toán: {noi_dung}</p>
            <p>...........................................................................................................................................................................</p>
            <p>Đề nghị thanh toán số tiền: .................{so_tien:,.0f} VNĐ.........................................................................</p>
            <p>Bằng chữ: ...................{bang_chu}..........................................................................................................</p>
            <p><i>(Kèm theo ...................{kem_theo}.................. chứng từ gốc)</i></p>

            <table class="header-table" style="margin-top: 20px;">
                <tr>
                    <td><b>Người đề nghị</b><br><i>(Ký, họ tên)</i><br><br><br><br><b>{ho_ten}</b></td>
                    <td><b>Trưởng đơn vị</b><br><i>(Ký, họ tên)</i></td>
                </tr>
            </table>

            <div style="margin-top: 50px; border-top: 1px dashed black; padding-top: 10px;">
                <p style="text-align: center; font-weight: bold;">Phần kiểm soát phê duyệt thanh toán của Trường</p>
                <p>Bằng số: .......................................................................................................................................................</p>
                <p>Bằng chữ: .....................................................................................................................................................</p>
                <table class="header-table" style="margin-top: 10px; font-size: 11pt;">
                    <tr>
                        <td><b>Kế toán thanh toán</b><br><i>(Ký, họ tên)</i></td>
                        <td><b>Kế toán Trưởng</b><br><i>(Ký, họ tên)</i></td>
                        <td><b>Duyệt của Hiệu trưởng</b><br><i>(Ký, họ tên)</i></td>
                    </tr>
                </table>
            </div>
        </div>
        """
        st.markdown(html_output, unsafe_allow_html=True)

# ==========================================
# 3. ĐIỀU KHIỂN
# ==========================================
st.sidebar.title("DANH MỤC")
chon = st.sidebar.selectbox("Chọn mẫu:", ["Giấy đề nghị thanh toán"])

if chon == "Giấy đề nghị thanh toán":
    mau_giay_de_nghi_thanh_toan()
