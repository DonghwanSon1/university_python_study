print("지금부터 달리기 시합을 시작하겠습니다.")

count = int(input("\n달리기 선수가 총 몇명인가요? : "))

players = []
num = 1

while num <= count :
    players.append(input("\n지금 들어온 선수 이름을 입력하세요 : "))
    num = num + 1

print("\n달리기 시합 결과!!\n")

index = 0
for score in players :
    print(index+1,"등",score)
    print("")
    index += 1

print("\n수고 많았습니다. 여러분!!")
