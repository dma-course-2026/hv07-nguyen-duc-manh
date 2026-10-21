a, b, c, t, n, m = map(
    int, input("Nhập a b c t n m: ").split()
)

tong_chi_phi = t * a + n * b + m * c

print(f"Tổng chi phí là: {tong_chi_phi}")