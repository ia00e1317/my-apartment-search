from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from django.contrib.auth import login
from django.http import HttpResponseRedirect


class SignUpView(generic.CreateView):	#追→
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    #追加　いる？
    def form_valid(self, form):
        user = form.save() # formの情報を保存
        #login(self.request, user) # 認証
        self.object = user 
        return HttpResponseRedirect(self.get_success_url()) # リダイレクト


class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    """パスワード変更ビュー"""
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'accounts/password_change.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # 継承元のメソッドCALL
        context["form_name"] = "password_change"
        return context

class PasswordChangeDone(LoginRequiredMixin,PasswordChangeDoneView):
    """パスワード変更完了"""
    template_name = 'accounts/password_change_done.html'




#class index(LoginRequiredMixin, generic.TemplateView):
#    """メニュービュー"""
#    template_name = 'accounts/top.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs) # 継承元のメソッドCALL
#        context["form_name"] = "top"
#        return context