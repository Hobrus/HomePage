from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('example', views.example, name='example'),
    path('goods', views.goods_view, name='goods')
]
