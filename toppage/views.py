from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Article

from django.contrib.auth.decorators import login_required   #追加
from django.contrib.auth.mixins import LoginRequiredMixin   #追加

from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from . import forms
#from .forms import ArticleForm

import csv   #追加
from io import TextIOWrapper, StringIO   #追加

from .models import SimplePhoto

import os
import shutil

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



#今回はやらないが今後の実装を考える事項
#登録にメールアドレスを利用する
#CSSファイルの切り出し
#一括問い合わせ機能は必要か？まとめて物件情報送ります
#未完成：画像ファイル削除機能
#未完成：登録メアドを問い合わせフォームのデフォルト入力


def index(request, roomtype='all'):
    searchForm = forms.SearchForm(request.GET)

    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        if roomtype == 'all':
            articles = Article.objects.filter(address1__contains=keyword)
        elif  roomtype == '2dk':
            articles = Article.objects.filter(address1__contains=keyword,planType__contains='2DK')
        else:
            articles = Article.objects.filter(address1__contains=keyword,planType__contains='3DK')
    else:
        searchForm = forms.SearchForm()
        if roomtype == 'all':
            articles = Article.objects.all()#.order_by('price').reverse()
        elif  roomtype == '2dk':
            articles = Article.objects.filter(planType__contains='2DK')
        else:
            articles = Article.objects.filter(planType__contains='3DK')


    #ソート：価格、面積、築年月、(所在地)
    sortForm = forms.SortForm(request.GET or None)
    sortValue = ''
    if sortForm.is_valid():
        sortValue = request.GET.get('sort_s', None)
        #if sortValue[0:1] == "p"
        #if sortValue[1:2] == "u"
        if sortValue == 'pu':
            articles = articles.order_by('price')
        elif sortValue == 'pd':
            articles = articles.order_by('price').reverse()
        elif sortValue == 'mu':
            articles = articles.order_by('exclusiveArea')
        elif sortValue == 'md':
            articles = articles.order_by('exclusiveArea').reverse()
        elif sortValue == 'au':
            articles = articles.order_by('constructionDate')
        elif sortValue == 'ad':
            articles = articles.order_by('constructionDate').reverse()


    message = roomtype
    if roomtype == 'all':
        message = '全件'
    else:
        message = ' ' + message

    rowlen = len(articles)
    i = 1
    rownum = 0
    headerrpeat = []
    while rownum <= rowlen:
        rownum = i * 9
        rownum += 1        
        i += 1
        headerrpeat.append(rownum)
    #headerrpeat = [10,19,28,37,46,55,64,73,82,91,100]

    context = {
        'message': message,
        'articles': articles,
        'searchForm': searchForm,
        'roomtype' : roomtype,
        'headerrpeat' : headerrpeat,
        'sortForm': sortForm,
    }
    return render(request,'toppage/index.html',context)


def about2dk(request):
    return render(request, 'toppage/about2dk.html')

@login_required
def detail(request, id, roomtype):
    article = get_object_or_404(Article, pk=id)
    context = {
        'message' : '物件詳細',
        'article' : article,
        'roomtype' : roomtype,
        #'id' : str(id),
    }
    return render(request, 'toppage/detail.html', context)

def delete(request, id, roomtype):
    #権限
    if not request.user.is_staff:
        return render(request, 'toppage/error.html')

    article = get_object_or_404(Article, pk=id)
    article.delete()

    articles = Article.objects.all()

    message = roomtype
    if roomtype == 'all':
        message = '全件'
    else:
        message = ' ' + message

    rowlen = len(articles)
    i = 1
    rownum = 0
    headerrpeat = []
    while rownum <= rowlen:
        rownum = i * 9
        rownum += 1        
        i += 1
        headerrpeat.append(rownum)

    #空
    searchForm = forms.SearchForm()
    sortForm = forms.SortForm()

    context = {
        'message': message,
        'articles': articles,
        'roomtype': roomtype,
        'headerrpeat' : headerrpeat,
        #フォーム
        'searchForm': searchForm,
        'sortForm': sortForm,
    }
    return render(request, 'toppage/index.html', context)

#soldout
def soldout(request, id, roomtype):
    #権限
    if not request.is_staff:
        return render(request, 'toppage/error.html')

    article = get_object_or_404(Article, pk=id)
    article.soldout = '1'
    article.save()

    articles = Article.objects.all()

    message = roomtype
    if roomtype == 'all':
        message = '全件'
    else:
        message = ' ' + message

    rowlen = len(articles)
    i = 1
    rownum = 0
    headerrpeat = []
    while rownum <= rowlen:
        rownum = i * 9
        rownum += 1        
        i += 1
        headerrpeat.append(rownum)

    #空
    searchForm = forms.SearchForm()
    sortForm = forms.SortForm()

    context = {
        'message': message,
        'articles': articles,
        'roomtype': roomtype,
        'headerrpeat' : headerrpeat,
        #フォーム
        'searchForm': searchForm,
        'sortForm': sortForm,
    }
    return render(request, 'toppage/index.html', context)


#pictureup
def pictureup(request, id, roomtype):
    #権限
    if not request.user.is_staff:
        return render(request, 'toppage/error.html')

    article = get_object_or_404(Article, pk=id)
    article.pictureFlag = '写真あり'
    article.save()

    articles = Article.objects.all()

    message = roomtype
    if roomtype == 'all':
        message = '全件'
    else:
        message = ' ' + message

    rowlen = len(articles)
    i = 1
    rownum = 0
    headerrpeat = []
    while rownum <= rowlen:
        rownum = i * 9
        rownum += 1        
        i += 1
        headerrpeat.append(rownum)

    #空
    searchForm = forms.SearchForm()
    sortForm = forms.SortForm()

    context = {
        'message': message,
        'articles': articles,
        'roomtype': roomtype,
        'headerrpeat' : headerrpeat,
        #フォーム
        'searchForm': searchForm,
        'sortForm': sortForm,
    }
    return render(request, 'toppage/index.html', context)


#問い合わせフォーム
class ContactFormView(LoginRequiredMixin,FormView): #BaseFormView
    model = Article
    template_name = 'contact/contact_form.html'
    form_class = forms.ContactForm
    success_url = reverse_lazy('toppage:contact_result')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["datas"] = Article.objects.all()
        id = self.kwargs.get('id')   #
        context["article"] = Article.objects.get(pk=id)
        #user = self.request.user
        #context["user"] = user
        return context

    #def form_valid(self, form):
    #def form_valid(self, form, id):
    def form_valid(self, form, **kwargs):
        #
        id = self.kwargs.get('id')
        article = Article.objects.get(pk=id)#1797
        #form.send_email()
        form.send_email(article)
        return super().form_valid(form)

class ContactResultView(LoginRequiredMixin,TemplateView):
    template_name = 'contact/contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "お問い合わせは正常に送信されました。"
        context['clsose_message'] = "ブラウザを閉じてください。"
        return context


#データ作成
def upload(request):
    #権限
    if not request.user.is_staff:
        return render(request, 'toppage/error.html')

    if 'csv' in request.FILES:
        Article.objects.all().delete()

        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='ANSI')
#        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        for i,line in enumerate(csv_file):
            #article, created = Articleup.objects.get_or_create(no=line[0])
            #article = Article(no=line[0])

            if i == 0:
                continue

            article = Article()
            article.bknNumber = line[0]#
            article.bknName = line[18]#

            if line[46] != '':
                linestr = line[46]
                article.price = "{:,}".format(int(linestr[0:len(linestr)-4]))#

            if line[48] != '':
                linestr = line[48]
                integerPrt = "{:,}".format(int(linestr[0:len(linestr)-4]))
                decimalPrt = linestr[len(linestr)-4:len(linestr)-3]
                article.priceTsubo = integerPrt + '.' + decimalPrt
                #article.priceTsubo = "{:,}".format(int(linestr[0:len(linestr)-4]))#★★★

            if line[49] != '':
                linestr = line[49]
                integerPrt = "{:,}".format(int(linestr[0:len(linestr)-4]))
                decimalPrt = linestr[len(linestr)-4:len(linestr)-3]
                article.priceSquare = integerPrt + '.' + decimalPrt
                #article.priceSquare = "{:,}".format(int(linestr[0:len(linestr)-4]))#★★★

            if line[133] and line[132]:
                lst = ['dm0', 'dm1', 'dm2', 'DK']
                idx = int(line[132])
                if lst[idx:idx+1]:
                    article.planType = line[133] + lst[idx]
                else:
                    article.planType = '???'
            #article.planType = line[133] + '★' + line[132] + '★'#

            article.planRoom = line[164]#
            article.address1 = line[14] + line[15]#
            article.address2 = line[16]#
            article.railwayLine = line[22]#
            article.station1 = line[23]#
            article.walkMin1 = line[24]#★★★
            article.walkMet1 = line[25]#★★★
            article.station2 = line[32]#####
            article.walkMin2 = line[33]#★★★
            article.walkMet2 = line[34]#★★★
            article.environment = line[189]#
            article.environmentMet = line[190]#★★★
            article.environmentMin = line[191]#★★★

            if line[35]:
                lst = ['dm0', '居住中', '空家', '賃貸中']
                idx = int(line[35])
                if lst[idx:idx+1]:
                    article.status = lst[idx]
                else:
                    article.status = '???'
            #article.status = line[35]

            if line[3]:
                lst = ['dm0', 'dm1', '中古マンション']
                idx = int(line[3])
                if lst[idx:idx+1]:
                    article.bknType = lst[idx]
                else:
                    article.bknType = '???'
            #article.bknType = line[3]

            article.bknTrade = line[2]
            article.exclusiveArea = line[57]#★★★
            article.balArea = line[60]#★★★
            
            if line[97]:
                lst = ['dm0', '有', '無']
                idx = int(line[97])
                if lst[idx:idx+1]:
                    article.associationFlag = lst[idx]
                else:
                    article.associationFlag = '???'
            #article.associationFlag = line[97]

            if line[98]:
                lst = ['dm0', '自主管理', '管理会社に一部委託', '管理会社に全部委託']
                idx = int(line[98])
                if lst[idx:idx+1]:
                    article.associationType = lst[idx]
                else:
                    article.associationType = '???'
            #article.associationType = line[98]

            if line[101] != '':
                article.administrative = "{:,}".format(int(line[101]))#★★★

            if line[103] != '':
                article.repairReserve = "{:,}".format(int(line[103]))#★★★

            if line[172]:
                lst = ['dm0', 'dm1', 'dm2', '鉄骨造', 'ＲＣ', 'ＳＲＣ', 'dm6', 'dm7', '軽量鉄骨', 'その他']
                idx = int(line[172])
                if lst[idx:idx+1]:
                    article.structure = lst[idx]
                else:
                    article.structure = '???'
            #article.structure = line[172]

            article.stairs = line[177] + '／' + line[175]#

            if line[182]:
                lst = ['dm0', '北', '北東', '東', '南東', '南', '南西', '西', '北西']
                idx = int(line[182])
                if lst[idx:idx+1]:
                    article.balDirection = lst[idx]
                else:
                    article.balDirection = '???'
            #article.balDirection = line[182]

            linestr = line[178]
            article.constructionDate = linestr[0:4] + '年' + linestr[4:6] + '月'#

            linestr = line[183]
            article.extensionDate1 = linestr[0:4] + '年' + linestr[4:6] + '月'#

            article.extensionHistory1 = line[184]

            linestr = line[185]
            article.extensionDate2 = linestr[0:4] + '年' + linestr[4:6] + '月'#

            article.extensionHistory2 = line[186]

            linestr = line[187]
            article.extensionDate3 = linestr[0:4] + '年' + linestr[4:6] + '月'#
            
            article.extensionHistory3 = line[188]
            article.pictureFlag = "写真なし"#line[197]
            #article.soldout = 

            article.save()


    context = { 'message': 'csvファイルアップロード', }
    return render(request, 'toppage/upload.html', context)


def photos(request):
    #権限
    if not request.user.is_staff:
        return render(request, 'toppage/error.html')

    images = SimplePhoto.objects.all()
    if request.method == 'POST':
        form = forms.PhotosForm(request.POST, request.FILES)
        if form.is_valid():
            for ff in request.FILES.getlist('photos_field'):
                p = SimplePhoto(img=ff)
                p.save()
    else:
        form = forms.PhotosForm()
    
    context = {
        'images': images, 
        'form': form,
        'message': '画像アップロード',
    }

    return render(request, 'toppage/photos.html', context)


def photosdelete(request):
    #権限
    if not request.user.is_staff:
        return render(request, 'toppage/error.html')

    #path = '../../../media/images'
    #if os.path.exists(path):
    #    shutil.rmtree(path)
    #    os.makedirs('../media/images')

    images = SimplePhoto.objects.all()
    images.delete()
    form = forms.PhotosForm()

    context = {
        'images': images, 
        'form': form,
        'message': '作成中：画像削除機能',
    }

    return render(request, 'toppage/photos.html', context)
