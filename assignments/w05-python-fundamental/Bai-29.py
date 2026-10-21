n = int(input("Nhập năm: "))

if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
    print(f"Số ngày của năm {n} là 366")
else:
    print(f"Số ngày của năm {n} là 365")