print("전체 책 목록\n")
books = []
books.append({"제목":"개발자의 코드","출판 연도":"2013.02.28","출판사":"A","쪽수":200,"추천 유무":False})
books.append({"제목":"클린 코드","출판 연도":"2010.03.04","출판사":"B","쪽수":584,"추천 유무":True})
books.append({"제목":"빅데이터 마케팅","출판 연도":"2014.07.02","출판사":"A","쪽수":296,"추천 유무":True})
books.append({"제목":"구글드","출판 연도":"2010.02.10","출판사":"B","쪽수":526,"추천 유무":False})
books.append({"제목":"강의력","출판 연도":"2013.12.12","출판사":"A","쪽수":248,"추천 유무":True})

index = 0
for book1 in books:
    print(book1)
    index += 1

many_page = []
recommends = []
all_pages = int()
pub_company = set()

for book in books:
    if book["쪽수"] > 250 :
        many_page.append(book["제목"])
    if book["추천 유무"] == True :
        recommends.append(book["제목"])
    all_pages += book["쪽수"]
    pub_company.add(book["출판사"])
one_many_page = [(book["제목"])for book in books if book["쪽수"] > 250]

print("\n쪽수가 250쪽 넘는 책 리스트 :", many_page)
print("\n내가 추천하는 책 리스트 :", recommends)
print("\n내가 읽은 책 전체 쪽수 :", all_pages)
print("\n내가 읽은 책의 출판사 목록 :",pub_company)
print("\n한 줄로 만든 쪽수가 250 쪽 넘는 책 리스트 :", one_many_page)
