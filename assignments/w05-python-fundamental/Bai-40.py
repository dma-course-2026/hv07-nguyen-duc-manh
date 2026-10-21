m, n = map(int, input("Nhập M và N (M < N): ").split())

if m >= n:
    print("Điều kiện không hợp lệ: M phải nhỏ hơn N")
else:
    tong = 0

    for i in range(m, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            tong += i

    print(f"Kết quả: {tong}")