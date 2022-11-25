from django.urls import re_path as url, include, path
from django.contrib.auth import views as auth_views
from accounts import views as acc_views
from rest_framework.routers import DefaultRouter
from accounts import views

router = DefaultRouter()
router.register(r'account', views.AccountsViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    path('', acc_views.home, name='Home'),
    path('register/', acc_views.sign_up, name='Register'),
    path('login/', acc_views.sign_in, name='Login'),
    path('logout/', acc_views.log_out , name='Logout')
]