# Git Merge Conflict Lab

Lab thực hành giúp học viên hiểu **khi nào merge conflict xảy ra**, cách đọc conflict markers, cách resolve conflict trên local và cập nhật lại Pull Request.

## Mục tiêu

Sau lab, học viên có thể:

- Tạo hai branch từ cùng một trạng thái `main`.
- Tạo conflict có chủ đích bằng cách sửa **cùng một dòng theo hai cách khác nhau**.
- Phân biệt **push rejected** với **merge conflict**.
- Đồng bộ `main` vào feature branch.
- Đọc `<<<<<<<`, `=======`, `>>>>>>>`.
- Resolve conflict, commit, push và cập nhật Pull Request.
- Kiểm tra commit graph sau khi xử lý.

---

# Mental model

Merge conflict không xảy ra chỉ vì:

```text
Hai người sửa cùng một file
```

Conflict thường xảy ra khi Git thấy:

```text
Cùng một vùng/ cùng một dòng được thay đổi khác nhau từ cùng một common ancestor
```

Ví dụ Code gốc ban đầu:

```python
print("Hello World")
```

Branch B sửa thành:

```python
print("Hello B")
```

Branch C sửa cùng dòng thành:

```python
print("Hello C")
```

Git có thể nhận ra hai thay đổi khác nhau, nhưng không thể tự quyết định:

```text
Giữ "Hello B"?
Giữ "Hello C"?
Hay tạo một nội dung khác?
```

Khi đó cần developer quyết định.

---

# Kịch bản lab

Ban đầu `main`:

```text
A
│
└── hello.py
```

Nội dung `hello.py`:

```python
print("Hello World")
```

Từ cùng commit `A`, tạo hai branch:

```text
             feature/hello-b
            /
main:  A
            \
             feature/hello-c
```

Sau đó:

```text
feature/hello-b: Hello World → Hello B
feature/hello-c: Hello World → Hello C
```

Branch B được merge vào `main` trước.

Khi branch C muốn merge vào `main`, conflict xuất hiện.

---

# Chuẩn bị

Đảm bảo đang ở repository dùng cho lab.

Kiểm tra:

```bash
git status
```

Chuyển về `main`:

```bash
git switch main
```

Lấy code mới nhất:

```bash
git pull origin main
```


# Bước 1 — Tạo branch B

Từ `main`:

```bash
git switch main
git pull origin main
git switch -c feature/hello-b
```

Sửa `hello.py`:

```python
print("Hello B")
```

Kiểm tra:

```bash
git diff
```

Commit:

```bash
git add hello.py
git commit -m "Change greeting to Hello B"
```

Push:

```bash
git push -u origin feature/hello-b
```

---

# Bước 2 — Tạo branch C từ trạng thái ban đầu

Điểm quan trọng của lab:

> Branch C phải được tạo từ `main` **trước khi thay đổi của B được đưa vào main**.

Nếu đang thực hiện tuần tự một mình, hãy tạo branch C ngay từ commit gốc trước khi merge B.

Ví dụ:

```bash
git switch main
git switch -c feature/hello-c
```

Sửa `hello.py` thành:

```python
print("Hello C")
```

Commit:

```bash
git add hello.py
git commit -m "Change greeting to Hello C"
```

Push:

```bash
git push -u origin feature/hello-c
```

Lúc này graph logic:

```text
             B
            /   feature/hello-b
A ---------- 
            \
             C
              feature/hello-c
```

Trong đó:

```text
A = print("Hello World")
B = print("Hello B")
C = print("Hello C")
```

---

# Bước 3 — Merge branch B vào main

Trên GitHub tạo Pull Request:

```text
feature/hello-b → main
```

Review và merge PR.

Sau khi merge:

```text
             B
            / \
A ----------   M ← main
 \
  C ← feature/hello-c
```

Nội dung `main` lúc này:

```python
print("Hello B")
```

Nhưng branch C vẫn chứa:

```python
print("Hello C")
```

---

# Bước 4 — Tạo Pull Request cho branch C

Trên GitHub tạo PR:

```text
feature/hello-c → main
```

GitHub có thể báo branch có conflict và chưa thể merge trực tiếp.

Nguyên nhân:

```text
Common ancestor:
print("Hello World")

main:
print("Hello B")

feature/hello-c:
print("Hello C")
```

Cả hai phía đã sửa **cùng một dòng theo hai cách khác nhau**.

---

# Bước 5 — Đồng bộ main vào feature/hello-c

Chuyển về branch C:

```bash
git switch feature/hello-c
```

Cập nhật trạng thái remote:

```bash
git fetch origin
```

Kiểm tra graph trước khi merge:

```bash
git log --oneline --graph --decorate --all
```

Sau đó merge `origin/main` vào branch hiện tại:

```bash
git merge origin/main
```

Git sẽ báo conflict, ví dụ:

```text
Auto-merging hello.py
CONFLICT (content): Merge conflict in hello.py
Automatic merge failed; fix conflicts and then commit the result.
```

---

# Bước 6 — Kiểm tra trạng thái conflict

Chạy:

```bash
git status
```

Có thể thấy:

```text
both modified: hello.py
```

Mở `hello.py`.

Git sẽ đánh dấu vùng conflict:

```python
<<<<<<< HEAD
print("Hello C")
=======
print("Hello B")
>>>>>>> origin/main
```

Ý nghĩa:

```text
<<<<<<< HEAD
phần code của branch hiện tại: feature/hello-c

=======
ranh giới giữa hai phiên bản

>>>>>>> origin/main
phần code đến từ main
```

Trong lab này:

```text
HEAD        = Hello C
origin/main = Hello B
```

---

# Bước 7 — Resolve conflict

Developer phải quyết định nội dung cuối cùng.

Có thể chọn B:

```python
print("Hello B")
```

Hoặc chọn C:

```python
print("Hello C")
```

Hoặc kết hợp thành nội dung mới:

```python
print("Hello Team")
```

Trong lab này, dùng:

```python
print("Hello Team")
```

Xóa toàn bộ conflict markers:

```text
<<<<<<< HEAD
=======
>>>>>>> origin/main
```

File cuối cùng chỉ còn:

```python
print("Hello Team")
```

---

# Bước 8 — Đánh dấu conflict đã được resolve

Kiểm tra:

```bash
git diff
```

Stage file:

```bash
git add hello.py
```

Kiểm tra lại:

```bash
git status
```

Sau khi `git add`, Git hiểu rằng developer đã resolve file này.

---

# Bước 9 — Commit kết quả resolve

Commit:

```bash
git commit -m "Resolve greeting conflict with main"
```

Graph lúc này có thể có dạng:

```text
             B -------- M ← main
            /          /
A ----------          /
 \                   /
  C ----------------R ← feature/hello-c
```

`R` là merge commit được tạo khi đưa `origin/main` vào branch C và resolve conflict.

---

# Bước 10 — Push lại feature branch

Push:

```bash
git push
```

Pull Request đang mở trên GitHub sẽ tự động cập nhật.

Không cần tạo PR mới.

Sau khi push:

```text
feature/hello-c
       │
       │ new resolve commit
       ▼
existing Pull Request
       │
       ▼
GitHub kiểm tra lại mergeability
```

Nếu không còn conflict, PR có thể tiếp tục review và merge.

---

# Bước 11 — Merge Pull Request

Sau khi reviewer approve, merge:

```text
feature/hello-c → main
```

Sau đó local đồng bộ lại:

```bash
git switch main
git pull origin main
```

Kiểm tra file:

```bash
cat hello.py
```

Kết quả mong đợi:

```python
print("Hello Team")
```

---

