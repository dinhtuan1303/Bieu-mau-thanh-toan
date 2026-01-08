import streamlit as st

# 1. Cấu hình tiêu đề trang web
st.set_page_config(page_title="Hệ thống in phiếu", page_icon="📝")

# 2. CSS Đặc biệt: Ẩn mọi thứ của trang web khi nhấn Ctrl+P
st.markdown("""
    <style>
    @media print {
        /* Ẩn tiêu đề lớn, các nút bấm, dòng thông báo xanh và menu của Streamlit */
        h1, .stButton, .stSuccess, [data-testid="stHeader"], footer, [data-testid="stForm"] {
            display: none !important;
        }
        
        /* Đẩy nội dung phiếu lên sát đầu trang giấy */
        .main .block-container {
            padding-top: 0 !important;
        }

        /* Xóa khung xám bao quanh phiếu khi in */
        .mau-in-thuc-te {
            border: none !important;
            padding: 0 !important;
        }
    }

    /* Giao diện hiển thị đẹp trên màn hình máy tính */
    .mau-in-thuc-te {
        background-color: white;
        color: black;
        padding: 40px;
        border: 1px solid #ddd;
        font-family: "Times New Roman", serif;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🖨️ Tạo Phiếu Thanh Toán Nhanh")

# 3. Form nhập liệu
with st.form("form_nhap"):
    col1, col2 = st.columns(2)
    with col1:
        ho_ten = st.text_input("Họ và tên người đề nghị")
        bo_phan = st.selectbox("Bộ phận", ["Hành chính", "Kế toán", "Kỹ thuật", "Tổ chức"])
    with col2:
        ngay = st.date_input("Ngày lập phiếu")
        so_tien = st.number_input("Số tiền (VNĐ)", min_value=0, step=1000)
    
    noi_dung = st.text_area("Nội dung thanh toán")
    chốt_phieu = st.form_submit_button("XUẤT PHIẾU")

# 4. Hiển thị phiếu
if chốt_phieu:
    st.success("Đã tạo mẫu! Nhấn Ctrl + P để in (Các phần thừa sẽ tự động biến mất).")
    
    # Định dạng HTML cho tờ phiếu
    html_content = f"""
    <div class="mau-in-thuc-te">
        <table style="width: 100%; border: none;">
            <tr>
                <td style="text-align: center; width: 40%; vertical-align: top;">
                    <b style="text-transform: uppercase;">ĐƠN VỊ CỦA BẠN</b><br>
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
        <h2 style="text-align: center; margin-bottom: 0;">GIẤY ĐỀ NGHỊ THANH TOÁN</h2>
        <p style="text-align: center; margin-top: 5px;"><i>Ngày {ngay.day} tháng {ngay.month} năm {ngay.year}</i></p>
        
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
                <br><br><br><br><br>
                <b>{ho_ten}</b>
            </div>
            <div style="text-align: center;">
                <b>Kế toán trưởng</b><br>
                (Ký, họ tên)
                <br><br><br><br><br>
                ...........................
            </div>
        </div>
    </div>
    """
    
    # HIỂN THỊ DƯỚI DẠNG VĂN BẢN ĐÃ ĐỊNH DẠNG (Quan trọng nhất)
    st.markdown(html_content, unsafe_allow_html=True)
