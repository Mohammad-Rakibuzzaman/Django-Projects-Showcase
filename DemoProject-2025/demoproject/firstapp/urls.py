from django.urls import path
from . import views


urlpatterns = [
      path('func_site', views.hello_func),
      path('class_site', views.heloClass.as_view())
]