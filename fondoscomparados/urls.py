from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from fondoscomparados.apps.viviendas import urls as viviendas_urls
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'fondoscomparados.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^admin/', admin.site.urls),
    url('^$', include(viviendas_urls)),
]
