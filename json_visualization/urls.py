from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'json_visualization.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'store.views.index',name='index'),
    # url(r'^store/', 'store.views.store',name='store'),
    url(r'^store/',include('store.urls'),name='store'),
    url(r'^admin/', include(admin.site.urls)),
]
