
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('toppage/', include('toppage.urls')),
    path('', RedirectView.as_view(url='/toppage/')),
    path('accounts/', include('accounts.urls')),	#追→
    path('accounts/', include('django.contrib.auth.urls')),	#追→
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)