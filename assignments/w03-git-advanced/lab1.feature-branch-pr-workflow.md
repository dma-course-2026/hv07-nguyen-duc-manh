# Git Feature Branch & Pull Request Workflow

Bài lab thực hành workflow cơ bản khi làm việc theo mô hình **feature branch + Pull Request**.

Mục tiêu:

```text
main
  ↓
create feature branch
  ↓
edit code
  ↓
commit
  ↓
push branch
  ↓
Pull Request
  ↓
Code Review
  ↓
Merge
  ↓
sync main
```

## Workflow tổng quát

| Bước | Việc làm | Command |
| --- | --- | --- |
| 1 | Chuyển về `main` | `git switch main` |
| 2 | Lấy code mới nhất | `git pull origin main` |
| 3 | Tạo branch cho task | `git switch -c feature/fill-contact` |
| 4 | Sửa code | chỉnh file trong VS Code |
| 5 | Kiểm tra thay đổi | `git status` / `git diff` |
| 6 | Stage | `git add .` |
| 7 | Commit | `git commit -m "Add fill-contact feature"` |
| 8 | Push branch lên GitHub | `git push -u origin feature/fill-contact` |
| 9 | Tạo Pull Request | `feature/fill-contact → main` trên GitHub |
| 10 | Review / sửa nếu cần | sửa → commit → push tiếp |
| 11 | Approve & Merge | merge PR trên GitHub |
| 12 | Đồng bộ local sau merge | `git switch main` → `git pull` |

---

## 1. Chuyển về `main`

Trước khi bắt đầu một task mới, nên quay về branch `main`.

```bash
git switch main
```

Kiểm tra branch hiện tại:

```bash
git branch
```

Ví dụ:

```text
* main
  feature/old-task
```

Dấu `*` cho biết branch hiện tại đang là `main`.

---

## 2. Lấy code mới nhất từ remote

Trước khi tạo branch mới, cần đảm bảo local `main` đang cập nhật theo remote.

```bash
git pull origin main
```

Trong đó:

- `origin` là tên remote mặc định.
- `main` là branch trên remote.
- `git pull` lấy commit mới từ remote và cập nhật branch local hiện tại.

Mental model:

```text
GitHub main
     ↓
origin/main
     ↓
local main
```

Lưu ý:

- `main` là branch local.
- `origin/main` là remote-tracking branch — Git dùng để ghi nhận trạng thái gần nhất của `main` trên remote.

---

## 3. Tạo branch mới cho task

Ví dụ task là làm chức năng login:

```bash
git switch -c feature/fill-contact
```

Lệnh này làm hai việc:

1. Tạo branch mới `feature/fill-contact`.
2. Chuyển sang branch đó.

Có thể kiểm tra:

```bash
git branch
```

Kết quả:

```text
  main
* feature/fill-contact
```

Cú pháp cũ tương đương:

```bash
git checkout -b feature/fill-contact
```

Khuyến nghị dùng `git switch -c` vì rõ nghĩa hơn đối với người mới.

---

## 4. Sửa code

Sau khi đã ở branch riêng, bắt đầu chỉnh sửa code bằng VS Code hoặc editor khác.


Điểm quan trọng:

> Không sửa trực tiếp trên `main`. Mỗi task nên có branch riêng.

---

## 5. Kiểm tra thay đổi

Xem trạng thái working directory:

```bash
git status
```

Xem nội dung đã thay đổi:

```bash
git diff
```

Ví dụ:

```diff
- print("Hello World")
+ print("Hello Login Feature")
```

---

## 6. Stage thay đổi

Stage toàn bộ thay đổi:

```bash
git add .
```

Hoặc chỉ stage một file:

```bash
git add README.md
```

Kiểm tra lại:

```bash
git status
```

---

## 7. Commit

Tạo commit cho thay đổi:

```bash
git commit -m "Add <name> infor"
```

Commit message nên:

- ngắn gọn;
- mô tả đúng thay đổi;
- dùng động từ rõ nghĩa.

Ví dụ:

```text
Add login feature
Fix login validation
Update login documentation
```

---

## 8. Push branch lên GitHub

Lần đầu push branch mới:

```bash
git push -u origin feature/fill-contact
```

Trong đó:

- `origin` là remote;
- `feature/login` là branch cần push;
- `-u` thiết lập upstream tracking.

Sau lần đầu, các lần sau có thể chỉ cần:

```bash
git push
```

Sau bước này:

```text
Local
feature/login
      │
      │ git push
      ▼
GitHub
feature/login
```

---

## 9. Tạo Pull Request

Trên GitHub, tạo Pull Request từ:

```text
feature/login → main
```

Có thể hiểu:

```text
source branch          target branch
feature/login   ─────> main
```

Pull Request là yêu cầu:

> Review các thay đổi trên branch này trước khi merge vào `main`.

Một PR thường có:

- Title
- Description
- Commits
- Changed files
- Reviewer
- Comments
- Status checks
- Merge button

Ví dụ title:

```text
Add login feature
```

---

## 10. Review và sửa nếu cần

Reviewer có thể:

- comment;
- yêu cầu sửa code;
- approve.

Nếu reviewer yêu cầu sửa, **không cần tạo PR mới**.

Chỉ cần sửa code tiếp trên chính branch:

```bash
git add .
git commit -m "Fix in-correct infor"
git push
```

PR hiện tại sẽ tự động cập nhật commit mới.

Flow:

```text
Pull Request
     ↓
Review
     ↓
Request changes
     ↓
Edit code
     ↓
Commit
     ↓
Push
     ↓
Pull Request tự cập nhật
```

---

## 11. Approve & Merge

Khi reviewer approve và các checks đều pass, merge PR vào `main`.

Flow:

```text
feature/fill-contact
      │
      │ Pull Request
      ▼
   Code Review
      │
      ▼
    Approve
      │
      ▼
     Merge
      │
      ▼
     main
```

Sau khi merge, code của task đã trở thành một phần của `main`.

---

## 12. Đồng bộ local sau khi merge

Sau khi PR đã được merge trên GitHub, local `main` của bạn chưa chắc đã có commit mới.

Chuyển về `main`:

```bash
git switch main
```

Pull code mới:

```bash
git pull origin main
```

Sau đó local `main` sẽ đồng bộ với remote.

---

## Xóa branch sau khi hoàn thành

Sau khi PR đã merge, có thể xóa branch local:

```bash
git branch -d feature/fill-contact
```

Nếu remote branch chưa được xóa tự động:

```bash
git push origin --delete feature/fill-contact
```

---

## Full command flow

```bash
# 1. Chuyển về main
git switch main

# 2. Lấy code mới nhất
git pull origin main

# 3. Tạo branch mới cho task
git switch -c feature/login

# 4. Sửa code bằng VS Code

# 5. Kiểm tra thay đổi
git status
git diff

# 6. Stage
git add .

# 7. Commit
git commit -m "Add login feature"

# 8. Push branch
git push -u origin feature/login

# 9. Tạo Pull Request trên GitHub
# feature/login -> main

# 10. Nếu reviewer yêu cầu sửa
git add .
git commit -m "Fix login validation"
git push

# 11. Approve & Merge PR trên GitHub

# 12. Đồng bộ main sau khi merge
git switch main
git pull origin main
```

---

## Mental model

```text
                    GitHub
                       │
                       │
                    main
                      ▲
                      │
                Pull Request
                      │
              feature/login
                      ▲
                      │ git push
                      │
                    Local
```

Một task đi qua flow:

```text
Task
 ↓
Update main
 ↓
Create branch
 ↓
Code
 ↓
Commit
 ↓
Push
 ↓
Pull Request
 ↓
Code Review
 ↓
Fix if needed
 ↓
Approve
 ↓
Merge
 ↓
Sync local main
```

## Nguyên tắc nên nhớ

- Không làm feature trực tiếp trên `main`.
- Trước khi tạo branch mới, cập nhật `main`.
- Một task nên có một branch riêng.
- Commit nhỏ và có ý nghĩa.
- Push branch trước khi tạo Pull Request.
- Nếu PR bị yêu cầu sửa, tiếp tục commit và push trên cùng branch.
- Merge chỉ sau khi review hoàn tất.
- Sau khi merge, quay lại `main` và pull code mới nhất.
