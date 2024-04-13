from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from items.views import ItemViewSet
from batches.views import BatchViewSet
from itemtypes.views import ItemTypeViewSet
from items.views import SubmitData

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'batches', BatchViewSet)
router.register(r'itemtypes', ItemTypeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/submit-data/', SubmitData.as_view(), name='submit-data'),
]