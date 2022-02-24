from django.urls import path
from .views import (
    registration,
    account_confirm,
    account,
    edit_request,
    change_email,
    change_password
    )


app_name="authe"

urlpatterns = [
    # path('',main, name="main"),
    # path('detail/<int:pk>/',detail, name="detail")
    path('registration/',registration, name="registration"),
    path('code/<str:code>/',account_confirm,name ="account_confirm"),
    path('account/',account,name ="account"),
    path('edit_request/',edit_request,name="edit_request"),
    path('email/<str:code>/',change_email,name="email"),
    path('password/<str:code>/',change_password,name="password"),
]