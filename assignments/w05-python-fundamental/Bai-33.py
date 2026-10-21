import math

x0, y0, R = map(
    float, input("Nhập tâm x0 y0 và bán kính R: ").split()
)
xa, ya = map(float, input("Nhập tọa độ điểm A: ").split())

if R < 0:
    print("Bán kính không hợp lệ")
else:
    d = math.sqrt((xa - x0) ** 2 + (ya - y0) ** 2)

    if abs(d - R) < 1e-9:
        print("Điểm A nằm trên đường tròn")
    elif d < R:
        print("Điểm A nằm trong đường tròn")
    else:
        print("Điểm A nằm ngoài đường tròn")