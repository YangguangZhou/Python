#SevenDightsDrawV2.py
from turtle import *
from time import*
#绘制数码管间隔
def drawGap():
    penup()
    fd(5)
#绘制单段数码管
def drawLine(draw):
    drawGap()
    pendown() if draw else penup()
    fd(40)
    drawGap()
    right(90)
#根据数字绘制七段数码管
def drawDight(dight):
    drawLine(True) if dight in[2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in[0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if dight in[0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in[0,2,6,8] else drawLine(False)
    left(90)
    drawLine(True) if dight in[0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in[0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if dight in[0,1,2,3,4,7,8,9] else drawLine(False)
    left(180)
    #为绘制后续数字确定位置
    penup()
    fd(20)
#获取要输出的数字
def drawDate(date):
    pencolor("darksalmon")
    for i in date:
        if i=='-':
            write('年',font=("Arial",18,"normal"))
            pencolor("orchid")
            fd(40)
        elif i=='=':
            write('月',font=("Arial",18,"normal"))
            pencolor("gold")
            fd(40)
        elif i=='+':
            write('日',font=("Arial",18,"normal"))
            pencolor("olivedrab")
            fd(40)
        elif i=='/':
            write('时',font=("Arial",18,"normal"))
            pencolor("royalblue")
            fd(40)
        elif i=='*':
            write('分',font=("Arial",18,"normal"))
        else:
            drawDight(eval(i))
def main():
    setup(1250,300,100,200)
    penup()
    fd(-500)
    pensize(5)
    speed(10)
    drawDate(strftime('%Y-%m=%d+%H/%M*',gmtime()))
    hideturtle()
    done()
main()
