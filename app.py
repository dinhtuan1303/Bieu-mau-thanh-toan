import streamlit as st
import pandas as pd

# 1. Đọc định mức từ file Excel
@st.cache_data
def load_dinh_muc():
    try:
        df = pd.read_excel("dinh_muc.xlsx")
        return pd.Series(df.Gia_Tri.values, index=df.Ten_Muc).to_dict()
    except:
        return {"Tiền ăn": 150000, "Phòng nghỉ": 350000}

DINH_MUC = load_dinh_muc()

st.title("📑 Bảng Kê Thanh Toán Đa Năng")

# 2. Tạo trạng thái lưu trữ danh sách các dòng nhập liệu
if 'rows' not in st.session_state:
    st.session_state.rows = [{"noi_dung": "Tiền ăn", "so_luong": 1}]

# 3. Giao diện thêm/bớt dòng
st.subheader("Chi tiết các khoản chi")
for i, row in enumerate(st.session_state.rows):
    col1, col2, col3 = st.columns([3, 2, 1])
    with col1:
        st.session_state.rows[i]['noi_dung'] = st.selectbox(
            f"Loại chi phí {i+1}", 
            list(DINH_MUC.keys()), 
            key=f"select_{i}"
        )
    with col2:
        st.session_state.rows[i]['so_luong'] = st.number_input(
            f"Số lượng/Ngày {i+1}", 
            min_value=1, 
            step=1, 
            key=f"num_{i}"
        )
    with col3:
        # Nút xóa dòng
        if st.button("Xóa", key=f"del_{i}"):
            st.session_state.rows.pop(i)
            st.rerun()

if st.button("➕ Thêm dòng chi phí"):
    st.session_state.rows.append({"noi_dung": list(DINH_MUC.keys())[0], "so_luong": 1})
    st.rerun()

# 4. Tính toán tổng tiền
st.divider()
tong_cong = 0
bang_du_lieu_html = ""

for i, row in enumerate(st.session_state.rows):
    don_gia = DINH_MUC.get(row['noi_dung'], 0)
    thanh_tien = row['so_luong'] * don_gia
    tong_cong += thanh_tien
    # Tạo các dòng cho bảng HTML in ấn
    bang_du_lieu_html += f"""
    <tr>
        <td>{i+1}</td>
        <td>{row['noi_dung']}</td>
        <td>{row['so_luong']}</td>
        <td>{don_gia:,.0f}</td>
        <td>{thanh_tien:,.0f}</td>
    </tr>
    """

st.metric("Tổng cộng thanh toán", f"{tong_cong:,.0f} VNĐ")

# 5. Xuất bản in (Kết hợp HTML bảng)
if st.button("🖨️ Xuất bản in"):
    st.success("Đã tạo mẫu! Nhấn Ctrl + P để in.")
    html_layout = f"""
    <div style="font-family: 'Times New Roman'; color: black; background: white; padding: 30px;">
        <h2 style="text-align: center;">BẢNG KÊ CHI TIẾT THANH TOÁN</h2>
        <table style="width: 100%; border-collapse: collapse; border: 1px solid black;">
            <tr style="background-color: #f2f2f2;">
                <th style="border: 1px solid black;">STT</th>
                <th style="border: 1px solid black;">Nội dung chi</th>
                <th style="border: 1px solid black;">Số lượng</th>
                <th style="border: 1px solid black;">Đơn giá</th>
                <th style="border: 1px solid black;">Thành tiền</th>
            </tr>
            {bang_du_lieu_html}
            <tr>
                <td colspan="4" style="border: 1px solid black; text-align: right;"><b>TỔNG CỘNG:</b></td>
                <td style="border: 1px solid black;"><b>{tong_cong:,.0f}</b></td>
            </tr>
        </table>
    </div>
    """
    st.markdown(html_layout, unsafe_allow_html=True)
