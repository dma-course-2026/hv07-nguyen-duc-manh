a, b, m, c, d, n = map(
    float, input("Nhập a b m c d n: ").split()
)

D = a * d - b * c
Dx = m * d - b * n
Dy = a * n - m * c

if D != 0:
    x = Dx / D
    y = Dy / D

    print(f"x = {x:.3f}")
    print(f"y = {y:.3f}")
elif Dx == 0 and Dy == 0:
    print("Hệ phương trình có vô số nghiệm")
else:
    print("Hệ phương trình vô nghiệm")