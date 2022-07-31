from django.urls import path
from music import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'json/', views.getJson),
    path('index/', views.Index),
    path('post/', views.postJson),
]
