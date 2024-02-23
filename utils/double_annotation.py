import os
import json
import shutil

# 원본 디렉토리 경로와 복사할 디렉토리 경로를 설정합니다.
src_dir = "../data/train/outputs_json"
dst_dir = "../data/train/outputs_json"

# 원본 디렉토리 안의 각 디렉토리를 순회합니다.
for dir_name in os.listdir(src_dir):
    src_sub_dir = os.path.join(src_dir, dir_name)
    if os.path.isdir(src_sub_dir):
        # 디렉토리 이름에서 'ID0'를 'ID1'로 변경합니다.
        new_dir_name = dir_name.replace("ID0", "ID1")
        dst_sub_dir = os.path.join(dst_dir, new_dir_name)

        # 새 디렉토리를 생성합니다.
        os.makedirs(dst_sub_dir, exist_ok=True)

        # 디렉토리 내의 json 파일들을 순회합니다.
        for file_name in os.listdir(src_sub_dir):
            if file_name.endswith(".json"):
                src_file_path = os.path.join(src_sub_dir, file_name)
                dst_file_path = os.path.join(dst_sub_dir, file_name)

                # json 파일을 로드합니다.
                with open(src_file_path, "r") as json_file:
                    data = json.load(json_file)

                # points의 좌표의 0번째 index 값을 2048에서 뺀 값으로 변경합니다.
                for annotation in data["annotations"]:
                    for i in range(len(annotation["points"])):
                        annotation["points"][i][0] = 2048 - annotation["points"][i][0]

                # 변경된 데이터를 새 디렉토리에 json 파일로 저장합니다.
                with open(dst_file_path, "w") as json_file:
                    json.dump(data, json_file)
