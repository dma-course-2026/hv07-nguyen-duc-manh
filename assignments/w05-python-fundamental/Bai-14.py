import math

a, b, c = map(float, input("Nhập 3 cạnh tam giác: ").split())

if a <= 0 or b <= 0 or c <= 0:
    print("Không tạo thành tam giác")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Không tạo thành tam giác")
else:
    chu_vi = a + b + c
    p = chu_vi / 2

    dien_tich = math.sqrt(
        p * (p - a) * (p - b) * (p - c)
    )

    print(f"Chu vi: {chu_vi:.2f}")
    print(f"Diện tích: {dien_tich:.2f}")