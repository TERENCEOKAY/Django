"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import current_datatime, display_meta
from mysite.books import views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^hello/$', hello),
    # url(r'^$', my_home_page_view),
    url(r'^time/$', current_datatime),
    # url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    # url(r'^books/$', book_list),
    url(r'^display_meta/$', display_meta),
    # url(r'^search_form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact/$', views.contact),
    url(r'^contact/thanks/$', views.thanks),
]
