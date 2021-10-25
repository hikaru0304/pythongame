from tkinter import *

top = Tk()
top.title("계산기")    #제목
top.resizable(False,False) #크기 고정
top.configure(background="pink") #배경색
top.geometry("210x320")
def cal():      #문자열을 수식으로 바꾸어 계산
    val = Entry.get(display)
    result = eval(val)
    display.delete(0,END)
    display.insert(0,result)
def clear(pos): #입력및 결과 삭제
    display.delete(0,END)
def b_press(val):   #숫자와 연산자 입력
    display.insert("end",val)
def ce():
    ms = Entry.get(display)
    x = ''
    for i in range(len(ms)-1):
        x += ms[i]
    display.delete(0,END)
    display.inset(0,x)
def m_cal():    #자주 사용하는 계산
    my = Entry.get(display)
    mc = 12900 * int(my)*0.95
    display.delete(0,END)
    display.insert(0,mc)
def ver():  #기호 바꾸기
    my = Entry.get(display)
    v = int(my) * -1
    display.delete(0,END)
    display.insert(0,v)
display = Entry(top, width =28, justify="right") #숫자가 오른쪽에 나타나도록
display.focus_set() #입력창에 포커스 설정
b_my = Button(top, text='M', width=5)   #첫번째 줄 버튼 생성
b_c = Button(top, text='C', width=5,command = lambda:clear(END))
b_ce = Button(top, text='CE', width=5)
b_e = Button(top, text='=', width=5,command=cal)

b_1 = Button(top, text='1', width=5,command=lambda:b_press('1'))    #두번째 줄 생성
b_2 = Button(top, text='2', width=5,command=lambda:b_press('2'))
b_3 = Button(top, text='3', width=5,command=lambda:b_press('3'))
b_a = Button(top, text='+', width=5,command=lambda:b_press('+'))

b_4 = Button(top, text='4', width=5,command=lambda:b_press('4'))    #세번째 줄 생성
b_5 = Button(top, text='5', width=5,command=lambda:b_press('5'))
b_6 = Button(top, text='6', width=5,command=lambda:b_press('6'))
b_s = Button(top, text='-', width=5,command=lambda:b_press('-'))

b_7 = Button(top, text='7', width=5,command=lambda:b_press('7'))    #네번째 줄 생성
b_8 = Button(top, text='8', width=5,command=lambda:b_press('8'))
b_9 = Button(top, text='9', width=5,command=lambda:b_press('9'))
b_m = Button(top, text='*', width=5,command=lambda:b_press('*'))

b_0 = Button(top, text='0', width=5,command=lambda:b_press('0'))    #다섯번째 줄 버튼 생성
b_v = Button(top, text='+/-', width=5)
b_p = Button(top, text='.', width=5,command=lambda:b_press('.'))
b_d = Button(top, text='/', width=5,command=lambda:b_press('/'))

display.grid(row = 0, column = 0, columnspan=4, pady=10, padx = 4) #입력창 배치
b_my.grid(row=1, column = 0, pady=3) #첫번째 줄 버튼 배치
b_c.grid(row=1, column=1)
b_ce.grid(row=1,column = 2)
b_e.grid(row=1,column = 3)

b_1.grid(row=2,column = 0,pady=3) #두번째 줄 버튼 배치
b_2.grid(row=2,column = 1)
b_3.grid(row=2,column = 2)
b_a.grid(row=2,column = 3)

b_4.grid(row=3,column = 0,pady=3) #세번째 줄 버튼 배치
b_5.grid(row=3,column = 1)
b_6.grid(row=3,column = 2)
b_s.grid(row=3,column = 3)

b_7.grid(row=4,column = 0,pady=3) #네번째 줄 버튼 배치
b_8.grid(row=4,column = 1)
b_9.grid(row=4,column = 2)
b_m.grid(row=4,column = 3)

b_0.grid(row=5,column = 0,pady=3) #다섯번째 줄 버튼 배치
b_v.grid(row=5,column = 1)
b_p.grid(row=5,column = 2)
b_d.grid(row=5,column = 3)

top.mainloop()


