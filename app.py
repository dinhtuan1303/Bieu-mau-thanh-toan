import streamlit as st

# 1. Cấu hình tiêu đề trang
st.set_page_config(page_title="Hệ thống in phiếu", page_icon="📝")

# 2. CSS Đặc biệt để ẩn mọi thứ KHI IN
st.markdown("""
    <style>
    /* Ẩn các thành phần web khi nhấn Ctrl + P */
    @media print {
        /* Ẩn tiêu đề lớn, nút bấm, dòng thông báo xanh, menu và header của Streamlit */
        h1, .stButton, .stSuccess, [data-testid="stHeader"], footer, [data-testid="stForm"], .stAlert, [data-testid="stDecoration"] {
            display: none !important;
        }
        
        /* Đẩy phiếu lên sát mép giấy, loại bỏ khoảng trắng dư thừa */
        .main .block-container {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
        }

        /* Loại bỏ khung viền bao quanh phiếu khi in */
        .khung-phieu-in {
            border: none !important;
            padding: 0 !important;
            margin: 0 !important;
            box-shadow: none !important;
        }
    }

    /* Giao diện hiển thị trên web cho dễ nhìn */
    .khung-phieu-in {
        background-color: white;
        color: black;
        padding: 40px;
        border: 1px solid #ddd;
        font-family: "Times New Roman", Times, serif;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🖨️ Tạo Phiếu Thanh Toán Nhanh")

# 3. Form nhập liệu
with st.form("form_thanh_toan"):
    col1, col2 = st.columns(2)
    with col1:
        ho_ten = st.text_input("Họ và tên người đề nghị")
        bo_phan = st.selectbox("Bộ phận", ["Hành chính", "Kế toán", "Kỹ thuật", "Tổ chức"])
    with col2:
        ngay = st.date_input("Ngày lập phiếu")
        so_tien = st.number_input("Số tiền (VNĐ)", min_value=0, step=1000)
    
    noi_dung = st.text_area("Nội dung thanh toán")
    chốt_phieu = st.form_submit_button("XUẤT PHIẾU ĐỂ IN")

# 4. Hiển thị phiếu khi bấm nút
if chốt_phieu:
    # Thông báo này chỉ hiện trên web, không hiện khi in
    st.success("Đã tạo mẫu thành công! Nhấn Ctrl + P để in phiếu.")
    
    # Nội dung phiếu bằng HTML
    html_phieu = f"""
    <div class="khung-phieu-in">
        <table style="width: 100%; border: none;">
            <tr>
                <td style="text-align: center; width: 45%; vertical-align: top;">
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
    
    # QUAN TRỌNG: unsafe_allow_html=True giúp thực thi mã HTML thay vì hiện thẻ code
    st.markdown(html_phieu, unsafe_allow_html=True)
