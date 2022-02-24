from django.urls import path
from .views import main

app_name="shop_window"

urlpatterns = [
    # path('',main, name="main"),
    # path('detail/<int:pk>/',detail, name="detail")
    # path('',registration, name="registration"),
    path('', main, name='main')
]