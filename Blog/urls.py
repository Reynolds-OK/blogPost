from django.contrib import admin
from django.urls import path, include
from articles import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.article_list, name='home'),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('profile/', include('users.urls')),
]


urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
