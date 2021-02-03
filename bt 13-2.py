# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 19:09:04 2021

@author: DELL
"""

import os
vi_tri = input('Vị trí thư mục: ')
ten_tap_tin = input('Nhập tên tập tin: ') 
textfile = os.path.join(vi_tri, ten_tap_tin + '.txt')
file1 = open(textfile, 'w+')
file1.write(input('Viết gì đó không giấu nha ông nội ko là lỗi đó :D '))
file1.close()