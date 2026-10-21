a, b, c = map(int, input("Nhập a, b, c: ").split())

max_val = a

if b > max_val:
    max_val = b

if c > max_val:
    max_val = c

print(f"Giá trị lớn nhất trong 3 số là: {max_val}")