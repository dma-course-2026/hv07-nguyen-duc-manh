a, b, c, d = map(int, input("Nhập a, b, c, d: ").split())

max_val = a

if b > max_val:
    max_val = b

if c > max_val:
    max_val = c

if d > max_val:
    max_val = d

print(f"Giá trị lớn nhất trong 4 số là: {max_val}")