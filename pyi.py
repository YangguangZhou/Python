import os
import time
a=input("请输入编译文件目录：")
b=input("请输入图标目录：")
if b=="":
    c="pyinstaller -F "+a
else:
    c="pyinstaller -F -w "+a+" -i "+b
os.system(c)
print("\nDone")
print('\nPress "exit" to exit the program.\n')
while input()!="exit":
    time.sleep(0.1)
