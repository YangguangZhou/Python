from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter.ttk import *
import ctypes

#解决高分辨率下模糊的问题
#调用api设置成由应用程序缩放
ctypes.windll.shcore.SetProcessDpiAwareness(1)
#调用api获得当前的缩放因子
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)

def OpenTxt():
    OpenPath=str(filedialog.askopenfilename(title='上传文件',filetypes=[('文本文档', '.txt')]))
    f=open(OpenPath,'r',encoding='utf-8')
    txt=f.read()
    TextInput.delete('0.0', END)
    TextInput.insert(END,txt)

def SaveTxt():
    textvar=TextInput.get('0.0',END)
    SavePath=str(filedialog.asksaveasfilename(title='保存文件',defaultextension='.txt',filetypes=[('文本文档', '.txt')]))
    f=open(SavePath,'w',encoding='utf-8')
    f.write(textvar)
    messagebox.showinfo('保存结果','保存成功！')

def GetText():
    global textvar
    global text
    textvar=TextInput.get('0.0',END)
    if textvar=='':
        messagebox.showerror('错误','输入不可为空！')
    else:
        j=0
        text=''
        for i in textvar:
            j+=1
            if (j%2!=0) or (i in '~~!@#$%^&*()_+{}|:"<>?`-=[]\;,./ \n')or(i in'~！@#￥%……&*（）——+{}|：“”《》?·-=【】、；’‘，。/ '):
                text=text+i
            else:
                text=text+'_'
        scrt.config(state=NORMAL)
        scrt.delete('0.0', END)
        scrt.insert(END,text)
        scrt.config(state=DISABLED)
        TextCheck.delete('0.0', END)
        TextCheck.config(state=DISABLED)

def StartRecite():
    TextInput.config(state=NORMAL)
    TextInput.delete('0.0', END)
    TextInput.config(state=DISABLED)
    scrt.config(state=NORMAL)
    scrt.delete('0.0', END)
    scrt.config(state=DISABLED)
    TextCheck.config(state=NORMAL)
    TextCheck.delete('0.0', END)
    
def CheckText():
    checktext=TextCheck.get('0.0',END)
    if checktext=='':
        messagebox.showerror('错误','输入不可为空！')
    else:
        if checktext==textvar:
            messagebox.showinfo('检查结果','全对了，真棒！')
        else:
            messagebox.showinfo('检查结果','有错哦，继续加油！')
        TextInput.config(state=NORMAL)
        TextInput.delete('0.0',END)
        TextInput.insert(END,textvar)
        scrt.config(state=NORMAL)
        scrt.insert(END,text)
        scrt.config(state=DISABLED)
        TextCheck.config(state=DISABLED)

def New():
    TextInput.config(state=NORMAL)
    TextInput.delete('0.0',END)
    TextInput.config(state=NORMAL)
    scrt.config(state=NORMAL)
    scrt.delete('0.0',END)
    scrt.config(state=DISABLED)
    TextCheck.config(state=NORMAL)
    TextCheck.delete('0.0',END)
    TextCheck.config(state=DISABLED)

def ShowInfo():
    hard=messagebox.askokcancel('程序介绍','你是否觉得背诵很困难呢?')
    if hard:
        messagebox.showinfo('程序介绍','那是你没用对方法！快来试试这个程序吧！\n\n背个X啊会去掉一部分文字，留下一些提示，辅助背诵，让背诵更轻松！')
    else:
        messagebox.showinfo('程序介绍','你也可以试试这个程序来提高你背诵的效率！\n\n背个X啊会去掉一部分文字，留下一些提示，辅助背诵，让背诵更轻松，效率更高！')

def ShowMyInfo():
    messagebox.showinfo('作者信息','YangguangZhou \n https://jzhome.vercel.app/')

def Exit():
    win.quit()
    win.destroy()
    exit()

win=Tk()
win.title('背个X啊')
win.iconbitmap('resources/logo.ico')

MenuBar=Menu(win)
win.config(menu=MenuBar)
FileMenu=Menu(MenuBar,tearoff=0)
FileMenu.add_command(label='新建',command=New)
FileMenu.add_command(label='保存',command=SaveTxt)
FileMenu.add_command(label='退出',command=Exit)
MenuBar.add_cascade(label='文件',menu=FileMenu)
MoreMenu=Menu(MenuBar,tearoff=0)
MoreMenu.add_command(label='程序介绍',command=ShowInfo)
MoreMenu.add_command(label='作者信息',command=ShowMyInfo)
MenuBar.add_cascade(label='更多',menu=MoreMenu)

tabControl=ttk.Notebook(win)
tab1=ttk.Frame(tabControl) 
tabControl.add(tab1,text='原文')
tab2=ttk.Frame(tabControl)
tabControl.add(tab2,text='背诵')
tab3=ttk.Frame(tabControl)
tabControl.add(tab3,text='检查')
tab4=ttk.Frame(tabControl)
tabControl.add(tab4,text='帮助')
tabControl.pack(expand=1,fill="both")

ShowText=ttk.LabelFrame(tab1,text='原文')
ShowText.grid(row=0,column=0,padx=8,pady=4)
TextInput=scrolledtext.ScrolledText(ShowText,width=100,height=20)
TextInput.config(state=NORMAL)
TextInput.grid(row=1,column=0)
OpenButton=Button(ShowText,text='打开文件',command=OpenTxt)
OpenButton.grid(row=2,column=0)
EnterButton=Button(ShowText,text='输入完成',command=GetText)
EnterButton.grid(row=3,column=0)

Recite=ttk.LabelFrame(tab2,text='背诵')
Recite.grid(row=0,column=0,padx=8,pady=4)
scrt=scrolledtext.ScrolledText(Recite,width=100,height=22)
scrt.config(state=DISABLED)
scrt.grid(row=1,column=0)
StartButton=Button(Recite,text='背诵完成',command=StartRecite)
StartButton.grid(row=2,column=0)

Check=ttk.LabelFrame(tab3,text='检查')
Check.grid(row=0,column=0,padx=8,pady=4)
TextCheck=scrolledtext.ScrolledText(Check,width=100,height=22)
TextCheck.config(state=DISABLED)
TextCheck.grid(row=1,column=0)
CheckButton=Button(Check,text='默写完成',command=CheckText)
CheckButton.grid(row=2,column=0)

Help=ttk.LabelFrame(tab4,text='帮助')
Help.grid(row=0,column=0,padx=8,pady=4)
h=scrolledtext.ScrolledText(Help,width=100,height=23,relief=FLAT)
ht='''1、输入文本\n
进入“原文”界面，可以自己输入文字，也可以点击“打开文件”按钮打开.txt文本文档。完成后点击“输入完成”准备开始背诵。\n
2、自主背诵\n
点击“输入完成”后，进入背诵界面，该程序会将文本挖空。自主背诵完成后点击“背诵完成”，准备开始默写。\n
3、默写\n
当点击“背诵完成”后，输入的原文及背诵时的提示将会被全部清空，直到在“检查”中点击“默写完成”按钮（如图）。\n
在“检查”页面的文本框中输入自己所背诵的内容，完成后点击“默写完成”结束默写。之后，程序将会检查默写内容，以提示框形式显示检查结果（如图）。\n
此时，输入的原文及背诵时的提示将会重新显示。\n
4、更多功能\n
在菜单栏上，在“文件”选项中可以点击“新建”按钮清空所有内容，也可以点击“保存”按钮将输入的文本保存为.txt的文本文档，点击“退出”后程序将停止运行'''
h.config(state=DISABLED)
h.grid(row=1,column=0)
h.config(state=NORMAL)
h.insert(END,ht)
p1=PhotoImage(file="resources/help/1.gif")
h.image_create('4.0',image=p1)
p2=PhotoImage(file="resources/help/2.gif")
h.image_create('8.0',image=p2)
p3=PhotoImage(file="resources/help/3.gif")
h.image_create('12.0',image=p3)
p4=PhotoImage(file="resources/help/4.gif")
h.image_create('14.0',image=p4)
p5=PhotoImage(file="resources/help/5.gif")
h.image_create('20.0',image=p5)
h.config(state=DISABLED)

win.mainloop()
