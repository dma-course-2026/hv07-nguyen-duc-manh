ch = input("Nhập một ký tự: ")

if len(ch) == 1 and (
    'a' <= ch <= 'z' or 'A' <= ch <= 'Z'
):
    print(f"{ch} là ký tự Alphabet")
else:
    print(f"{ch} không phải là ký tự Alphabet")