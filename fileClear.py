import os
import shutil

def organize_files(target_dir):
    if not os.path.exists(target_dir):
        print(f"오류: '{target_dir}' 폴더가 존재하지 않아.")
        return

    # 확장자별 분류 폴더 매핑
    extensions_map = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.hwp'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Archives': ['.zip', '.tar', '.gz', '.rar'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp']
    }

    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)

        # 디렉토리는 건너뜀
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for category, exts in extensions_map.items():
            if file_ext in exts:
                category_dir = os.path.join(target_dir, category)
                os.makedirs(category_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(category_dir, filename))
                print(f"이동 완료: {filename} -> {category}/")
                moved = True
                break
        
        if not moved:
            other_dir = os.path.join(target_dir, 'Others')
            os.makedirs(other_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(other_dir, filename))
            print(f"기타 분류: {filename} -> Others/")

    print("모든 파일 정리가 완료되었어!")

# 사용 예시 (경로를 원하는 폴더로 변경해서 사용해)
# organize_files("./test_folder")