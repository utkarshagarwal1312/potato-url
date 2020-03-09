from django.conf.urls import url

from core.views import Redirection, CreateMapping

app_name = 'core'

urlpatterns = [
    url(r'^redirect/(?P<key>\w+)/$', Redirection.as_view(), name='redirect'),
    url(r'^create/$', CreateMapping.as_view(), name='create_map')
]
