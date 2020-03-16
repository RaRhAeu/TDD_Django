from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from lists.views import home_page

urlpatterns = [
    url(r'^$', home_page, name='home'),
    # path('admin/', admin.site.urls),
]
