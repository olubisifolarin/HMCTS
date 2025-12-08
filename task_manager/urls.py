from django.contrib import admin
from django.urls import path
from tasks.views import TaskListCreateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.shortcuts import redirect

def home(request):
    return redirect('/api/tasks/')

schema_view = get_schema_view(
   openapi.Info(
      title="Tasks API",
      default_version='v1',
      description="API documentation for the Task Manager",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/tasks/', TaskListCreateView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
    path('swagger.json/', schema_view.without_ui(cache_timeout=0)),
]
