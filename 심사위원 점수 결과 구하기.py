print("5명의 평가 점수를 입력하세요! (100점 만점)")

score = []
max_score = 0
min_score = 100


for i in range(0,5,1) :
    i = int(input("점수 입력 : "))
    if i <= 100 :
        score.append(i)
    else :
        print("100점이 최고점수 입니다.")
        i = int(input("점수 입력 : "))
        score.append(i)
print("\n##총 입력 점수##")
for a in score :
    print(a,"점")

print("\n##제거 대상 점수##")
max_score = max(score)
print("-최고 점수 :",max_score,"점")

min_score = min(score)
print("-최소 점수 :",min_score,"점")

score.remove(max(score))
score.remove(min(score))

print("\n##최종 입력 점수##")
for a in score :
    print(a,"점")

print("-----------------------")

sum1 = sum(score)
avg = sum1/len(score)
print("총점 :",sum1,"점")
print("평균 :",round(avg,2),"점") 
