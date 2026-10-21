a, b = map(float, input("Nhập a và b: ").split())

if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print(f"Phương trình có một nghiệm: x = {x}")