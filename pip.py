import os
import time
a=input("请输入要安装库的名称或安装命令：")
if a[1:11]!="pip install":
    b="pip install "+a+" -i https://pypi.tuna.tsinghua.edu.cn/simple"
else:
    b=a
os.system(b)
print("\nDone")
time.sleep(1)
