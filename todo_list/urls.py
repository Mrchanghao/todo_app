# from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # name이 url 값으로 이용된다
    # template 에서 url을 이용하여 변수로 설정됨
    # {% url 'about' %} <a class="nav-link" href="{% url 'about' %}">About</a>
    # url path 가 변경 되더라도 template을 다시 설정 하지 않아도 된다.
    path('about/', views.about, name="about"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('completed/<list_id>', views.completed, name="completed"),
    path('uncompleted/<list_id>', views.uncompleted, name="uncompleted"),
    path('edit/<list_id>', views.edit, name="edit"),
]
