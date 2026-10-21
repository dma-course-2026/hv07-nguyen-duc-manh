a, b = map(int, input("Nhập hai số nguyên: ").split())
phep_toan = input("Nhập phép toán (+, -, *, /): ")

if phep_toan == "+":
    ket_qua = a + b
    print(f"{a} + {b} = {ket_qua}")
elif phep_toan == "-":
    ket_qua = a - b
    print(f"{a} - {b} = {ket_qua}")
elif phep_toan == "*":
    ket_qua = a * b
    print(f"{a} * {b} = {ket_qua}")
elif phep_toan == "/":
    if b == 0:
        print("Không thể chia cho 0")
    else:
        ket_qua = a / b
        print(f"{a} / {b} = {ket_qua}")
else:
    print("Phép toán không hợp lệ")