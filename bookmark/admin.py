from django.contrib import admin

# Register your models here.
# 관리자 페이지에서 관리할 모델을 등록.
# 관리자 페이지를 커스터마이징.
# 관리자페이지 모양을 바꾼다 ? -> 커스터마이징.

# 옵션 클래스를 만들어서 추가.

# BMI 만들었던 것의 등록 코드 살펴보기..?

from .models import Bookmark

class BookmarkOptions(admin.ModelAdmin):
    list_display = ['id', 'site_name', 'url']
    #list_editable = ['site_name', 'url'] # 왠만한 옵션의 경우 안킴. 실수할 수 있기 때문에.
    #list_filter = ['url'] # 대부분 DateTime필드가 있을 경우 많이 사용.
    search_fields = ['site_name', 'url'] #Foreign Key 필드 같은 가른 테이블을 참조하는 항목은 사용X
    # raw_id_fields : 선택값 -> 입력값으로 바꾸는 역할.
    # 관리자 페이지에 커스텀 페이지 추가.
    # 관리지 페이지에 action 추가.
#admin.site.register(모델)
admin.site.register(Bookmark, BookmarkOptions)

# 그 다음, 관리자 페이지에 들어가서 2-3개 정도 등록해 보기.

# python manage.py runserver
# 이 후 admin 페이지 들어가서 bookmark에 2개정도 등록해보기.







