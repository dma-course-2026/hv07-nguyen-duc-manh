ho_ten = input("Nhập họ tên chủ hộ: ")
chi_so_cu, chi_so_moi = map(
    int, input("Nhập chỉ số cũ và mới: ").split()
)

dien_tieu_thu = chi_so_moi - chi_so_cu

if dien_tieu_thu < 0:
    print("Chỉ số điện không hợp lệ")
else:
    if dien_tieu_thu <= 60:
        tien_dien = dien_tieu_thu * 5
    elif dien_tieu_thu <= 160:
        tien_dien = 60 * 5 + (dien_tieu_thu - 60) * 8
    else:
        tien_dien = (
            60 * 5
            + 100 * 8
            + (dien_tieu_thu - 160) * 10
        )

    print(f"Chủ hộ: {ho_ten}")
    print(f"Điện tiêu thụ: {dien_tieu_thu} kW")
    print(f"Số tiền phải trả là: {tien_dien:.2f}")