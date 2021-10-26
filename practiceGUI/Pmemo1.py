from tkinter import *
from tkinter.filedialog import *
import os

es ="" # 편집을 위한 전역변수 선언

def newFile():
    top.title("제목없음-메모장")
    file = None
    ta.delete(1.0,END)
def openFile():
    file = askopenfilename(title="파일 선택",filetypes=(("텍스트 파일","*.txt"),("모든 파일","*.*")))
    top.title(os.path.basename(file)+"- 메모장")
    ta.delete(1.0,END)
    f = open(file,"r")
    ta.insert(1.0,f.read())
    f.close()
def saveFile():
    f = asksaveasfile(mode ="w", defaultextension=".txt")
    if f is None:
        return
    ts = str(ta.get(1.0,END))
    f.write(ts)
    f.close()
def cut():
    global es
    es=ta.get(SEL_FIRST,SEL_LAST)
    ta.delete(SEL_FIRST,SEL_LAST)
def copy():
    global es
    es = ta.get(SEL_FIRST,SEL_LAST)
def paste():
    global es
    ta.insert(INSERT,es)
def delete():
    ta.delete(SEL_FIRST,SEL_LAST)

top = Tk()
top.title("메모장")
top.geometry("400x400")

ta = Text(top)
sb = Scrollbar(ta)
sb.config(command=ta.yview)
sb.pack(side=RIGHT, fill=Y)
top.grid_rowconfigure(0,weight=1)
top.grid_columnconfigure(0,weight=1)
ta.grid(sticky = N +E+S+W) #ta가 동서남북을 다 채우도록 고정

file=None

mb = Menu(top)
fi = Menu(mb, tearoff=0)
fi.add_command(label="새 파일",command=newFile)
fi.add_command(label="열기",command=openFile)
fi.add_command(label="저장")
fi.add_separator()  #분리선 추가
fi.add_command(label="종료")
mb.add_cascade(label="파일",menu=fi)  #파일 메뉴를 메뉴바에 붙이기

e = Menu(mb,tearoff=0)
e.add_command(label="잘라내기")
e.add_command(label="복사")
e.add_command(label="붙이기")
e.add_command(label="삭제")
mb.add_cascade(label="편집",menu=e)   #편집 메뉴를 메뉴바에 붙이기

h = Menu(mb,tearoff=0)
h.add_command(label="메모장 정보")
mb.add_cascade(label="도움말",menu=h) #도움말을 메뉴바에 붙이기

top.config(menu=mb)
top.mainloop()
