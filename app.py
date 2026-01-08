import streamlit as st

st.set_page_config(page_title="Hệ thống in phiếu", page_icon="📝")

# --- PHẦN CSS ĐỂ ẨN FORM KHI IN ---
st.markdown("""
    <style>
    @media print {
        /* Ẩn toàn bộ các thành phần của Streamlit như menu, sidebar, các ô nhập liệu */
        [data-testid="stForm"], 
        header, 
        footer, 
        .stButton, 
        [data-testid="stHeader"] {
            display: none !important;
        }
        
        /* Loại bỏ các khoảng trắng dư thừa do Streamlit tạo ra khi in */
        .main .block-container {
            padding: 0 !important;
            margin: 0 !important;
        }

        /* Đảm bảo phần phiếu in được hiển thị rõ ràng */
        .print-container {
            border: none !important;
            width: 100%;
        }
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🖨️ Tạo Phiếu Thanh Toán Nhanh")

# Phần nhập liệu (Sẽ bị ẩn khi nhấn Ctrl + P)
with st.form("my_form"):
    st.subheader("Thông tin viên chức")
    col1, col2 = st.columns(2)
    with col1:
        ho_ten = st.text_input("Họ và tên")
        bo_phan = st.selectbox("Bộ phận/Phòng ban", ["Hành chính", "Kế toán", "Kỹ thuật", "Tổ chức"])
    with col2:
        ngay = st.date_input("Ngày lập phiếu")
        so_tien = st.number_input("Số tiền thanh toán (VNĐ)", min_value=0, step=1000)

    noi_dung = st.text_area("Nội dung thanh toán")
    submit_button = st.form_submit_button("Tạo bản in")

# Xử lý hiển thị mẫu phiếu
if submit_button:
    st.success("Đã tạo mẫu! Nhấn Ctrl + P để in (Lúc này các ô nhập liệu sẽ biến mất).")
    
    # Bao bọc phiếu trong một thẻ div có class là 'print-container'
    st.markdown(f"""
    <div class="print-container" style="border: 2px solid black; padding: 40px; background-color: white; color: black; font-family: 'Times New Roman'; line-height: 1.6;">
        <table style="width: 100%; border: none;">
            <tr>
                <td style="text-align: center; width: 40%;">
                    <b>ĐƠN VỊ CỦA BẠN</b><br>
                    ----------
                </td>
                <td style="text-align: center;">
                    <b>CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</b><br>
                    <b>Độc lập - Tự do - Hạnh phúc</b><br>
                    ----------
                </td>
            </tr>
        </table>
        
        <br><br>
        <h2 style="text-align: center; margin-bottom: 0;">GIẤY ĐỀ NGHỊ THANH TOÁN</h2>
        <p style="text-align: center; margin-top: 0;"><i>Ngày {ngay.day} tháng {ngay.month} năm {ngay.year}</i></p>
        
        <br>
        <p style="margin-left: 50px;"><b>Kính gửi:</b> Ban Lãnh đạo đơn vị</p>
        <p>Họ và tên người đề nghị: {ho_ten}</p>
        <p>Bộ phận: {bo_phan}</p>
        <p>Nội dung thanh toán: {noi_dung}</p>
        <p>Số tiền bằng số: <b>{so_tien:,.0f} VNĐ</b></p>
        <p><i>(Số tiền bằng chữ: ........................................................................)</i></p>
        
        <br>
        <div style="display: flex; justify-content: space-between; margin-top: 30px;">
            <div style="text-align: center; width: 45%;">
                <b>Người lập phiếu</b><br>(Ký, họ tên)
                <br><br><br><br>
                <b>{ho_ten}</b>
            </div>
            <div style="text-align: center; width: 45%;">
                <b>Kế toán trưởng</b><br>(Ký, họ tên)
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
