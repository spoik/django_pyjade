from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import BookListView

urlpatterns = patterns('',
    url(r'^$', BookListView.as_view(), name='book_list')
)
