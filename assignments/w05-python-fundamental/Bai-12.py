dai, rong = map(
    float, input("Nhập chiều dài và chiều rộng: ").split()
)

dien_tich = dai * rong
chu_vi = 2 * (dai + rong)

print(f"Diện tích: {dien_tich:g}")
print(f"Chu vi: {chu_vi:g}")