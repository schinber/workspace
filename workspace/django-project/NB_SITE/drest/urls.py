from django.conf.urls import url
from drest import views

urlpatterns = [
    url(r'^test/$', views.test),
]
