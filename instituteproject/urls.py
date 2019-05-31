"""instituteproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from instituteapp import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',views.home_page),
    url(r'^contact/',views.contact_page),
    url(r'^courses/',views.courses_page),
    url(r'^feedback/',views.feedback_page),
    url(r'^ourteam/',views.team_page),
    url(r'^gallery/',views.gallery_page),


    url(r'^$',views.main_page)
]
