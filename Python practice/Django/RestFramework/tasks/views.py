from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import logout
from account.mixins import LogoutRequiredMixin
from account.utils import account_activation_token
User = get_user_model()
import logging  # noqa: E402
logger = logging.getLogger(__name__)
# Create your views here.

class TaskListView(LoginRequiredMixin, generic.View):
    def get(self, request):
        return render(request, 'tasks/task_list.html')
    

