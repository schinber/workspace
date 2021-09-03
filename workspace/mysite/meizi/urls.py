from django.conf.urls import url, include

from views import get_girl_pic

urlpatterns = [
    url(r'^get_girl_pic/', get_girl_pic),
]
