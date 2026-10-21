a = float(input("Nhập cơ số a: "))
n = int(input("Nhập số mũ n: "))

if n < 0:
    if a == 0:
        print("Không xác định 0 mũ số âm")
    else:
        ket_qua = 1

        for i in range(-n):
            ket_qua *= a

        ket_qua = 1 / ket_qua
        print(f"{a:g} lũy thừa {n} = {ket_qua:g}")
else:
    ket_qua = 1

    for i in range(n):
        ket_qua *= a

    print(f"{a:g} lũy thừa {n} = {ket_qua:g}")