a, b, c = map(float, input("Nhập 3 cạnh: ").split())

if a <= 0 or b <= 0 or c <= 0:
    print("Không tạo thành tam giác")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Không tạo thành tam giác")
elif a == b or b == c or a == c:
    print("Là tam giác cân")
else:
    print("Không phải tam giác cân")