from django.urls import path
from website.views import *
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
from . import views

app_name = 'website'\

sitemaps = {'static':StaticViewSitemap}
urlpatterns = [
    path('', index_view, name = 'index'),
    path('about/', about_view, name = 'about'),
    path('contact/', contact_view, name = 'contact'),
    path('elements/',elements_view, name = 'elements'),
    path('newsletter/',newsletter_view, name = 'newsletter'),
    path('test/',test_view, name = 'test'),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
