from django.urls import re_path, path
from polls import views

app_name = 'poll'
urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('<int:pk>/results/', views.ResultView.as_view(), name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote"),
]

