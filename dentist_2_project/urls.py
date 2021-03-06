
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dentist_2_project.core.urls')),
    path('accounts/', include('dentist_2_project.accounts.urls')),
    path('services/', include('dentist_2_project.services.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
