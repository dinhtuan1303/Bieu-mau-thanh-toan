import streamlit as st

# 1. Cấu hình trang
st.set_page_config(page_title="Hệ thống in phiếu", page_icon="📝")

# 2. CSS để xử lý giao diện hiển thị và GIAO DIỆN IN
st.markdown("""
    <style>
    /* CSS dành riêng cho chế độ IN (Ctrl + P) */
    @media print {
        /* Ẩn hoàn toàn tiêu đề web, nút bấm, thông báo xanh và các thành phần thừa */
        h1, .stButton, .stSuccess, [data-testid="stHeader"], footer, [data-testid="stForm"], .stAlert {
            display: none !important;
        }
        
        /* Đẩy nội dung phiếu lên sát mép trên cùng của giấy */
        .main .block-container {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
        }

        /* Xóa bỏ khung viền xám xung quanh phiếu khi in */
        .mau-in-thuc-te {
            border: none !important;
            padding: 0 !important;
            margin: 0 !important;
        }
    }

    /* Giao diện hiển thị trên màn hình máy tính để dễ nhìn */
    .mau-in-thuc-te {
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
with st.form("input_form"):
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
    st.success("Đã tạo mẫu thành công! Nhấn Ctrl + P để in phiếu.")
    
    # Định dạng nội dung tờ phiếu bằng HTML
    html_layout = f"""
    <div class="mau-in-thuc-te">
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
    
    # Dùng unsafe_allow_html=True để hiển thị đúng định dạng thay vì hiện code
    st.markdown(html_layout, unsafe_allow_html=True)
