from django.urls import path
from account.views import SignUp, SignIn, SignOut
urlpatterns = [
    path('sign_up/', SignUp.as_view(), name='sign_up'),
    path('sign_in/', SignIn.as_view(), name='sign_in'),
    path('sign_out/', SignOut.as_view(), name='sign_out'),
]
