from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from mainapp.views import index, shop

urlpatterns = patterns('',
                       url(r'^$', index.Index.as_view()),
                       url(r'^kontakt/$', TemplateView.as_view(template_name='about.html')),
                       url(r'^sprzedaz/$', shop.Shop.as_view()),
                       )
