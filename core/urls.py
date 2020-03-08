from django.conf.urls import url

from core.views import Redirection

app_name = 'core'

urlpatterns = [
    url(r'^redirect/(?P<url>\w+)/$', Redirection.as_view(), name='redirect'),
]
