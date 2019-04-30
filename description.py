"""
description.py

1. 파이썬 프로젝트 만들기
2. 장고 설치 : pip install django
3. 장고 프로젝트 만들기 : django-admin startproject config .
4. DB 초기화 : python manage.py migrate
5. 관리자 계정 생성 : python manage.py createsuperuser
6. 기본 앱 만들기 : python manage.py startapp bookmark
7. config-settings.py의 INSTALLED_APPS 에 추가. : 'bookmark',
   --> 추가 해야 템플릿 폴더 검색, DB 변경사항 추적.

앱
(custom field)
1. Models.py 작성.
   ==> 필드를 만들면 -> DB에 컬럼 -> 컬럼의 데이터 타입, 제약조건
                                        IntegerField, 커스텀필드?   ==> 메뉴얼을 보면서 여러 필드를 알고 필요한 것들을 알아가기.
   (forms.py작성)
        ---> 오늘 만들 Bookmark: site_name, url, created 등.
        ---> User모델 있다 가정시. username, password, first_name, last_name, created
        (---> 비밀번호 한번더 입력받는 check용으로 사용하는 것들? DB에 no저장, 추가로 입력받는 것들.?)
2. views.py 작성.
   (context_processor 작성) : 모든 페이지(템플릿 파일 전체)에 출력될 내용.
        --> ex) 장바구니, user
   (custom template tag)
        --> 템플릿 엔진에서 지원하는 태그 외에, 개발자가 추가로 필요한 기능.
3. urls.py 작성.
4. template 만들기.

"""


"""
검색 엔진 최적화 관련
SEO - Search Engine Optimization

HTML 표준에 맞춰
Meta Tag               --> 토렌트로 파일 검색할때 관련 내용이 없어도 구글 사이트 목록에 뜨도록 하는거..
OpenGraph

ex) supple toner 검색한다 했을때, 서평, 가격, 등등.. 
# 구글에서 검색이 잘되게 하려면 이걸 추가?
# 이건 프론트 사람들이 짠다?
# 여기에 뿌려줄 내용은 우리가 알고 있어야 함.
# meta description --> 일정 길이 이상이면(250자) 처리를 안한다..? 를 알아야 항목을 만들고 관리자 페이지를 제어 가능하다?

# 책관련 - 검색 엔진 최적화 A to Z -> 읽어만 보기. 사진 말고.
# 흥마리오의 워드프레스 SEO 구글 검색엔진최적화

# SEO방법은 시즌별로 구글에서 바꿈. 
# 메타태그를 어떻게 넣을지에 대한 자동화가 있다?

# 이쪽은 계속해서 최신화된 글을 봐야함.

"""




"""
localhost/bookmark/1 : 글보기, 수정, 삭제   # 1번
localhost/bookmark/create : 글쓰기         # 2번

'bookmark<int:value>'/   # 1번은 되는데 2번은 안된다?
int: 정수
str: 문자(default)
uuid: application 호출 할때 사용.
slug: why-so-serius => SEO때문에 많이 사용.
path: 'bookmark<value>'/ => bookmark/19/04/29/ 등으로 매칭 가능.

'bookmark<value>'/      # 둘다 매칭이 되서 원하는대로 매칭이 안됨.

위의 기본 converter를 제외한 형태가 필요하다면 custom converter를 만든다.


"""




"""
추가, 수정, 삭제의 경우 해당 기능을 완료한 후에 이동할 페이지가 필요하다.
1) success_url 이라는 속성값을 지정.
2) model에 get_absolute_url이라는 메서드를 만든다.
3) 


"""




"""
<<20190430(화)>>

배포 Deploy : 서버에 올린다.
1) Pythonanywhere /w Github
1-1) github에 소스코드를 업로드, requirements도 같이.
1-2) pythonanywhere.com에 가입.   -->  https://www.pythonanywhere.com/user/hsy2763/
    -> 우선 github repository 만듬.(wps_bookmark)

2) Heroku
3) AWS Linux FTP
4) AWS EB
5) Docker

"""











