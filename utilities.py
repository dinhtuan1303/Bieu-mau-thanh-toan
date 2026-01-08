def format_vnd(amount):
    """Định dạng số thành chuỗi 1.000.000"""
    return f"{amount:,.0f}".replace(",", ".")

def chieu_so_thanh_chu(number):
    """Hàm đổi số thành chữ Tiếng Việt"""
    dict_chu = {'0':'không','1':'một','2':'hai','3':'ba','4':'bốn','5':'năm','6':'sáu','7':'bảy','8':'tám','9':'chín'}
    def read_group_3(n):
        res = ""; n = n.zfill(3)
        if n[0] != '0': res += dict_chu[n[0]] + " trăm "
        elif n[1] != '0' or n[2] != '0': res += "không trăm "
        if n[1] == '1': res += "mười "
        elif n[1] != '0': res += dict_chu[n[1]] + " mươi "
        elif n[0] != '0' and n[2] != '0': res += "lẻ "
        if n[2] == '5' and n[1] != '0': res += "lăm"
        elif n[2] == '1' and n[1] != '0' and n[1] != '1': res += "mốt"
        elif n[2] != '0' or (n[0] == '0' and n[1] == '0' and n[2] == '0'):
            if not (n[2] == '0' and (n[0] != '0' or n[1] != '0')): res += dict_chu[n[2]]
        return res.strip()
    if number == 0: return "Không đồng"
    s = str(int(number))[::-1]
    groups = [s[i:i+3][::-1] for i in range(0, len(s), 3)]
    units = ["", "nghìn", "triệu", "tỷ", "nghìn tỷ", "triệu tỷ"]
    parts = [read_group_3(g) + " " + units[i] for i, g in enumerate(groups) if read_group_3(g)]
    return " ".join(parts[::-1]).strip().capitalize() + " đồng"