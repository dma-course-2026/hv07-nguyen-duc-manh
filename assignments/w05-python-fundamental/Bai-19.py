a, b = map(float, input("Nhập a và b: ").split())

if a > 0:
    x = -b / a
    print(f"Bất phương trình có nghiệm: x >= {x}")
elif a < 0:
    x = -b / a
    print(f"Bất phương trình có nghiệm: x <= {x}")
else:
    if b >= 0:
        print("Bất phương trình đúng với mọi x")
    else:
        print("Bất phương trình vô nghiệm")