from __future__ import unicode_literals

from django.urls import re_path as url

from markitup.views import apply_filter

urlpatterns = [
    url(r'preview/$', apply_filter, name='markitup_preview'),
]
