from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="EDUGIEUN API",
      default_version='v1',
      description="Contents of edugieun's repo",
      terms_of_service="https://help.github.com/en/github/site-policy",
      contact=openapi.Contact(email="gieun625@gmail.com"),
      license=openapi.License(name="License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name = 'api'

urlpatterns = [
    path('problems/', views.problem_list),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
