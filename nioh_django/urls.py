from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from welcomeapp.views import aboutPage, initPage
from charactersapp.views import AllChars, CurrentCharacter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', initPage),
    path('about/', aboutPage, name="about_path"),
    path('characters/', AllChars, name="all_chars"),
    path('current_charatcer/<str:charName>', CurrentCharacter, name="cur_char")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)