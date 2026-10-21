a, b = map(int, input("Nhập a và b: ").split())

if a == 0 and b == 0:
    print("Không kiểm tra ước số khi cả hai số đều bằng 0")
elif a == 0:
    print("0 không là ước của", b)
    print(f"{b} là ước của 0")
elif b == 0:
    print("0 không là ước của", a)
    print(f"{a} là ước của 0")
else:
    if b % a == 0:
        print(f"{a} là ước của {b}")
    else:
        print(f"{a} không là ước của {b}")

    if a % b == 0:
        print(f"{b} là ước của {a}")
    else:
        print(f"{b} không là ước của {a}")