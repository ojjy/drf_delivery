"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from customereq import views as customereq_views
from django.conf.urls import url, include

from anoboards import views as anoboard_views
from users import views as user_views
from boards import views as boards_views
from notice import views as notice_views
router = routers.DefaultRouter()
router.register(r'customereqs', customereq_views.CustomereqViewset)
router.register(r'anoboards', anoboard_views.AnonymBoardViewset)
router.register(r'users', user_views.UserViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('request_ship/', customereq_views.CustomereqCreateView.as_view(), name="request_ship"),
    path('request_delete/<int:pk>', customereq_views.CustomereqDeleteView.as_view(), name="request_delete"),
    path('request_update/<int:pk>', customereq_views.CustomereqUpdateView.as_view(), name="request_update"),
    path('request_detail/<int:pk>', customereq_views.CustomereqDetailView.as_view(), name="request_detail"),
    path('request_list', customereq_views.CustomereqListView.as_view(), name="request_list"),

    path('detail/<int:pk>', anoboard_views.AnonymBoardDetailView.as_view(), name='detail'),
    path('create/', anoboard_views.AnonymBoardCreateView.as_view(), name='create'),
    path('delete/<int:pk>', anoboard_views.AnonymBoardDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', anoboard_views.AnonymBoardUpdateView.as_view(), name='update'),
    path('list', anoboard_views.AnonymBoardListView.as_view(), name='list'),

    path('bo_detail/<int:pk>', boards_views.BoardDetailView.as_view(), name='bo_detail'),
    path('bo_create/', boards_views.BoardCreateView.as_view(), name='bo_create'),
    path('bo_delete/<int:pk>', boards_views.BoardDeleteView.as_view(), name='bo_delete'),
    path('bo_update/<int:pk>', boards_views.BoardUpdateView.as_view(), name='bo_update'),
    # path('list', board_views.BoardListView.as_view(), name='list'),
    path('com_detail/<int:pk>', boards_views.CommentDetailView.as_view(), name='com_detail'),
    path('com_create/', boards_views.CommentCreateView.as_view(), name='com_create'),
    path('com_delete/<int:pk>', boards_views.CommentDeleteView.as_view(), name='com_delete'),
    path('com_update/<int:pk>', boards_views.CommentUpdateView.as_view(), name='com_update'),

    path('signup_cbv/', user_views.SinupView.as_view(), name="signup_cbv"),
    path('login/', user_views.login_view, name="login"),
    path('index/', user_views.login_view, name="index"),
    path('logout/', user_views.logout_view, name="logout"),
    path('signup/', user_views.signup_view, name="signup"),
    path('activate/<str:uidb64>/<str:token>/', user_views.activate, name="activate"),
    path('app_login/', user_views.app_login, name="app_login"),

    path('notice_create/', notice_views.NoticeCreateView.as_view(), name="notice_create"),
    path('notice_create_fbv/', notice_views.post, name="notice_create_fbv"),
    path('notice_detail/<int:pk>', notice_views.NoticeDetailView.as_view(), name="notice_detail"),
    path('notice_update/<int:pk>', notice_views.NoticeUpdateView.as_view(), name="notice_update"),
    path('notice_delete/<int:pk>', notice_views.NoticeDeleteView.as_view(), name="notice_delete"),
    path('notice_list', notice_views.NoticeListView.as_view(), name="notice_list"),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

