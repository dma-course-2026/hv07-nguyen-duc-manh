a, b, c = map(float, input("Nhập 3 điểm: ").split())

diem_tb = (a + b + c) / 3

print(f"Điểm trung bình là: {diem_tb:}")

if diem_tb >= 5.0:
    print("Đậu")
else:
    print("Rớt")