# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 15:23:30 2021

@author: DELL
"""

#Thư viện thao tác với các tâp tin và thư mục là thư viện OS :
#Đối với thư mục:
# Các hàm cơ bản của thư mục là:  
# Hiển thị thư mục hiện tại :os.getcwd()
#Thay đổi thư mục hiện tại :os.chdir()
# Danh sách thư mục và file :os.listdir()
# Tạo một thư mục mới :os.mkdir()
# Đổi tên thư mục hoặc tên file:os.rename()
# Xóa bỏ thư mục hoặc file :os.rmdir()
#Đối với file:
# Các hàm cơ bản của file là
# Mở file : fh = open(filepath, mode)
# Đọc nội dung từ file : read([count])
#Ghi nội dung vào file : write()
# Đóng file đã mở : close()
#Đổi tên file : os.rename(old, new)
# Xóa file : os.remove(file)
# 2. Lập trình đọc tất cả tập tin và thư mục con trực tiếp của thư mục gốc ổ đĩa C và in kết quả ra màn hình

import os
print("tất cả các tệp và thư mục trong ổ C:")
path = 'C:\\Users\\MyPC\\Documents'
print(os.listdir(path))
print("")

print("các thư mục:")
list1 = next(os.walk(path))[1]
print(list1)
print("")

print("các tệp:")
list2 = next(os.walk(path))[2]
print(list2)