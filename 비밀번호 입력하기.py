def check_pwd(number1) :
    number = '1234'
    global flag
    if number == number1 :
        print("정확한 비밀번호입니다!!")
        flag = False
    else :
        print("비밀번호가 틀렸습니다. 다시 시도하시오.")
        


flag = True
while flag :
    number1 = input("비밀번호 4자리를 입력하세요 : ")
    check_pwd(number1)
