import os

# Tên file mặc định để lưu dữ liệu
FILE_NAME = "quan_ly_phong_tro.txt"

# Đơn giá điện và nước (Sinh viên có thể điều chỉnh tùy ý)
DON_GIA_DIEN = 3500   # VNĐ / kWh
DON_GIA_NUOC = 12000  # VNĐ / m3

def doc_dieu_kien_so_thuc(thong_bao):
    """Hàm kiểm tra nhập số thực dương"""
    while True:
        try:
            gia_tri = float(input(thong_bao))
            if gia_tri <= 0:
                print("Lỗi: Giá trị phải lớn hơn 0. Vui lòng nhập lại!")
            else:
                return gia_tri
        except ValueError:
            print("Lỗi: Nhập sai kiểu dữ liệu (phải là số). Vui lòng nhập lại!")

def doc_dieu_kien_so_khong_am(thong_bao):
    """Hàm kiểm tra nhập số không âm (dùng cho điện, nước)"""
    while True:
        try:
            gia_tri = float(input(thong_bao))
            if gia_tri < 0:
                print("Lỗi: Chỉ số không được âm. Vui lòng nhập lại!")
            else:
                return gia_tri
        except ValueError:
            print("Lỗi: Nhập sai kiểu dữ liệu (phải là số). Vui lòng nhập lại!")

# 3.1. Quản lý phòng: Thêm phòng
def them_phong(danh_sach_phong):
    print("\n--- THÊM PHÒNG TRỌ MỚI ---")
    while True:
        ma_phong = input("Nhập mã phòng: ").strip()
        if not ma_phong:
            print("Lỗi: Mã phòng không được để trống.")
            continue
        # Kiểm tra mã phòng trùng
        trung = False
        for p in danh_sach_phong:
            if p["ma_phong"] == ma_phong:
                trung = True
                break
        if trung:
            print("Lỗi: Mã phòng đã tồn tại. Vui lòng nhập mã khác!")
        else:
            break

    so_phong = input("Nhập số phòng: ").strip()
    dien_tich = doc_dieu_kien_so_thuc("Nhập diện tích (m2): ")
    gia_thue = doc_dieu_kien_so_thuc("Nhập giá thuê (VNĐ): ")
    
    print("Chọn trạng thái phòng:")
    print("1. Trống")
    print("2. Đang thuê")
    chon_tt = input("Lựa chọn (1/2): ").strip()
    if chon_tt == "2":
        trang_thai = "Đang thuê"
        ten_nguoi_thue = input("Nhập tên người thuê: ").strip()
        so_dien = doc_dieu_kien_so_khong_am("Nhập số điện tiêu thụ (kWh): ")
        so_nuoc = doc_dieu_kien_so_khong_am("Nhập số nước tiêu thụ (m3): ")
    else:
        trang_thai = "Trống"
        ten_nguoi_thue = "-"
        so_dien = 0.0
        so_nuoc = 0.0

    phong_moi = {
        "ma_phong": ma_phong,
        "so_phong": so_phong,
        "dien_tich": dien_tich,
        "gia_thue": gia_thue,
        "trang_thai": trang_thai,
        "ten_nguoi_thue": ten_nguoi_thue,
        "so_dien": so_dien,
        "so_nuoc": so_nuoc
    }
    danh_sach_phong.append(phong_moi)
    print("Thêm phòng thành công!")

# 3.1. Hiển thị danh sách phòng
def hien_thi_danh_sach(danh_sach_phong):
    if not danh_sach_phong:
        print("\nDanh sách phòng trọ hiện đang trống!")
        return
    
    print("\n" + "="*105)
    print(f"{'Mã P':<8} | {'Số P':<8} | {'Diện tích':<10} | {'Giá thuê':<12} | {'Trạng thái':<12} | {'Người thuê':<18} | {'Số điện':<8} | {'Số nước':<8}")
    print("="*105)
    for p in danh_sach_phong:
        print(f"{p['ma_phong']:<8} | {p['so_phong']:<8} | {p['dien_tich']:<10.1f} | {p['gia_thue']:<12,.0f} | {p['trang_thai']:<12} | {p['ten_nguoi_thue']:<18} | {p['so_dien']:<8.1f} | {p['so_nuoc']:<8.1f}")
    print("="*105)

# 3.1. Cập nhật thông tin phòng
def cap_nhat_phong(danh_sach_phong):
    print("\n--- CẬP NHẬT THÔNG TIN PHÒNG ---")
    ma_phong = input("Nhập mã phòng cần cập nhật: ").strip()
    
    phong_tim_thay = None
    for p in danh_sach_phong:
        if p["ma_phong"] == ma_phong:
            phong_tim_thay = p
            break
            
    if not phong_tim_thay:
        print("Lỗi: Phòng không tồn tại trong hệ thống!")
        return

    print(f"Đang cập nhật cho phòng: {ma_phong}. Nhấn Enter nếu muốn giữ nguyên giá trị cũ.")
    
    so_phong_moi = input(f"Số phòng mới [{phong_tim_thay['so_phong']}]: ").strip()
    if so_phong_moi:
        phong_tim_thay['so_phong'] = so_phong_moi
        
    dien_tich_moi = input(f"Diện tích mới [{phong_tim_thay['dien_tich']}]: ").strip()
    if dien_tich_moi:
        try:
            val = float(dien_tich_moi)
            if val > 0: phong_tim_thay['dien_tich'] = val
            else: print("Diện tích không hợp lệ, giữ nguyên giá trị cũ.")
        except ValueError:
            print("Sai kiểu dữ liệu, giữ nguyên giá trị cũ.")

    gia_moi = input(f"Giá thuê mới [{phong_tim_thay['gia_thue']}]: ").strip()
    if gia_moi:
        try:
            val = float(gia_moi)
            if val > 0: phong_tim_thay['gia_thue'] = val
            else: print("Giá thuê không hợp lệ, giữ nguyên giá trị cũ.")
        except ValueError:
            print("Sai kiểu dữ liệu, giữ nguyên giá trị cũ.")

    tt_moi = input(f"Trạng thái mới (1. Trống, 2. Đang thuê) [{phong_tim_thay['trang_thai']}]: ").strip()
    if tt_moi == "1":
        phong_tim_thay['trang_thai'] = "Trống"
        phong_tim_thay['ten_nguoi_thue'] = "-"
        phong_tim_thay['so_dien'] = 0.0
        phong_tim_thay['so_nuoc'] = 0.0
    elif tt_moi == "2":
        phong_tim_thay['trang_thai'] = "Đang thuê"
        ten_moi = input(f"Tên người thuê mới [{phong_tim_thay['ten_nguoi_thue']}]: ").strip()
        if ten_moi: phong_tim_thay['ten_nguoi_thue'] = ten_moi
        
        sd_moi = input(f"Số điện mới [{phong_tim_thay['so_dien']}]: ").strip()
        if sd_moi:
            try: phong_tim_thay['so_dien'] = float(sd_moi)
            except ValueError: pass
            
        sn_moi = input(f"Số nước mới [{phong_tim_thay['so_nuoc']}]: ").strip()
        if sn_moi:
            try: phong_tim_thay['so_nuoc'] = float(sn_moi)
            except ValueError: pass

    print("Cập nhật thông tin phòng thành công!")

# 3.1 & 5. Xóa phòng
def xoa_phong(danh_sach_phong):
    print("\n--- XÓA PHÒNG TRỌ ---")
    ma_phong = input("Nhập mã phòng cần xóa: ").strip()
    
    phong_tim_thay = None
    for p in danh_sach_phong:
        if p["ma_phong"] == ma_phong:
            phong_tim_thay = p
            break
            
    if not phong_tim_thay:
        print("Lỗi: Phòng không tồn tại trong hệ thống!")
        return

    # Kiểm tra: Phòng đang có người thuê không được xóa nếu chưa xử lý trạng thái
    if phong_tim_thay['trang_thai'] == "Đang thuê":
        print("Lỗi: Phòng đang có người thuê, không được xóa nếu chưa xử lý trạng thái (chuyển về trống trước khi xóa)!")
        return

    danh_sach_phong.remove(phong_tim_thay)
    print("Xóa phòng thành công!")

# 3.2. Tìm kiếm phòng
def tim_kiem_phong(danh_sach_phong):
    print("\n--- TÌM KIẾM PHÒNG TRỌ ---")
    print("1. Tìm theo Mã phòng")
    print("2. Tìm theo Số phòng")
    print("3. Tìm theo Tên người thuê")
    print("4. Tìm theo Trạng thái phòng")
    chon = input("Nhập lựa chọn tìm kiếm (1-4): ").strip()
    
    ket_qua = []
    if chon == "1":
        tu_khoa = input("Nhập mã phòng cần tìm: ").strip().lower()
        ket_qua = [p for p in danh_sach_phong if tu_khoa in p['ma_phong'].lower()]
    elif chon == "2":
        tu_khoa = input("Nhập số phòng cần tìm: ").strip().lower()
        ket_qua = [p for p in danh_sach_phong if tu_khoa in p['so_phong'].lower()]
    elif chon == "3":
        tu_khoa = input("Nhập tên người thuê cần tìm: ").strip().lower()
        ket_qua = [p for p in danh_sach_phong if tu_khoa in p['ten_nguoi_thue'].lower()]
    elif chon == "4":
        tu_khoa = input("Nhập trạng thái cần tìm (Trống / Đang thuê): ").strip().lower()
        ket_qua = [p for p in danh_sach_phong if tu_khoa in p['trang_thai'].lower()]
    else:
        print("Lựa chọn không hợp lệ!")
        return

    if ket_qua:
        print(f"\nTìm thấy {len(ket_qua)} kết quả phù hợp:")
        hien_thi_danh_sach(ket_qua)
    else:
        print("Không tìm thấy phòng phù hợp với yêu cầu.")

# 3.3. Sắp xếp phòng
def sap_xep_phong(danh_sach_phong):
    if not danh_sach_phong:
        print("\nDanh sách trống, không thể sắp xếp!")
        return
        
    print("\n--- SẮP XẾP PHÒNG TRỌ ---")
    print("1. Sắp xếp theo Giá thuê")
    print("2. Sắp xếp theo Diện tích")
    print("3. Sắp xếp theo Chi phí sử dụng (Tổng tiền thanh toán)")
    chon = input("Nhập lựa chọn (1-3): ").strip()
    
    thu_tu = input("Thứ tự (1. Tăng dần, 2. Giảm dần): ").strip()
    dao_nguoc = True if thu_tu == "2" else False

    if chon == "1":
        danh_sach_phong.sort(key=lambda x: x['gia_thue'], reverse=dao_nguoc)
        print("Đã sắp xếp theo Giá thuê thành công!")
    elif chon == "2":
        danh_sach_phong.sort(key=lambda x: x['dien_tich'], reverse=dao_nguoc)
        print("Đã sắp xếp theo Diện tích thành công!")
    elif chon == "3":
        danh_sach_phong.sort(key=lambda x: (x['gia_thue'] + x['so_dien']*DON_GIA_DIEN + x['so_nuoc']*DON_GIA_NUOC), reverse=dao_nguoc)
        print("Đã sắp xếp theo Chi phí sử dụng thành công!")
    else:
        print("Lựa chọn không hợp lệ!")
        return
    hien_thi_danh_sach(danh_sach_phong)

# 3.4. Tính tiền phòng
def tinh_tien_phong(danh_sach_phong):
    print("\n--- TÍNH TIỀN PHÒNG ---")
    ma_phong = input("Nhập mã phòng cần tính tiền: ").strip()
    
    phong = None
    for p in danh_sach_phong:
        if p["ma_phong"] == ma_phong:
            phong = p
            break
            
    if not phong:
        print("Lỗi: Phòng không tồn tại!")
        return

    tien_thue = phong['gia_thue']
    tien_dien = phong['so_dien'] * DON_GIA_DIEN
    tien_nuoc = phong['so_nuoc'] * DON_GIA_NUOC
    tong_tien = tien_thue + tien_dien + tien_nuoc

    print("\n" + "~"*40)
    print(f"HÓA ĐƠN THANH TOÁN - PHÒNG: {phong['so_phong']} (Mã: {phong['ma_phong']})")
    print(f"- Người thuê: {phong['ten_nguoi_thue']}")
    print(f"- Tiền thuê phòng: {tien_thue:,.0f} VNĐ")
    print(f"- Tiền điện ({phong['so_dien']} kWh x {DON_GIA_DIEN:,}): {tien_dien:,.0f} VNĐ")
    print(f"- Tiền nước ({phong['so_nuoc']} m3 x {DON_GIA_NUOC:,}): {tien_nuoc:,.0f} VNĐ")
    print("-" * 40)
    print(f"TỔNG CỘNG PHẢI THANH TOÁN: {tong_tien:,.0f} VNĐ")
    print("~"*40)

# 3.5. Thống kê
def thong_ke(danh_sach_phong):
    print("\n--- BÁO CÁO THỐNG KÊ ---")
    tong_so_phong = len(danh_sach_phong)
    if tong_so_phong == 0:
        print("Danh sách phòng trống, chưa có dữ liệu thống kê.")
        return

    phong_dang_thue = sum(1 for p in danh_sach_phong if p['trang_thai'] == "Đang thuê")
    phong_trong = tong_so_phong - phong_dang_thue
    
    tong_doanh_thu = sum(p['gia_thue'] + p['so_dien']*DON_GIA_DIEN + p['so_nuoc']*DON_GIA_NUOC for p in danh_sach_phong if p['trang_thai'] == "Đang thuê")
    
    phong_max_chi_phi = max(danh_sach_phong, key=lambda x: x['gia_thue'] + x['so_dien']*DON_GIA_DIEN + x['so_nuoc']*DON_GIA_NUOC)
    max_chi_phi_val = phong_max_chi_phi['gia_thue'] + phong_max_chi_phi['so_dien']*DON_GIA_DIEN + phong_max_chi_phi['so_nuoc']*DON_GIA_NUOC

    print(f"1. Tổng số phòng: {tong_so_phong}")
    print(f"2. Số phòng đang thuê: {phong_dang_thue}")
    print(f"3. Số phòng còn trống: {phong_trong}")
    print(f"4. Tổng doanh thu tạm tính (các phòng đang thuê): {tong_doanh_thu:,.0f} VNĐ")
    print(f"5. Phòng có chi phí cao nhất: Mã phòng '{phong_max_chi_phi['ma_phong']}' (Số phòng: {phong_max_chi_phi['so_phong']}) với tổng chi phí: {max_chi_phi_val:,.0f} VNĐ")

# 3.6. Lưu dữ liệu xuống file TXT
def luu_du_lieu(danh_sach_phong):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for p in danh_sach_phong:
                line = f"{p['ma_phong']}|{p['so_phong']}|{p['dien_tich']}|{p['gia_thue']}|{p['trang_thai']}|{p['ten_nguoi_thue']}|{p['so_dien']}|{p['so_nuoc']}\n"
                f.write(line)
        print(f"Lưu dữ liệu thành công vào file '{FILE_NAME}'!")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

# 3.6. Đọc dữ liệu từ file TXT
def doc_du_lieu(danh_sach_phong):
    if not os.path.exists(FILE_NAME):
        print(f"Lỗi: File '{FILE_NAME}' không tồn tại!")
        return

    try:
        danh_sach_phong.clear()
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 8:
                    p = {
                        "ma_phong": parts[0],
                        "so_phong": parts[1],
                        "dien_tich": float(parts[2]),
                        "gia_thue": float(parts[3]),
                        "trang_thai": parts[4],
                        "ten_nguoi_thue": parts[5],
                        "so_dien": float(parts[6]),
                        "so_nuoc": float(parts[7])
                    }
                    danh_sach_phong.append(p)
        print(f"Đọc dữ liệu thành công từ file '{FILE_NAME}'!")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")

# Giao diện Menu chính
def main():
    danh_sach_phong = []
    # Tự động đọc dữ liệu cũ nếu file tồn tại
    if os.path.exists(FILE_NAME):
        doc_du_lieu(danh_sach_phong)

    while True:
        print("\n" + "="*50)
        print("          QUẢN LÝ PHÒNG TRỌ")
        print("="*50)
        print("1. Thêm phòng")
        print("2. Hiển thị danh sách")
        print("3. Cập nhật phòng")
        print("4. Xóa phòng")
        print("5. Tìm kiếm")
        print("6. Sắp xếp")
        print("7. Tính tiền phòng")
        print("8. Thống kê")
        print("9. Lưu dữ liệu")
        print("10. Đọc dữ liệu")
        print("0. Thoát")
        print("="*50)
        
        lua_chon = input("Lựa chọn: ").strip()
        
        if lua_chon == "1":
            them_phong(danh_sach_phong)
        elif lua_chon == "2":
            hien_thi_danh_sach(danh_sach_phong)
        elif lua_chon == "3":
            cap_nhat_phong(danh_sach_phong)
        elif lua_chon == "4":
            xoa_phong(danh_sach_phong)
        elif lua_chon == "5":
            tim_kiem_phong(danh_sach_phong)
        elif lua_chon == "6":
            sap_xep_phong(danh_sach_phong)
        elif lua_chon == "7":
            tinh_tien_phong(danh_sach_phong)
        elif lua_chon == "8":
            thong_ke(danh_sach_phong)
        elif lua_chon == "9":
            luu_du_lieu(danh_sach_phong)
        elif lua_chon == "10":
            doc_du_lieu(danh_sach_phong)
        elif lua_chon == "0":
            print("\nCảm ơn bạn đã sử dụng chương trình Quản lý phòng trọ. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng nhập từ 0 đến 10.")

if __name__ == "__main__":
    main()