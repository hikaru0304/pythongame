from tkinter import *

window = Tk()
window.title("My Favorite Baseball Team")           # Tkinter 타이틀명
window.geometry("500x250")                          # 화면 사이즈 크기 구성
window.resizable(False, False)                      # 화면 늘리기 기능 없앰

f = open("data_into.txt", 'r', encoding="UTF-8")    # data_info.txt 파일 읽기모드로 오픈
lines = f.readline()                                # data_info.txt 파일의 첫 번째 줄만 가지고 옴
for line in lines:
    lis = lines.split(":")                          # data_info.txt 내용을 :을 기준으로 나눔

label = ['', '', '', '', '', '']                    # 정보를 출력할 Label을 반복문을 사용하기 위해 리스트 생성(6개의 Lable을 사용하기 때문에 크기가 6인 리스트 생성함)

# 첫 번째 화면 구성
for i in range(0, 6):
    label[i] = Label(text=lis[i])                   # 반복문을 이용해서 리스트에 Lable 내용을 넣음

# 두 번째 화면 구성
lines_2 = f.readlines()                             # data_info.txt 파일의 내용을 전부 읽음
for line in lines_2:
    lis_2 = line.split(":")                         # 파일의 모든 줄을 읽기 때문에 여기서 :을 기준으로 나눠지는 줄은 마지막 줄이 된다.

label[0].pack()                                     # 중앙 상단의 라벨 표시

img = PhotoImage(file="Hanhwa.PNG")                 # 이미지 파일 불러오기
w = Label(window, image=img).pack(side="left")      # 왼쪽에 이미지 표시

# 이미지에 대한 정보를 라벨로 출력
label[1].place(x = 330, y = 40)
label[2].place(x = 330, y = 70)
label[3].place(x = 330, y = 100)
label[4].place(x = 330, y = 140)
label[5].place(x = 330, y = 160)


def previous():                                     # 이전 버튼을 클릭 했을 때 이벤트
    for i in range(0, 6):
        label[i].configure(text=lis[i])             # 다음 버튼 클릭시 첫 번째 화면 구성으로 Lable의 text를 변환

def next():                                         # 다음 버튼을 클릭 했을 때 이벤트
    for i in range(0, 6):
        label[i].configure(text=lis_2[i])           # 다음 버튼 클릭시 두 번째 화면 구성으로 Lable의 text를 변환

# 이전 버튼 구성
button_1 = Button(window, text = "이전", command = previous)
button_1.place(x = 330, y = 200)

# 다음 버튼 구성
button_2 = Button(window, text = "다음", command = next)
button_2.place(x = 435, y = 200)

window.mainloop()