
import os
from openpyxl import Workbook

def write_file_names_to_excel(directory_path, excel_path):
    # 创建Excel文件
    wb = Workbook()
    ws = wb.active

    # 获取目录中的文件名
    file_names = [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]

    # 将文件名写入Excel文件
    for i, file_name in enumerate(file_names, start=1):
        ws.cell(row=i, column=1, value=file_name)

    # 保存Excel文件
    wb.save(excel_path)

# 使用示例
directory_path = 'F:\\婚禮\\婚紗照\\V1'
excel_path = 'F:\\婚禮\\婚紗照\\photo_filenames_0916.xlsx'
write_file_names_to_excel(directory_path, excel_path)