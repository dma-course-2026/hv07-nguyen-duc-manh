import math

r = float(input("Nhập bán kính: "))

if r < 0:
    print("Bán kính không hợp lệ")
else:
    dien_tich = math.pi * r ** 2
    chu_vi = 2 * math.pi * r

    print(f"Diện tích: {dien_tich:.2f}")
    print(f"Chu vi: {chu_vi:.2f}")