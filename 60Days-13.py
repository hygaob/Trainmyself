#複製檔案

import shutil

w=r"C:\Users\Fish\桌面\workspace"
source=f"{w}\source.txt"
destination_path=f"{w}\destiknation_file.txt"
#copyfile  只會複製文件內容
shutil.copyfile(source,destination_path)

#copy 複製文件描述權限
#copy2 可複製文件內容與文件描述權限

#刪除檔案
import os
import shutil
del_path=r"C:\Users\Fish\桌面\workspace"

#os.remove(f"{del_path}/test.txt")
#刪除空資料夾  只能用在空資料夾
#os.rmdir(f"{del_path}\dirc")

#刪除資料夾及內容  需謹慎使用
#shutil.rmtree(f"{del_path}\dirc")

#丟到資源回收桶
# import send2trash
# send2trash.send2trash(fr"{del_path}\test2.txt")
