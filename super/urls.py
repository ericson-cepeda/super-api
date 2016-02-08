from django.conf.urls import patterns, include, url
from application.api.views import ErrorView
from django.contrib import admin

from django.conf.urls.static import static
from super.settings.base import DEBUG, STATIC_URL, STATIC_DEV

admin.autodiscover()

urlpatterns = []

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_DEV)

urlpatterns += [
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^services/', include('application.api.urls', namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^.*/$',ErrorView.as_view(),name='error'),
]