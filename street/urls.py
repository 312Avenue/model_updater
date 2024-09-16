from rest_framework import routers

from .views import StreetViews, HomeViews

router = routers.SimpleRouter()
router.register(r'street', StreetViews)
router.register(r'home', HomeViews)

urlpatterns = []
urlpatterns += router.urls
