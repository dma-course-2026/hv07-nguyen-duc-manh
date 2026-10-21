a, b, c = map(float, input("Nhập 3 cạnh: ").split())

if a <= 0 or b <= 0 or c <= 0:
    print("Không tạo thành tam giác")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Không tạo thành tam giác")
else:
    if a >= b and a >= c:
        canh_lon = a
        canh_1 = b
        canh_2 = c
    elif b >= a and b >= c:
        canh_lon = b
        canh_1 = a
        canh_2 = c
    else:
        canh_lon = c
        canh_1 = a
        canh_2 = b

    if abs(canh_1 ** 2 + canh_2 ** 2 - canh_lon ** 2) < 1e-9:
        print("Là tam giác vuông")
    else:
        print("Không phải tam giác vuông")