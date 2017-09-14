import shutil
import os
from _io import StringIO, BytesIO
fso = BytesIO(bytes('1111',encoding='utf-8'))
# help(open)
# help(StringIO)
# help(BytesIO)
shutil.copyfile('C:/Users/YCH/Desktop/txt.txt','C:/Users/YCH/Desktop/copy1.txt')
with open('C:/Users/YCH/Desktop/copy2.txt', 'wb') as ft2:
    ft2.write(fso.read(1024*16))
    
with open('C:/Users/YCH/Desktop/txt.txt', 'rb') as ft3:
    with open('C:/Users/YCH/Desktop/copy3.txt', 'wb') as ft4:
        ft4.write(ft3.read(1024*16))
# with open('/path/to/file', 'r') as f:
#     print(f.read())
#     
#     """字节流"""
# with open('/path/to/file', 'rb') as f:
#     print(f.read())
# """with as ������ṹ:
# try:
#     f = open('/path/to/file', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
# """
# with open('/Users/michael/test.txt', 'w') as f:
#     f.write('Hello, world!')
# with open('/Users/michael/test.txt', 'wb') as f:
#     f.write('Hello, world!')
    

