# open() : 파일을 특정한 모드로 여는 함수. 읽을때는 r, 쓸때에는 w
# read() : 파일을 객체로부터 모든 내용을 읽는 함수입니다.
f = open("input.txt","r",encoding="UTF-8")
list = f.readlines()
for i, data in enumerate(list):
    print("%d 번째 줄: %s" %(i+1,data), end='')
f.close()