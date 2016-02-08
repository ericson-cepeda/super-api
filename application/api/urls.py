from rest_framework import routers
from application.api.views import ArticleViewSet, StoreViewSet, ArticleFilterList
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'stores', StoreViewSet)

urlpatterns = [
    url('^articles/stores/(?P<store_id>.+)/$', ArticleFilterList.as_view()),
]

urlpatterns += router.urls