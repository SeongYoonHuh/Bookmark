from django.urls import path

from .views import BookmarkList, BookmarkCreate, BookmarkUpdate, BookmarkDetail, BookmarkDelete
# namespace 이름 공간
# 다른 앱들과 url pattern 이름이 겹치는 것을 방지하기 위해서 사용
# namespace라는 인수가 존재.

app_name = 'bookmark'
urlpatterns = [
    # path(url pattern, view, url pattern name),
    # 끝에 콤마는 실수 안하게 항상 넣고..

    # 문법적 차이.
    # 함수형 뷰 : 이름만 씀.
    # 클래스형 뷰 : 이름.as_view()

    # 쿼리스트링 or path방식으로 글을 본다..? -> 서버에게 확정을 시켜줘야 함.
    # <변수명>/ 기본 변수명은 pk 임.
    # converter 종류 : (path, uuid, slug, int, str) => custom converter

    # 위도, 경도? map/127.2222-34.3412/
    # convert -> location
    # map/<location:valu>/

    # converter -> 여기선 int로 변환.
    # detail/abc/
    path('detail/<int:pk>/',BookmarkDetail.as_view(), name='detail'),

    path('delete/<int:pk>/',BookmarkDelete.as_view(), name='delete'),

    path('update/<int:pk>/',BookmarkUpdate.as_view(), name='update'),

    path('create/',BookmarkCreate.as_view(), name='create'),
    path('', BookmarkList.as_view(), name='index'),
]

# 1차와 2차 url 연결.
