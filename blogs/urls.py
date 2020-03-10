from django.conf.urls import url
from . import views

app_name='blogs'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    #文章列表页面
    url(r'^posts/$',views.posts,name='posts'),
    #单篇文章页面
    url(r'^posts/(?P<post_id>\d+)/$',views.post,name='post'),
    #创建新文章页面
    url(r'^new_post/$',views.new_post,name='new_post'),
    #编辑文章页面
    url(r'^edit_post/(?P<post_id>\d+)/$',views.edit_post,name='edit_post'),
    #个人文章列表
    url(r'^my_posts/$',views.my_posts,name='my_posts'),
]
