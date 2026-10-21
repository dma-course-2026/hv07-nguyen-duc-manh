s = int(input("Nhập số giây: "))

if s < 0:
    print("Số giây không hợp lệ")
else:
    gio = s // 3600
    phut = (s % 3600) // 60
    giay = s % 60

    print(f"{gio} giờ : {phut} phút : {giay} giây")