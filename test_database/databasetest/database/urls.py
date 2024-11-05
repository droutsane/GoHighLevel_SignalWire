from django.urls import path
from database import views


urlpatterns = [
    path('hooks',views.hooks, name='hooks')
]