import streamlit as st

# 1. Cấu hình trang
st.set_page_config(page_title="Hệ thống in phiếu", page_icon="📝")

# 2. CSS để ẩn mọi thứ khi in, chỉ để lại phần phiếu
st.markdown("""
    <style>
    /* Ẩn các thành phần giao diện web khi in */
    @media print {
        header, footer, .stButton, [data-testid="stHeader"], [data-testid="stForm"], .stSuccess {
            display: none !important;
        }
        .main .block-container {
            padding: 0 !important;
        }
    }
    /* Làm đẹp mẫu phiếu trên màn hình */
    .mau-phiieu {
        background-color: white;
        color: black;
        padding: 40px;
        border: 1px solid #ccc;
        font-family: "Times New Roman", Times, serif;
        line-height: 1.5;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🖨️ Tạo Phiếu Thanh Toán Nhanh")

# 3. Form nhập liệu
with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        ho_ten = st.text_input("Họ và tên người đề nghị")
        bo_phan = st.selectbox("Bộ phận", ["Hành chính", "Kế toán", "Kỹ thuật", "Tổ chức"])
    with col2:
        ngay = st.date_input("Ngày lập phiếu")
        so_tien = st.number_input("Số tiền (VNĐ)", min_value=0, step=1000)
    
    noi_dung = st.text_area("Nội dung thanh toán")
    chốt_phieu = st.form_submit_button("Xuất Phiếu Để In")

# 4. Hiển thị phiếu khi bấm nút
if chốt_phieu:
    st.success("Đã tạo mẫu thành công! Nhấn Ctrl + P để in phiếu.")
    
    # Biến nội dung HTML của tờ phiếu
    html_layout = f"""
    <div class="mau-phiieu">
        <table style="width: 100%; border: none;">
            <tr>
                <td style="text-align: center; width: 40%; vertical-align: top;">
                    <b>ĐƠN VỊ CỦA BẠN</b><br>
                    ----------
                </td>
                <td style="text-align: center; vertical-align: top;">
                    <b>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</b><br>
                    <b>Độc lập - Tự do - Hạnh phúc</b><br>
                    ----------
                </td>
            </tr>
        </table>
        
        <br><br>
        <h2 style="text-align: center;">GIẤY ĐỀ NGHỊ THANH TOÁN</h2>
        <p style="text-align: center;"><i>Ngày {ngay.day} tháng {ngay.month} năm {ngay.year}</i></p>
        
        <br>
        <p style="padding-left: 30px;"><b>Kính gửi:</b> Ban Lãnh đạo đơn vị</p>
        <p>Họ và tên người đề nghị: {ho_ten}</p>
        <p>Bộ phận: {bo_phan}</p>
        <p>Nội dung thanh toán: {noi_dung}</p>
        <p>Số tiền bằng số: <b>{so_tien:,.0f} VNĐ</b></p>
        <p><i>Số tiền bằng chữ: ........................................................................................</i></p>
        
        <br>
        <div style="display: flex; justify-content: space-around; margin-top: 20px;">
            <div style="text-align: center;">
                <b>Người lập phiếu</b><br>
                (Ký, họ tên)
                <br><br><br><br>
                <b>{ho_ten}</b>
            </div>
            <div style="text-align: center;">
                <b>Kế toán trưởng</b><br>
                (Ký, họ tên)
                <br><br><br><br>
                ...........................
            </div>
        </div>
    </div>
    """
    
    # QUAN TRỌNG: Cần unsafe_allow_html=True để hiển thị đúng HTML
    st.markdown(html_layout, unsafe_allow_html=True)
