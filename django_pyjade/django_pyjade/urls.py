from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('home.urls')),

    # Admin routes
    url(r'^admin/', include(admin.site.urls)),
)
