from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.login),
    path("index/",views.index,name='admin'),
    path('signup/',views.signup),
    path('login/',views.login,name='login'),
    path('policy/',views.policy, name='policy'),
    path('logout/',views.userlogout),
    path('delete/<int:id>',views.deletedata),
]
