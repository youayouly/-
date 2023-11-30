import os
import shutil

def create_empty_folders(source_folder, destination_folder):
    # 获取源文件夹下的所有文件夹及子文件夹
    for root, dirs, files in os.walk(source_folder):
        for dir_name in dirs:
            source_path = os.path.join(root, dir_name)
            # 构建目标文件夹中相同的子文件夹路径
            destination_path = source_path.replace(source_folder, destination_folder, 1)
            os.makedirs(destination_path)

def copy_small_files(source_folder, destination_folder, max_file_size_mb=100):
    # 获取源文件夹下的所有文件
    for root, dirs, files in os.walk(source_folder):
        for file_name in files:
            source_path = os.path.join(root, file_name)
            
            # 获取文件大小（以MB为单位）
            file_size_mb = os.path.getsize(source_path) / (1024 * 1024)
            
            # 如果文件大小小于指定的阈值，复制到目标文件夹
            if file_size_mb < max_file_size_mb:
                destination_path = source_path.replace(source_folder, destination_folder, 1)
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)  # 确保目标文件夹存在
                shutil.copy2(source_path, destination_path)

# 用法示例
source_directory = "C:\\Users\\Administrator\\Desktop\\thought"
destination_directory = "C:\\Users\\Administrator\\Desktop\\thought1"

create_empty_folders(source_directory, destination_directory)
copy_small_files(source_directory, destination_directory)
