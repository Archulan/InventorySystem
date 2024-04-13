from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from items.views import ItemViewSet
from batches.views import BatchViewSet
from itemtypes.views import ItemTypeViewSet
from items.views import SubmitData
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'batches', BatchViewSet)
router.register(r'itemtypes', ItemTypeViewSet)


schema_view = get_schema_view(
   openapi.Info(
       title="Inventory API",
       default_version='v1',
       description="API documentation for the Inventory Management System",
       terms_of_service="https://www.google.com/policies/terms/",
       contact=openapi.Contact(email="contact@inventory.local"),
       license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/submit-data/', SubmitData.as_view(), name='submit-data'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]