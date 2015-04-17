from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from mainapp.views import index_view, shop_view

urlpatterns = patterns('',
                       url(r'^$', index_view.IndexView.as_view()),
                       url(r'^kontakt/$', TemplateView.as_view(template_name='about.html')),
                       url(r'^sprzedaz/$', shop_view.ShopView.as_view()),
                       )
