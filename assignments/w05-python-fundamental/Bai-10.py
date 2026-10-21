n = int(input("Nhập số nguyên có 3 chữ số: "))

if 100 <= n <= 999:
    hang_tram = n // 100
    hang_chuc = (n % 100) // 10
    hang_don_vi = n % 10

    print(f"Hàng trăm = {hang_tram}")
    print(f"Hàng chục = {hang_chuc}")
    print(f"Hàng đơn vị = {hang_don_vi}")
else:
    print("Vui lòng nhập số nguyên có 3 chữ số")