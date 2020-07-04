from django.urls import path, include
from django.conf.urls.static import static
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blog , name='all_blog'),
    path('<int:blog_id>/', views.details , name='details'),
]