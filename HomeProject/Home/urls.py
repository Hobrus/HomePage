from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('example', views.example, name='example'),
    path('goods', views.goods_view, name='goods'),
    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('balance', views.balance_view, name='balance')
]
