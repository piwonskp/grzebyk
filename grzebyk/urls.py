from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

from grzebyk import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'grzebyk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^galeria/', include('photologue.urls', namespace='photologue')),
    url(r'^', include('mainapp.urls')),
)
urlpatterns += static(settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT)
