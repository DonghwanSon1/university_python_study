mrn = input('의무기록번호')
p_name = input('환 자 성 명')
p_sid1 = input('주 민 번 호 앞 자 리')
p_sid2 = input('주 민 번 호 뒷 자 리')
p_zipcd = input('우 편 번 호')
p_adrs = input('상 세 주 소')

#시스템 종료 함수
import time
p_year1 = int(p_sid1[0:2])+1900
p_year2 = int(p_sid1[0:2])+2000
p_day1 = int(p_sid1[4:7])

#윤년 계산
#윤년일땐 윤년이라 하고 윤년이 아닐시 29일을 입력하면 5초후 종료하게 만듬
#1900년대 윤년
if int(p_sid2[0]) == 1 and 2 and 5 and 6 :
    if(p_year1 % 4 == 0 and (p_year1 % 100 != 0 or p_year1 % 400 == 0)) :
        print("\n윤년입니다")
    elif p_day1 == 29 :         
        print("윤년이 아닙니다. 다시 실행하세요")
        print("5초 후에 꺼집니다.")
        time.sleep(5)
        sys.exit(1)        
    else :
        print(p_year1,"년도는 윤년이 아닙니다.")
#2000년대 윤년
else :
    if(p_year2 % 4 == 0 and (p_year2 % 100 != 0 or p_year2 % 400 == 0)) :
        print("\n윤년입니다")
    elif p_day1 == 29 :         
        print("\n윤년이 아닙니다. 다시 실행하세요")
        print("5초 후에 꺼집니다.")
        time.sleep(5)
        sys.exit(1)
    else :
        print("")
        print(p_year2,"년도는 윤년이 아닙니다.")

#현재 날짜 함수
from datetime import datetime
now = datetime.now()

p_year = int(p_sid1[0:2])
p_month = int(p_sid1[2:4])
p_day = int(p_sid1[4:7]) 
#1900년대 현재 날짜함수를 이용해서 계산
def number(age):
    a = now.year
    b = 1900+age
    if now.month < p_month :
        print("만",a-b-1,"살입니다.")
    elif now.month == p_month :
         if now.day >= p_day : 
            print("만",a-b,"살입니다.")
         else :
            print("만",a-b-1,"살입니다.")
    else :
          print("만",a-b,"살입니다.")
#2000년대 현재 날짜 함수를 이용해서 계산
def number1(age):
    a=now.year
    b=2000+age
    if now.month < p_month :
        print("만",a-b-1,"살입니다.")
    elif now.month == p_month :
         if now.day >= p_day : 
            print("만",a-b,"살입니다.")
         else :
            print("만",a-b-1,"살입니다.")
    else :
          print("만",a-b,"살입니다.")


#함수를 이용해서 나이계산
if int(p_sid2[0]) == 1 :
    number(p_year)
    print("1900년대 남자입니다.")
elif int(p_sid2[0]) == 2 :
    number(p_year)
    print("1900년대 여자입니다.")
elif int(p_sid2[0]) == 3:
    number1(p_year)
    print("2000년대 남자입니다.")
elif int(p_sid2[0]) == 4:
    number1(p_year)
    print("2000년대 여자입니다.")
elif int(p_sid2[0]) == 5:
    number(p_year)
    print("1900년대 외국인 남자입니다.")
elif int(p_sid2[0]) == 6:
    number(p_year)
    print("1900년대 외국인 여자입니다.")
elif int(p_sid2[0]) == 7:
    number1(p_year)
    print("2000년대 외국인 남자입니다.")
elif int(p_sid2[0]) == 8:
    number1(p_year)
    print("2000년대 외국인 여자입니다.")
else :
    print("주민번호 뒷자리 확인해주세요")
print('\n입력 하신 정보는 아래와 같습니다.'
      '\n┎━━━━━━━━━━━━━━━━-┒'
      '\n┃의무기록번호: ',mrn,'         ┃',
      '\n┃------------------------------   ┃',
      '\n┃환 자 성 명 : ',p_name,'           ┃',
      '\n┃------------------------------   ┃',
      '\n┃주 민 번 호 : ',p_sid1,'-',p_sid2,' ┃',
      '\n┃------------------------------   ┃',
      '\n┃우 편 번 호 : ',p_zipcd,'            ┃',
      '\n┃------------------------------   ┃',
      '\n┃상 세 주 소 : ',p_adrs,'           ┃',
      '\n┖━━━━━━━━━━━━━━━━-┚')
