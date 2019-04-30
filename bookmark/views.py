from django.shortcuts import render

# Create your views here.
# 뷰 종류

# 클래스형 뷰 함수형 뷰는 서로 상호 기능 제약이 거의 없다.
# CRUDL에 특별한 처리를 추가해야 되는 경우.
# 함수형뷰는 자유도가 클래스형 뷰에 비해서 높다.
# 함수형 : def 뷰이름(request[,추가 인수]):
#               처리할 내용
# 처리할 코드를 직접 다 개발자가 작성
#

# 제네릭뷰 상속 받는 이유: 거기 있는 기능이나 내용을 상속 받으려고?
# CRUDL 에 관련 기능은 자주 사용하기 때문에 장고에서 제네릭.
# 클래스형뷰는 생산성이 함수형뷰에 비해 높다.
# 클래스형 : class 뷰이름(제네릭뷰):
#               처리할 내용
# 제네릭 기능 외에 추가적인 기능을 개발자가 작성.
# 메서드 방식 - 커스터마이징에 관련된 메서드를 찾아야 한다.

# CRUD_L
from django.views.generic.list import ListView
#from django.views.generic.edit import Createview

from .models import Bookmark

# 주의사항: 클래스형 뷰의 이름은 자유! abc 이렇게 해도 상관무.
class BookmarkList(ListView):
    model = Bookmark

    # 템플릿 종류를 바꾸거나
    # 읽어오는 데이터를 변경하거나
    # 페이지네이션을 걸거나
    # 검색 쿼리를 적용하거나
    # 권한 체크. 이런 일들을 이 안에서 할 수 있고, 이걸 함수형 뷰에서 할려면 코드를 쭈루룩 다 써야한다.
    # 클래스형뷰와 함수형뷰 서로 왔다갔다 쓸수 있게..

# 뷰를 만들었다 -> URL 연결.
# urls.py 파일 만들기.



# 리스트를 제외한 CRUD를 뷰를 만들고, URL연결까지 해보기.
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class BookmarkCreate(CreateView):
    model = Bookmark
    # fields는 사용자가 입력할 모델 필드를 정하는 것.
    fields = ['site_name','url', 'contents']
    template_name_suffix = '_create'
    success_url = '/'
    # _create
    # _form

class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url', 'contents']
    template_name_suffix = '_update'
    success_url = '/'
    # _update
    # _form

class BookmarkDelete(DeleteView):
    model = Bookmark
    template_name_suffix = '_delete'
    success_url = '/'
    # _delete
    # _confirm_delete

from django.views.generic.detail import DetailView

class BookmarkDetail(DetailView):
    model = Bookmark
    template_name_suffix = '_detail'
    # _detail


# 과제. detail만들고 template 만들고
# _create, _update로 만들어서 해보기?

