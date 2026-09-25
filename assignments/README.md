# Weekly Assignments

Thư mục này chứa toàn bộ bài tập hàng tuần của khóa DMA 2026

## 1. Folder Naming

Mỗi tuần tạo một thư mục theo format:

`wXX-topic`

Trong đó:

- `XX`: số tuần, luôn dùng 2 chữ số.
- `topic`: tên chủ đề ngắn gọn, viết thường, dùng dấu `-`.
- Không dùng dấu tiếng Việt.
- Không dùng khoảng trắng.

Ví dụ:

```text
assignments/
├── w02-git/
├── w05-python-basic/
├── w06-numpy/
├── w07-pandas/
├── w08-data-cleaning/
└── w13-sql-basic/
```

Không dùng:

```text
Week 5 Python
tuan5_python
W5-Python
python-week5
```

## 2. File Naming

Tên file nên:

- viết thường;
- không có dấu tiếng Việt;
- không có khoảng trắng;
- dùng `snake_case` cho source code/data file.

Ví dụ:

```text
solution.py
solution.ipynb
queries.sql
customer_analysis.ipynb
architecture.drawio
architecture.png
```

Không dùng:

```text
Bai Tap Tuan 5.py
Final final.ipynb
solution_v2_final_final.py
```

## 3. Branch Naming

Mỗi bài tập phải được thực hiện trên một branch riêng:

```text
hw/wXX-topic
```

Ví dụ:

```text
hw/w05-python-basic
hw/w07-pandas
hw/w13-sql-basic
```

Không làm bài trực tiếp trên `main`.

## 4. Pull Request Naming

Khi nộp bài, tạo Pull Request vào `main`.

PR title:

```text
[WXX] Topic - Student ID
```

Ví dụ:

```text
[W07] Pandas - HV01
[W13] SQL Basic - HV01
```

Thời điểm tạo Pull Request đầu tiên được tính là thời điểm nộp bài.

## 5. Weekly Workflow

Trước khi bắt đầu bài mới:

```bash
git checkout main
git pull
git checkout -b hw/wXX-topic
```

Tạo thư mục bài:

```text
assignments/wXX-topic/
```

Trong quá trình làm:

```bash
git status
git diff
git add .
git commit -m "feat: complete assignment"
```

Khi nộp:

```bash
git push -u origin hw/wXX-topic
```

Sau đó tạo Pull Request:

```text
hw/wXX-topic → main
```

## 6. Revision After Review

Nếu instructor yêu cầu chỉnh sửa:

- Không tạo branch mới.
- Không tạo Pull Request mới.
- Tiếp tục sửa trên branch hiện tại.

Ví dụ:

```bash
git add .
git commit -m "fix: address review feedback"
git push
```

Pull Request hiện tại sẽ tự động cập nhật.

## 7. Suggested Weekly Structure

Tùy loại bài, cấu trúc có thể khác nhau.

### Python / Data

```text
w07-pandas/
├── solution.ipynb
├── README.md
└── data/
```

### SQL

```text
w13-sql-basic/
├── queries.sql
└── README.md
```

### Data Modeling

```text
w17-data-modeling/
├── model.drawio
├── model.png
└── README.md
```

### ML

```text
w28-linear-regression/
├── notebook.ipynb
├── src/
└── README.md
```

## 8. Do Not Commit

Không commit:

```text
.env
API keys
passwords
credentials
.venv/
__pycache__/
.idea/
.vscode/
.ipynb_checkpoints/
```

Không commit dataset lớn hoặc dữ liệu nhạy cảm nếu instructor không yêu cầu.

## 9. Before Submission

Trước khi tạo Pull Request, kiểm tra:

- [ ] Đúng folder `wXX-topic`
- [ ] Đúng branch `hw/wXX-topic`
- [ ] Code/notebook chạy được
- [ ] Output đã được kiểm tra
- [ ] Không có API key/password
- [ ] Không có file môi trường hoặc file rác
- [ ] Commit message có ý nghĩa
- [ ] Pull Request đúng format
