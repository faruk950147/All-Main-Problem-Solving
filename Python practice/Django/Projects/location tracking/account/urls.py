from django.urls import path
from account.views import SignUpView, SignInView, SignOutView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('sign/', SignInView.as_view(), name='sign'),
    path('signout/', SignOutView.as_view(), name='signout'),
]
