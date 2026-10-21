n = int(input("Nhập n: "))

tong = 0

for i in range(2, n + 1, 2):
    tong += i

print(f"Tổng các số chẵn từ 1 đến {n} = {tong}")