from django.conf.urls import include, url
from django.contrib import admin

from sarahjaine.views import AboutView, HomeView, WorkList, WorkDetail

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^work/$', WorkList.as_view(), name='work_list'),
    url(r'^work/$', WorkDetail.as_view(), name='work_detail'),
    url(r'^admin/', include(admin.site.urls)),
]
