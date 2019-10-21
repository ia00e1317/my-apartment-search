from django.urls import path
from . import views

from .views import ContactFormView, ContactResultView

from .views import photos

app_name = 'toppage'

urlpatterns = [
    #問い合わせフォーム
    path('contact/<int:id>', ContactFormView.as_view(), name='contact_form'),
    path('contact/result/', ContactResultView.as_view(), name='contact_result'),

    #csv、画像
    path('upload',views.upload,name='upload'),
    path('photos',views.photos,name='photos'),
    path('photos/delete',views.photosdelete,name='delete'),
    #他ページ
    path('about2dk',views.about2dk,name='about2dk'),

    path('',views.index,name='index'),
    path('<str:roomtype>',views.index,name='index'),
    path('<str:roomtype>/<int:id>',views.detail,name='detail'),

    path('<str:roomtype>/<int:id>/pictureup',views.pictureup,name='pictureup'),
    path('<str:roomtype>/<int:id>/delete',views.delete,name='delete'),
    path('<str:roomtype>/<int:id>/soldout',views.soldout,name='soldout'),

]


