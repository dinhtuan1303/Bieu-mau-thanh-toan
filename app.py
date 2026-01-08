import streamlit as st

# Giao diện ứng dụng
st.set_page_config(page_title="Hệ thống in phiếu", page_icon="📝")

st.title("🖨️ Tạo Phiếu Thanh Toán Nhanh")

# Phần nhập liệu
with st.container():
    st.subheader("Thông tin viên chức")
    col1, col2 = st.columns(2)
    with col1:
        ho_ten = st.text_input("Họ và tên")
        bo_phan = st.selectbox("Bộ phận/Phòng ban", ["Hành chính", "Kế toán", "Kỹ thuật", "Tổ chức"])
    with col2:
        ngay = st.date_input("Ngày lập phiếu")
        so_tien = st.number_input("Số tiền thanh toán (VNĐ)", min_value=0, step=1000)

    noi_dung = st.text_area("Nội dung thanh toán")

# Nút xử lý
if st.button("Tạo bản in"):
    st.success("Đã tạo mẫu! Hãy kiểm tra bên dưới.")
    st.divider()
    
    # Hiển thị mẫu giấy để in (Dùng Markdown để định dạng giống tờ giấy)
    st.markdown(f"""
    <div style="border: 1px solid black; padding: 20px; background-color: white; color: black;">
        <h2 style="text-align: center;">GIẤY ĐỀ NGHỊ THANH TOÁN</h2>
        <p><b>Kính gửi:</b> Ban Lãnh đạo đơn vị</p>
        <p><b>Họ và tên người đề nghị:</b> {ho_ten}</p>
        <p><b>Bộ phận:</b> {bo_phan}</p>
        <p><b>Nội dung:</b> {noi_dung}</p>
        <p><b>Số tiền:</b> {so_tien:,.0f} VNĐ</p>
        <p style="text-align: right;"><i>Ngày {ngay.day} tháng {ngay.month} năm {ngay.year}</i></p>
        <div style="display: flex; justify-content: space-between; margin-top: 50px;">
            <p><b>Người lập phiếu</b><br>(Ký, họ tên)</p>
            <p><b>Kế toán trưởng</b><br>(Ký, họ tên)</p>
        </div>
        <br><br><br>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 Mẹo: Nhấn Ctrl + P để in phiếu này.")