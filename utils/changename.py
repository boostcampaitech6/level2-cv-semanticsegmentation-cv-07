import os

# 변경하려는 디렉토리 경로를 지정합니다.
dir_path = "../data/test/DCM"

# 디렉토리 내의 모든 하위 디렉토리를 순회합니다.
for dir_name in os.listdir(dir_path):
    # 디렉토리 이름이 'ID'로 시작하는 경우
    if dir_name.startswith("ID"):
        # 원래 디렉토리의 전체 경로
        original_dir = os.path.join(dir_path, dir_name)
        # 변경할 디렉토리의 전체 경로
        new_dir = os.path.join(dir_path, "ID0" + dir_name[2:])
        # 디렉토리 이름을 변경합니다.
        os.rename(original_dir, new_dir)
