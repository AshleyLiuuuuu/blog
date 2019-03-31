from django.urls import path
from django.conf.urls import url,include
from . import view,search,search2

urlpatterns = [
    url(r'^hello$',view.hello),
    url(r'^search-form$',search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post',search2.search_post),
    url(r'',include('blog.urls')),
    url(r'',include('comments.urls'))
]