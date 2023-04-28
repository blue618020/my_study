# 데이터 수집 단계

# 데이터 수집 -> 데이터 분석/처리 -> 인공지능 모델 학습 -> 인공지능 모델 평가 -> 사용

# http (hypertext transfer protocol)
# request(요청) - response(응답)
# client(클라이언트) - server(서버)
# 클라이언트 : 서버에게 받는 쪽인 사용자 웹브라우저
# 클라이언트가 요청 -> 서버가 받고 응답을 돌려줌 
# 크롤링: 웹페이지로부터 데이터를 추출하는 행위

# html (hypertext markup language) 파싱
# (응답 까보면 나오는거)
# 웹 사이트를 표현하기 위한 언어
# 태그와 태그로 표현함 <html></html>

# import requests

# url = "https://www.naver.com/"
# response = requests.get(url)
# status = response.status_code  # 상태코드
# html = response.text
# print(status)  # 결과: 200
# print(html)

# http 상태코드
# 200 : ok 요청 성공
# 302 : 리다이렉트 다른 페이지로 바로 연결

# 400 : Bad Request 요청이 잘못됨
# 401 : Unauthorizer 비인증됨
# 403 : Forvbidden 접근 권한 없음
# 404 : Not Found 요청받은 내용이 없음
# 405 : Method Nnot Allower 접근 방법이 잘못됨

# 500 : Internal Server Error 서버 에러
# 501 : Not Implemented
# 502 : Bad Gateway 잘못된 응답

# url 구조
# 프로토콜://호스트주소:포트번호/경로 ? 쿼리=검색어
# 쿼리이름=값&쿼리이름=값&
# https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%B9%98%ED%82%A8
# 프로토콜    호스트주소        경로     ?어디인가=이미지           쿼리=값(치킨으로 검색한거임)
# search_url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%B9%98%ED%82%A8" 
# response = requests.get(search_url)
# print(response.text)  # 결과: "'치킨'의 네이버 이미지검색 결과입니다." 라는걸 확인할 수 있음

# import requests
# search_url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=" 
# keyword = "맥주"
# url = search_url + keyword
# response = requests.get(url)
# # print(response.text)  # 결과: "'맥주'의 네이버 이미지검색 결과입니다." 라는걸 확인할 수 있음
# print(type(response.text))  # 결과: <class 'str'>

# BeautifulSoup
# 뷰티풀수프
# html 파싱(parsing)
# html을 객체구조화해서 사용
# 표준 라이브러리가 아니라서 설치해야함 (pip install)
# from bs4 import BeautifulSoup
# html 태그
# <태그이름 속성=속성값>내용</태그이름>
# html = "<html><body>hello</body></html>"
# soup = BeautifulSoup(html, "html.parser") # html을 어떤식으로 읽어낼지(파싱할지)
# print(soup)
# print(type(soup))
# # 결과:
# # <html><body>hello</body></html>
# # <class 'bs4.BeautifulSoup'>

# print(soup.body)
# print(type(soup.body))
# # 결과:
# # <body>hello</body>
# # <class 'bs4.element.Tag'>

# print(soup.body.text)
# print(type(soup.body.text))
# # 결과:
# # hello
# # <class 'str'>

# 구글에서 이미지를 가져오고 저장하는 방법 (복잡;)
# 이미지 주소 가져옴 -> 저장할 파일을 만듬 -> 첫번째 사진부터 끝까지 저장시킴 순서
# import requests
# from bs4 import BeautifulSoup
# search_url = "https://www.google.com/search?tbm=isch&q=" # 구글 이미지 링크
# keyword = "맥주"
# url = search_url + keyword
# response = requests.get(url)
# html = response.text   # 문자열 객체로 들어감
# soup = BeautifulSoup(html, "html.parser")
# imgs = soup.find_all('img')

# import os   # 저장파일 만듬. 파일이름은 imgs
# folder_name = "imgs"
# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)

# for idx, img in enumerate(imgs[1:]):  
#     # 이미지를 하나씩 저장. [1:]인 이유는 0번째 이미지가 구글 로고이기 때문
#     print(idx, "번째 이미지 저장")
#     file_name = f"img_{idx}.jpg"
#     file_path = os.path.join(folder_name, file_name)
#     img_response = requests.get(img['src'])
#     img_data = img_response.content
#     with open(file_path, "wb") as f:
#         f.write(img_data)

# enumerate
# li1 = ["김연아","류현진","손흥민"]
# for name in enumerate(li1):
#     print(name)



# 네이버 IT/과학 뉴스 크롤링 (여기서 좀 이해함)
import requests
from bs4 import BeautifulSoup
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"  # 네이버 IT/과학 뉴스 링크
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}) 
# headers={"User-Agent": "Mozilla/5.0"} --> 네이버가 크롤링을 막아놔서 봇 아닌척 넣은 코드. 크롤링 방지 회피(이걸뚫네)

html = response.text  # html 변수에 텍스트들 긁어온거 넣음
soup = BeautifulSoup(html, "html.parser")
div = soup.body.find('div', attrs={'class': 'list_body'}) # '헤드라인 뉴스'쪽만 가져온 것
headlines = div.find_all('a', attrs={'class': 'cluster_text_headline'})  # 뉴스의 제목이 있는 a 태그만 가져온 것

# 텍스트 파일을 새로 만들어서 뉴스 제목 텍스트를 저장해보기
# crawling_result 폴더의 headline.txt 파일 생성(os)
import os
folder_name = "crawling_result"
if not os.path.exists(folder_name):  # 폴더의 존재가 없을때만 생성하겠다(mkdir)
    os.mkdir(folder_name)
for headline in headlines:  # 반복문을 넣어서 전체 제목을 저장할거임
    file_name = "headline.txt"
    file_path = os.path.join(folder_name, file_name)  # 파일 경로들을 하나로 합치던거
    with open(file_path, "a", encoding='utf-8') as f:  # a 모드로 텍스트 저장
        f.write(headline.text.strip()) # 뉴스 제목의 텍스트만 필요없는 공백 제외해서
        f.write("\n")
