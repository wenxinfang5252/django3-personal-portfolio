from django.urls import path
from . import views #indicates this folder's view

app_name = 'blog' #specify the app name 

urlpatterns = [
    path('', views.all_blogs, name = 'all_blogs'), #if nothing provided, show all_blogs
    path('<int:blog_id>/', views.detail, name = 'detail'),#match the interger given
]
