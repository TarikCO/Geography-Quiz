#Import Djange library named path
from django.urls import path

#Import from views.py all the account views functions
from account.views import (
    registration_view, 
    logout_view,
    login_view,
    account_view,
)

#Create web urls that redirects the user to each of the views rendered
urlpatterns = [
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
    ]





