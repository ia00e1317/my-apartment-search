from django import forms
from .models import Article

from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse

from .models import SimplePhoto

from django.contrib.auth.models import User
#from django.shortcuts import get_object_or_404
#from django.contrib.auth import get_user_model User = get_user_model()
from django.shortcuts import render, get_object_or_404, redirect

class SearchForm(forms.Form):
    keyword = forms.CharField(label='所在地', max_length=40, label_suffix='：')

#ソート
class SortForm(forms.Form):
    SORT_CHOICES = (
        ('', '-'*10),
        ('pu', '価格：昇順'),
        ('pd', '価格：降順'),
        ('mu', '面積：昇順'),
        ('md', '面積：降順'),
        ('au', '築年月：昇順'),
        ('ad', '築年月：降順')
    )
    sort_s = forms.ChoiceField(
        label = '表示順',
        widget = forms.Select,
        choices = SORT_CHOICES,
        required = False,
    )

#問い合わせフォーム
class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "お名前※必須",
        }),
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': "メールアドレス※必須",
        }),
    )
    phone = forms.CharField(
        label='',
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "電話番号",
        }),
    )
    date = forms.CharField(
        label='',
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "内見希望日",
        }),
    )
    message = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "希望条件 / 質問 / 要望\n他にご興味がある物件があれば物件番号を入力してください。",
        }),
    )
    magagine = forms.BooleanField(
        label='希望条件に合う物件があればメール連絡を希望する',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'check',
        }),
    )

    #def send_email(self):
    def send_email(self,article):
    #def send_email(self):
        subject = "お問い合わせ"
        email = self.cleaned_data['email']

        inquiry  = "物件番号：\n" + article.bknNumber + "\n\n"
        inquiry += "名前：\n" + self.cleaned_data['name'] + "\n\n"
        inquiry += "メールアドレス：\n" + email + "\n\n"
        inquiry += "電話番号：\n" + self.cleaned_data['phone'] + "\n\n"
        inquiry += "内見希望日時：\n" + self.cleaned_data['date'] + "\n\n"
        inquiry += "メッセージ：\n" + self.cleaned_data['message'] + "\n\n"
        inquiry += "メルマガ希望：\n" + str(self.cleaned_data['magagine'])

        #from_email = '{name} <{email}>'.format(name=name, email=email)
        #from_email = settings.DEFAULT_FROM_EMAIL  # 送信者
        #recipient_list = ["toritoritorina@gmail.com"]  # 宛先リスト
        from_email = email
        recipient_list = [settings.EMAIL_HOST_USER]  # 受信者リスト
        try:
            send_mail(subject, inquiry, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")


#画像
class PhotosForm(forms.Form):
    photos_field = forms.ImageField(
        label = '',
        widget=forms.ClearableFileInput(attrs={'multiple': True}))



#初期値設定
#initial='Text',
#initial=user.email,

#メアドのデフォルト
#http://hideharaaws.hatenablog.com/entry/2017/02/05/021111
#https://narito.ninja/blog/detail/43/
#
#pkをどうやって取得する？ログインユーザーのIDを取るには？
#user = get_object_or_404(User, pk=pk)
#user = get_object_or_404(User, pk=1)
#user = self.request.user
