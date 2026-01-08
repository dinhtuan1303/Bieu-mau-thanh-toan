import streamlit as st
# Sửa lỗi 1: Thêm dấu phẩy giữa các module
from modules import mauso3_tamung, mauso4_1_thanhtoan

st.set_page_config(page_title="Hệ thống QNU", layout="wide")

st.sidebar.title("DANH MỤC")

# Thiết lập danh sách lựa chọn
option_1 = "Giấy đề nghị tạm ứng"
option_2 = "Giấy đề nghị thanh toán"

menu = st.sidebar.selectbox("Chọn loại mẫu:", [option_1, option_2])

# Sửa lỗi 2: Đảm bảo điều kiện if khớp hoàn toàn với selectbox
if menu == option_1:
    mauso3_tamung.hien_thi()
elif menu == option_2:
    mauso4_1_thanhtoan.hien_thi()
