count = int(input("입력하는 학생수가 총 몇명인가요? : "))

print("학생의 이름과 시험 점수를 차례대로 입력하세요!")

mix = []
num = 1


while num <= count :
    print(num,"번째 학생====")
    line = []
    line.append(input("* 이름 : "))
    line.append(int(input("* 점수 : ")))
    num = num + 1
    mix.append(line)
    mix1 = tuple(mix)


mix1_dict = dict(mix1)


flag = True
while flag :
    wanted = input("어떤 학생의 점수가 궁금하신가요? 이름을 입력하세요 : ")
    if wanted in mix1_dict :
        print(wanted,"학생의 점수 :",mix1_dict[wanted],"점")
        print("프로그램 종료합니다.")
        flag = False
    else :
        print("찾는 학생(",wanted,")의 점수가 존재하지 않습니다.")
        print("다시 입력해주세요")
