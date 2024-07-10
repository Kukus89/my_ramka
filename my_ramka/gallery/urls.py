from django.urls import path, include
from gallery import views

app_name = "gallery"

urlpatterns = [
    path('', views.IndexListView.as_view(), name="index"),
    path('create/', views.PostCreateView.as_view(), name="post"),
]
