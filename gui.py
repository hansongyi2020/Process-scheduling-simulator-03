from tkinter import *

win = Tk()
win.geometry("300x100")#크기
win.title("what time?")#제목
win.option_add("*Font", "궁서 20")#폰트

def alert():
    print("버튼이 눌림")

btn = Button(win)#버튼 생성
btn.config(text = "한송이")#내용
btn.config(width = 10)#너비
btn.config(command = alert)#

btn.pack()
win.mainloop() 