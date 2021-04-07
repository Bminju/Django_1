from django.urls import path
from . import views # .은 현재 디렉토리를 말함

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
