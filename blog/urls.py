from django.urls import path
from .views import  UserListAPIView, UserCreateAPIView, UserUpdateAPIView, UserDeleteAPIView, UserRetrieveAPIView, \
    ReytingListAPIView, ReytingCreateAPIView, ReytingUpdateAPIView, ReytingDeleteAPIView, ReytingRetrieveAPIView, \
    MockTestListAPIView, MockTestCreateAPIView, MockTestUpdateAPIView, MockTestDeleteAPIView, MockTestRetrieveAPIView, \
    UniversitetListAPIView, UniversitetCreateAPIView, UniversitetUpdateAPIView, UniversitetDeleteAPIView, UniversitetRetrieveAPIView, \
    SozlamalarListAPIView, SozlamalarCreateAPIView, SozlamalarUpdateAPIView, SozlamalarDeleteAPIView, SozlamalarRetrieveAPIView, \
    YutuqListAPIView, YutuqCreateAPIView, YutuqUpdateAPIView, YutuqDeleteAPIView, YutuqRetrieveAPIView

urlpatterns = [

    path('user/', UserListAPIView.as_view()),
    path('user/create', UserCreateAPIView.as_view()),
    path('user/<int:pk>edit', UserUpdateAPIView.as_view()),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view()),
    path('user/<int:pk>/delete', UserDeleteAPIView.as_view()),

    path('reyting/', ReytingListAPIView.as_view()),
    path('reyting/create', ReytingCreateAPIView.as_view()),
    path('reyting/<int:pk>edit', ReytingUpdateAPIView.as_view()),
    path('reyting/<int:pk>/', ReytingRetrieveAPIView.as_view()),
    path('reyting/<int:pk>/delete', ReytingDeleteAPIView.as_view()),

    path('mocktest/', MockTestListAPIView.as_view()),
    path('mocktest/create', MockTestCreateAPIView.as_view()),
    path('mocktest/<int:pk>edit', MockTestUpdateAPIView.as_view()),
    path('mocktest/<int:pk>/', MockTestRetrieveAPIView.as_view()),
    path('mocktest/<int:pk>/delete', MockTestDeleteAPIView.as_view()),

    path('universitet/', UniversitetListAPIView.as_view()),
    path('universitet/create', UniversitetCreateAPIView.as_view()),
    path('universitet/<int:pk>edit', UniversitetUpdateAPIView.as_view()),
    path('universitet/<int:pk>/', UniversitetRetrieveAPIView.as_view()),
    path('universitet/<int:pk>/delete', UniversitetDeleteAPIView.as_view()),

    path('sozlamalar/', SozlamalarListAPIView.as_view()),
    path('sozlamalar/create', SozlamalarCreateAPIView.as_view()),
    path('sozlamalar/<int:pk>edit', SozlamalarUpdateAPIView.as_view()),
    path('sozlamalar/<int:pk>/', SozlamalarRetrieveAPIView.as_view()),
    path('sozlamalar/<int:pk>/delete', SozlamalarDeleteAPIView.as_view()),

    path('yutuq/', YutuqListAPIView.as_view()),
    path('yutuq/create', YutuqCreateAPIView.as_view()),
    path('yutuq/<int:pk>edit', YutuqUpdateAPIView.as_view()),
    path('yutuq/<int:pk>/', YutuqRetrieveAPIView.as_view()),
    path('yutuq/<int:pk>/delete', YutuqDeleteAPIView.as_view()),

]
