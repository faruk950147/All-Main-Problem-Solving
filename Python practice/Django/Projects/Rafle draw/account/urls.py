from django.urls import path
from account.views import Sign_up, Sign_in, Sign_out
urlpatterns = [
    path('sign_up/', Sign_up.as_view(), name='sign_up'),
    path('sign_in/', Sign_in.as_view(), name='sign_in'),
    path('sign_out/', Sign_out.as_view(), name='sign_out'),
]
