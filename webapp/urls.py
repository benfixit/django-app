from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='index'),
    url(r'^list/$', views.ListOfUsers.as_view(), name='listings'),
    url(r'^add/$', views.UserFormView.as_view(), name='add-user')
]