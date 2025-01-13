import os

# 파일을 생성할 폴더 경로
folder_path = "./solutions"

# 6001번부터 6098번까지의 파일 이름 리스트
file_names = [f"{i}.py" for i in range(6001, 6099)]  # 6001.py ~ 6098.py

# 폴더가 없으면 생성
os.makedirs(folder_path, exist_ok=True)

# 파일 생성
for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w") as f:
        # 각 파일에 기본 내용 작성
        f.write(f"# CodeUp Problem {file_name}\n\n")

print("6001번부터 6098번까지의 파일 생성 완료!")
