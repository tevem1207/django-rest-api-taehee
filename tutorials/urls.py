from django.urls import path
from . import views

app_name = 'tutorials'

urlpatterns = [
    path('', views.tutorial_list),
    path('<int:pk>', views.tutorial_detail),
    path('<int:pk>', views.tutorial_list_published),
]
