n = int(input("Nhập n: "))

tong = 0

for i in range(1, n + 1):
    tong += i

print(f"Tổng từ 1 đến {n} = {tong}")