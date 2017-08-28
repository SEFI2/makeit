
from django.conf.urls import url, include
from django.contrib import admin
from blogs.models import Blog as blog_model
from django.conf import settings
from django.conf.urls.static import static




from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^blogs/', include('blogs.urls' , namespace='blogs')),
    url(r'^users/', include('profiles.urls' , namespace='profiles')),
    url(r'^messenger/', include('messenger.urls', namespace='messenger')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)