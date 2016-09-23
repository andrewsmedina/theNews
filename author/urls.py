from django.conf.urls import url

from author import views

app_name = 'author'

urlpatterns = [
    url(r'^signin/$', views.SigninView.as_view(), name='signin'),
    url(r'^signout/$', views.SignOutView.as_view(), name='signout'),
    url(r'profile/(?P<pk>[\w-]+)/$', views.ProfileView.as_view(), name='profile'),
    url(r'(?P<pk>[\w-]+)/edit/$', views.ProfileEditView.as_view(),
        name='edit_profile')
]