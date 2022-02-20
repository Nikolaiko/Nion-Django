from django.contrib import admin
from django.urls import path
from .views import initPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', initPage)
]
