a, b = map(int, input("Nhập a và b: ").split())

if a < b:
    print(f"{a} là giá trị nhỏ nhất")
elif b < a:
    print(f"{b} là giá trị nhỏ nhất")
else:
    print("Hai số bằng nhau")