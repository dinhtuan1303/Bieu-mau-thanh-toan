import streamlit as st

# Cấu hình trang (Sửa lỗi page_icon)
st.set_page_config(page_title="Hệ thống in phiếu", page_icon="📝", layout="centered")

# --- PHẦN 1: CSS ĐỂ ẨN TIÊU ĐỀ VÀ THÀNH PHẦN THỪA KHI IN ---
st.markdown("""
    <style>
    /* CSS dành riêng cho chế độ IN (Ctrl + P) */
    @media print {
        /* Ẩn tiêu đề lớn (h1), form nhập liệu, các nút bấm, dòng thông báo và thanh công cụ Streamlit */
        h1, [data-testid="stForm"], .stButton, .stSuccess, .stAlert, 
        header, footer, [data-testid="stHeader"], [data-testid="stDecoration"] {
            display: none !important;
            height: 0;
            margin: 0;
            padding: 0;
        }
        
        /* Loại bỏ khoảng trắng dư thừa do Streamlit tạo ra */
        .main .block-container {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }
        
        /* Hiển thị vùng in toàn màn hình */
        .vung-phiếu-in {
            border: none !important;
            width: 100% !important;
            margin: 0 !important;
            padding: 0 !important;
        }
    }

    /* Giao diện hiển thị trên màn hình máy tính */
    .vung-phiếu-in {
        background-color: white;
        color: black;
        padding: 30px;
        border: 1px solid #ddd;
        font-family: "Times New Roman", Times, serif;
    }
    </style>
    """, unsafe_allow_html=True)

# Tiêu đề này chỉ hiện trên Web, sẽ bị ẩn khi in nhờ CSS h1 ở trên
st.title("🖨️ Tạo Phiếu Thanh Toán Nhanh")

# --- PHẦN 2: FORM NHẬP LIỆU ---
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

# --- PHẦN 3: HIỂN THỊ PHIẾU ---
if chốt_phieu:
    # Thông báo này cũng sẽ tự ẩn khi in
    st.success("Đã tạo mẫu! Nhấn Ctrl + P để in.")
    
    # Tạo chuỗi HTML (Lưu ý: Không dùng thụt đầu dòng (tabs) quá nhiều bên trong f-string để tránh lỗi markdown)
    html_layout = f"""
<div class="vung-phiếu-in">
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
    <h2 style="text-align: center; margin: 0;">GIẤY ĐỀ NGHỊ THANH TOÁN</h2>
    <p style="text-align: center; margin-top: 5px;"><i>Ngày {ngay.day} tháng {ngay.month} năm {ngay.year}</i></p>
    <br>
    <p style="padding-left: 30px;"><b>Kính gửi:</b> Ban Lãnh đạo đơn vị</p>
    <p>Họ và tên người đề nghị: {ho_ten}</p>
    <p>Bộ phận: {bo_phan}</p>
    <p>Nội dung thanh toán: {noi_dung}</p>
    <p>Số tiền bằng số: <b>{so_tien:,.0f} VNĐ</b></p>
    <p><i>Số tiền bằng chữ: ................................................................................</i></p>
    <br>
    <div style="display: flex; justify-content: space-around; margin-top: 20px;">
        <div style="text-align: center;">
            <b>Người lập phiếu</b><br>(Ký, họ tên)
            <br><br><br><br><b>{ho_ten}</b>
        </div>
        <div style="text-align: center;">
            <b>Kế toán trưởng</b><br>(Ký, họ tên)
            <br><br><br><br>...........................
        </div>
    </div>
</div>
"""
    # Dùng st.components.v1.html hoặc st.markdown với unsafe_allow_html=True
    st.markdown(html_layout, unsafe_allow_html=True)
