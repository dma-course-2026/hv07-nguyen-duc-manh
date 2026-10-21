n = int(input("Nhập n: "))

if n < 0:
    print("Không tính được giai thừa của số nguyên âm")
else:
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    print(f"{n} giai thừa = {fact}")